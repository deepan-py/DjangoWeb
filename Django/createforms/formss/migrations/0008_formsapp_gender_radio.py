# Generated by Django 2.2.5 on 2020-12-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0007_formsapp_datetimeofentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsapp',
            name='gender_radio',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
