# Generated by Django 3.2 on 2022-09-17 08:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_auto_20220917_1710'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='account_number',
            new_name='account_id',
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='isin',
            new_name='group_id',
        ),
    ]