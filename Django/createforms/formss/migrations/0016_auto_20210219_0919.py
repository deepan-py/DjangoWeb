# Generated by Django 3.1.6 on 2021-02-19 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0015_auto_20210218_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formsapp',
            name='imgesAdd',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
    ]