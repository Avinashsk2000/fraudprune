# Generated by Django 4.0.1 on 2022-01-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0003_register_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register_account',
            name='id',
        ),
        migrations.AlterField(
            model_name='register_account',
            name='Email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
