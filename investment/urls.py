from django.urls import path
from . import views

urlpatterns = [
    path('account', views.account_view, name='account'), # 투자 화면
    path('account-asset/<str:pk>', views.account_asset_view, name='account-asset'), # 투자 상세 화면
    path('asset/<str:fk>', views.asset_view, name='asset'), # 보유 종목 화면
    path('transfer-amount-1/', views.transfer_amount_1, name='transfer-amount-1'), # 투자금 입금 Phase 1
    path('transfer-amount-2/', views.transfer_amount_2, name='transfer-amount-2'), # 투자금 입금 Phase 2
]
