from rest_framework import serializers
from investment.models import Account, Asset, AssetGroup
from django.contrib.auth import get_user_model


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["current_price",
                  "quantity"]


class AssetGroupSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True, read_only=True)

    class Meta:
        model = AssetGroup
        fields = ["isin",
                  "asset_name",
                  "group_name",
                  "assets"]


class AccountSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True, read_only=True)

    class Meta:
        model = Account
        fields = ["account_number",
                  "account_name",
                  "brokerage",
                  "total_amount",
                  "assets"]


class UserAccountSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "accounts"]









