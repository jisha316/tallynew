# Generated by Django 4.0.4 on 2023-01-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_purchase_voucher_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasevoucher',
            name='no',
            field=models.IntegerField(null=True),
        ),
    ]
