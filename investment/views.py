from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from investment.models import Account, Asset, AssetGroup
from investment.serializers import UserAccountSerializer, AccountAssetSerializer, AssetSerializer, AssetGroupSerializer
from django.contrib.auth import get_user_model

from django.shortcuts import get_object_or_404

@api_view(['GET'])
def accountView(request, pk):
    '''
    투자 화면 조회
        - 사용자 id로 사용자의 계좌정보 조회
    '''
    user = get_object_or_404(get_user_model(), id=pk)
    serializer = UserAccountSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def accountAssetView(request, pk):
    '''
    투자 상세 화면 조회
        - 계좌 id로 계좌 투자 정보 및 투자 상세 조회
    '''
    account = get_object_or_404(Account, id=pk)
    serializer = AccountAssetSerializer(account, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def assetView(request, fk):
    '''
    보유 종목 화면 조회
        - 계좌 id로 보유 종목 정보 조회
    '''
    assets = Asset.objects.filter(account=fk)
    if assets.exists():
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)
    else:
        return Response({'message': '보유종목이 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def transferAmount1(request, pk):
    '''
    투자금 입금 Phase 1
    '''

    account = Account.objects.get(id=pk)
    serializer = UserAccountSerializer(instance=account, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def transferAmount2(request,pk):
    '''
    투자금 입금 Phase 2
    '''

    account = Account.objects.get(id=pk)
    serializer = UserAccountSerializer(instance=account, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
