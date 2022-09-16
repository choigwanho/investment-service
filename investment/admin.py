from django.contrib import admin
from .models import Account, AccountInvest, StockGroup


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(AccountInvest)
class AccountInvestAdmin(admin.ModelAdmin):
    pass


@admin.register(StockGroup)
class StockGroupAdmin(admin.ModelAdmin):
    pass
