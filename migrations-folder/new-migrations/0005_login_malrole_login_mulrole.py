# Generated by Django 4.0.6 on 2022-08-23 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoticketapp', '0004_rename_mrole_register_marole_register_murole'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='malrole',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='login',
            name='mulrole',
            field=models.CharField(default='', max_length=20),
        ),
    ]
