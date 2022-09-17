from django.urls import path
from . import views

urlpatterns = [
    path('account/<str:pk>', views.AccountView, name='account'), # 투자 화면
    path('account-asset/<str:pk>', views.accountAssetView, name='account-asset'), # 투자 상세 화면
    path('my-asset/', views.myAssetView, name='my-asset'), # 보유 종목 화면
]
