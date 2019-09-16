# Generated by Django 2.2.5 on 2019-09-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20190909_0647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='detailed',
            field=models.TextField(blank=True, default='', max_length=3000, null=True, verbose_name='Подробнее'),
        ),
    ]
