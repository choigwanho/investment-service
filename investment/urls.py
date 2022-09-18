from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>', views.accountView, name='account'), # 투자 화면
    path('account-asset/<str:pk>', views.accountAssetView, name='account-asset'), # 투자 상세 화면
    path('asset-group/<str:fk>', views.assetGroupView, name='asset-group'), # 보유 종목 화면
]
