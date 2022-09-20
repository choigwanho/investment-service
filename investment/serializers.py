from rest_framework import serializers
from investment.models import Account, Asset, AssetGroup, Transfer
from django.contrib.auth import get_user_model


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ["account_number",
                  "user_name",
                  "transfer_amount"]


class AssetGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetGroup
        fields = ["isin",
                  "asset_name",
                  "group_name"]


class AssetSerializer(serializers.ModelSerializer):
    # 보유 종목의 평가 금액
    market_value = serializers.SerializerMethodField(read_only=True)
    group = AssetGroupSerializer(read_only=True)

    class Meta:
        model = Asset
        fields = ["market_value",
                  "current_price",
                  "quantity",
                  "group"]

    def get_market_value(self, obj):
        return obj.quantity * obj.current_price


class AccountAssetSerializer(serializers.ModelSerializer):
    assets = AssetSerializer(many=True, read_only=True)
    # 계좌 총 자산
    total_amount = serializers.SerializerMethodField(read_only=True)
    # 총 수익금
    total_benefit = serializers.SerializerMethodField(read_only=True)
    # 수익률
    roi = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = ["id",
                  "account_name",
                  "brokerage",
                  "account_number",
                  "total_amount",
                  "invest_amount",
                  "total_benefit",
                  "roi",
                  "assets"]

    def get_total_amount(self, obj):
        amount = 0
        for asset in obj.assets.all():
            amount += asset.current_price * asset.quantity
        return amount

    def get_total_benefit(self, obj):
        benefit = self.get_total_amount(obj) - obj.invest_amount
        return benefit

    def get_roi(self, obj):
        return_of_invest = (self.get_total_benefit(obj)/obj.invest_amount)*100
        return round(return_of_invest, 2)


class UserAccountSerializer(serializers.ModelSerializer):
    accounts = AccountAssetSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["username", "accounts"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"