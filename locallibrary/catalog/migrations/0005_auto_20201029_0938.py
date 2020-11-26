# Generated by Django 3.1.2 on 2020-10-29 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201028_1646'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='developer',
        ),
        migrations.AddField(
            model_name='game',
            name='developer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.developer'),
        ),
    ]