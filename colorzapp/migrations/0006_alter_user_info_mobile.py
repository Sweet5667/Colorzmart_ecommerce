# Generated by Django 4.1.4 on 2022-12-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colorzapp', '0005_user_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='mobile',
            field=models.CharField(max_length=10),
        ),
    ]
