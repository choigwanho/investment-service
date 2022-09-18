from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from investment.models import Account, Asset, AssetGroup
from investment.serializers import UserAccountSerializer, AccountAssetSerializer, AssetSerializer, AssetGroupSerializer
from django.contrib.auth import get_user_model


@api_view(['GET'])
def accountView(request, pk):
    '''
    투자 화면 조회
    '''
    user = get_user_model().objects.get(id=pk)
    serializer = UserAccountSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def accountAssetView(request, pk):
    '''
    투자 상세 화면 조회
    '''
    account = Account.objects.get(id=pk)
    serializer = AccountAssetSerializer(account, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def assetGroupView(request, fk):
    '''
    보유 종목 화면 조회
    '''
    assets = Asset.objects.filter(account=fk)
    serializer = AssetSerializer(assets, many=True)
    return Response(serializer.data)


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
