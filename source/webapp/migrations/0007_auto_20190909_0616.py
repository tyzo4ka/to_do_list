# Generated by Django 2.2.5 on 2019-09-09 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190909_0613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='detailed',
            field=models.TextField(default=None, max_length=5000, null=True, verbose_name='Подробнее'),
        ),
    ]
