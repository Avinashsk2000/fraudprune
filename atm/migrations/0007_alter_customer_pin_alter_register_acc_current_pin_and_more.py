# Generated by Django 4.0.1 on 2022-01-13 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0006_rename_register_account_register_acc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='PIN',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='register_acc',
            name='Current_PIN',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='register_acc',
            name='New_PIN',
            field=models.CharField(max_length=255),
        ),
    ]
