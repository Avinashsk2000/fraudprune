# Generated by Django 4.0 on 2022-05-15 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0012_transaction_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='status',
            field=models.IntegerField(),
        ),
    ]
