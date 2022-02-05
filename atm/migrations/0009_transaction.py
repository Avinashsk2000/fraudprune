# Generated by Django 4.0.1 on 2022-01-14 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atm', '0008_remove_register_acc_current_pin'),
    ]

    operations = [
        migrations.CreateModel(
            name='transaction',
            fields=[
                ('Email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('unique_code_s', models.CharField(max_length=255)),
            ],
        ),
    ]
