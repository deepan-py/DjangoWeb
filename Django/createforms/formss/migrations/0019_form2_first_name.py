# Generated by Django 3.1.6 on 2021-02-19 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0018_auto_20210219_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='form2',
            name='first_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]