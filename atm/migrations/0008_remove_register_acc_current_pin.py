# Generated by Django 4.0.1 on 2022-01-13 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0007_alter_customer_pin_alter_register_acc_current_pin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_acc',
            name='Current_PIN',
        ),
    ]
