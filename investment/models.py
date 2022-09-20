from django.db import models
from django.contrib.auth import get_user_model


class Account(models.Model):
    """
    계좌 테이블
    """
    # 계좌 번호
    account_number = models.CharField(max_length=100)
    # 계좌명
    account_name = models.CharField(max_length=50)
    # 증권사
    brokerage = models.CharField(max_length=50)
    # 투자금
    invest_amount = models.IntegerField(default=0)
    # 사용자 이름
    user = models.ForeignKey(get_user_model(), related_name='accounts', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "계좌"
        verbose_name_plural = "계좌"

    def __str__(self):
        return f'{self.account_number}'


class AssetGroup(models.Model):
    """
    자산 그룹 테이블
    """
    # 종목  ISIN
    isin = models.CharField(max_length=50)
    # 종목명
    asset_name = models.CharField(max_length=50)
    # 종목의 자산군
    group_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "자산 그룹 정보"
        verbose_name_plural = "자산 그룹 정보"

    def __str__(self):
        return f'{self.isin}'


class Asset(models.Model):
    """
    자산 정보 테이블
    """
    # 계좌 번호
    account = models.ForeignKey('Account', related_name='assets', on_delete=models.CASCADE)
    # 보유 종목 ISIN
    group = models.ForeignKey('AssetGroup', on_delete=models.CASCADE)
    # 종목 현재가
    current_price = models.IntegerField(default=0)
    # 종목 보유 수량
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = "계좌 자산 정보"
        verbose_name_plural = "계좌 자산 정보"

    def __str__(self):
        return f'{self.account_id} {self.group_id}'


class Transfer(models.Model):
     """
     입금 거래 테이블
     """
     account_number = models.CharField(max_length=100)
     user_name = models.CharField(max_length=100)
     transfer_amount = models.IntegerField(default=0)

     class Meta:
         verbose_name = "입금 거래 정보"
         verbose_name_plural = "입금 거래 정보"

     def __str__(self):
         return f'{self.account_number} {self.user_name} {self.transfer_amount}'