# Generated by Django 4.0.1 on 2022-01-13 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0005_remove_customer_id_alter_customer_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='register_account',
            new_name='register_acc',
        ),
    ]