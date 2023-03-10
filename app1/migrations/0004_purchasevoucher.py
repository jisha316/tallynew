# Generated by Django 4.0.4 on 2023-01-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_stock_itemcreation_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='purchasevoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10, null=True)),
                ('invoice_no', models.CharField(max_length=100, null=True)),
                ('party_accname', models.CharField(max_length=200, null=True)),
                ('purchase_ledger', models.CharField(max_length=200, null=True)),
                ('date', models.DateField(null=True)),
                ('item_name', models.CharField(max_length=100, null=True)),
                ('quantity', models.CharField(max_length=100, null=True)),
                ('rate', models.CharField(max_length=100, null=True)),
                ('per', models.CharField(max_length=100, null=True)),
                ('amount', models.CharField(max_length=100, null=True)),
                ('total', models.CharField(max_length=100, null=True)),
                ('narration', models.TextField(null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
            ],
        ),
    ]
