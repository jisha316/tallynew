# Generated by Django 4.0.4 on 2023-01-24 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_purchasevoucher_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchasevoucher',
            name='voucher',
        ),
    ]
