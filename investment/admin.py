from django.contrib import admin
from .models import Account, Asset, AssetGroup


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass


@admin.register(AssetGroup)
class AssetGroupAdmin(admin.ModelAdmin):
    pass
