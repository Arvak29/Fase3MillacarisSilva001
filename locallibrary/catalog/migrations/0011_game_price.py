# Generated by Django 3.1.2 on 2020-10-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_remove_game_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='price',
            field=models.CharField(default=0, max_length=9),
            preserve_default=False,
        ),
    ]