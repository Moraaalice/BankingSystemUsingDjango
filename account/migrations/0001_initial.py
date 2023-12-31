# Generated by Django 4.2.3 on 2023-07-12 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transactionIdentificationNumber', models.CharField(max_length=20)),
                ('TransactionType', models.CharField(max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
