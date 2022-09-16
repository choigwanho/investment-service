from django.db import models
from django.conf import settings


class Account(models.Model):
    """
    계좌 테이블
    """
    # 계좌 번호
    account_number = models.CharField(max_length=100)
    # 계좌명
    account_name = models.CharField(max_length=50)
    # 증권사
    broker_name = models.CharField(max_length=50)
    # 계좌 총 자산
    total_amount = models.IntegerField(default=0)
    # 사용자 이름
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "계좌"
        verbose_name_plural = "계좌"

    def __str__(self):
        return f'{self.user_name} {self.account_number}'


class AccountInvest(models.Model):
    """
    계좌 투자 정보 테이블
    """
    # 계좌 번호
    account_number = models.ForeignKey('Account', related_name='Account', on_delete=models.CASCADE)
    # 보유 종목 ISIN
    isin = models.ForeignKey('StockGroup', related_name='StockGroup', on_delete=models.CASCADE)
    # 종목 현재가
    current_price = models.IntegerField(default=0)
    # 종목 보유 수량
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name = "계좌 투자 정보"
        verbose_name_plural = "계좌 투자 정보"

    def __str__(self):
        return self.account_number


class StockGroup(models.Model):
    """
    종목 정보 테이블
    """
    # 종목  ISIN
    isin = models.CharField(max_length=50)
    # 종목명
    item_name = models.CharField(max_length=50)
    # 종목의 자산군
    group_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "종목 정보"
        verbose_name_plural = "종목 정보"

    def __str__(self):
        return self.isin
