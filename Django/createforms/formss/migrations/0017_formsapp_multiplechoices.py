# Generated by Django 3.1.6 on 2021-02-19 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formss', '0016_auto_20210219_0919'),
    ]

    operations = [
        migrations.AddField(
            model_name='formsapp',
            name='multipleChoices',
            field=models.CharField(choices=[('1', 'one'), ('2', 'two'), ('3', 'three')], default='1', max_length=1),
        ),
    ]
