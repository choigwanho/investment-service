from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from investment.models import Account, Asset, AssetGroup
from investment.serializers import UserAccountSerializer, AccountSerializer, AssetSerializer, AssetGroupSerializer
from django.contrib.auth import get_user_model


@api_view(['GET'])
def AccountView(request, pk):
    '''
    투자 화면
    '''
    user = get_user_model().objects.get(id=pk)
    serializer = UserAccountSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def accountAssetView(request, pk):
    '''
    투자 상세 화면
    '''
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def myAssetView(request):
    '''
    보유 종목 화면
    '''
    assets = AssetGroup.objects.all()
    serializer = AssetGroupSerializer(assets, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def transferAmount1(request,pk):g
    '''
    투자금 입금 Phase 1 API
    '''

    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(instance=account, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def transferAmount2(request,pk):
    '''
    투자금 입금 Phase 2 API
    '''

    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(instance=account, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
