# Generated by Django 3.1.2 on 2020-11-01 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20201031_1728'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='img',
        ),
    ]
