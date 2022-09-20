import hashlib

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from investment.models import Account, Asset, Transfer
from investment.serializers import UserAccountSerializer, AccountAssetSerializer, AssetSerializer, TransferSerializer, AccountSerializer
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404


@api_view(['GET'])
def account_view(request):
    '''
    투자 화면 조회
        - 로그인한 사용자 id로 사용자의 계좌정보 조회
    '''
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), id=request.user.id)
        serializer = UserAccountSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def account_asset_view(request, pk):
    '''
    투자 상세 화면 조회
        - 계좌 id, 로그인한 사용자 id로 계좌 투자 정보 및 투자 상세 조회
    '''
    if request.user.is_authenticated:
        account = get_object_or_404(Account, id=pk, user=request.user.id)
        serializer = AccountAssetSerializer(account, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
def asset_view(request, fk):
    '''
    보유 종목 화면 조회
        - 계좌 id로 보유 종목 정보 조회
    '''
    if request.user.is_authenticated:
        is_valid_account_id = False
        accounts = Account.objects.filter(user=request.user.id)

        for account in accounts:
            if account.id == int(fk):
                is_valid_account_id = True
                break

        if not is_valid_account_id:
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        assets = Asset.objects.filter(account=fk)
        if assets.exists():
            serializer = AssetSerializer(assets, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': '보유종목이 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def transfer_amount_1(request):
    '''
    투자금 입금 Phase 1
    '''
    if request.user.is_authenticated:
        # 본인 확인
        if not (request.user.username == request.data['user_name']):
            return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)

        # 사용자 검증
        user = get_object_or_404(get_user_model(), username=request.data['user_name'])

        # 계좌 검증
        accounts = Account.objects.filter(user=user.id)
        account_flag = False

        for account in accounts:
            print(type(account.account_number), type(request.data['account_number']))
            if account.account_number == request.data['account_number']:
                account_flag = True
                break

        # 데이터 저장
        if account_flag:
            serializer = TransferSerializer(data=request.data, many=False)

            if serializer.is_valid():
                serializer.save()

                transfer_identifier = Transfer.objects.last().id

                return Response({'transfer_identifier': transfer_identifier})

            return Response({'message': '요청이 실패하였습니다'}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'message': '사용자의 계좌 정보가 없습니다.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def transfer_amount_2(request):
    '''
    투자금 입금 Phase 2
    '''
    if request.user.is_authenticated:
        signature = request.data['signature']
        transfer_identifier = request.data['transfer_identifier']

        transfer = get_object_or_404(Transfer, id=transfer_identifier)
        transfer_info_str = f'{transfer.account_number}{transfer.user_name}{transfer.transfer_amount}'

        transfer_hash = hashlib.sha3_512(transfer_info_str.encode('utf-8')).hexdigest()

        # hash 값 검증
        if signature == transfer_hash:

            account = get_object_or_404(Account, account_number=transfer.account_number)

            # 투자금 업데이트
            invest_amount = account.invest_amount + transfer.transfer_amount

            transfer_data = {
                "account_number": account.account_number,
                "account_name": account.account_name,
                "brokerage": account.brokerage,
                "invest_amount": invest_amount,
                "user": account.user.id
            }

            serializer = AccountSerializer(instance=account, data=transfer_data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': '권한이 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
