# Generated by Django 5.0 on 2023-12-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateField(auto_now_add=True),
        ),
    ]
