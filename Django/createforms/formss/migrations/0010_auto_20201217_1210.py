# Generated by Django 2.2.5 on 2020-12-17 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0009_auto_20201217_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsapp',
            name='imgesAdd',
            field=models.ImageField(upload_to='templates/'),
        ),
    ]