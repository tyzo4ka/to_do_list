# Generated by Django 2.2.5 on 2019-09-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20190909_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete_before',
            field=models.DateField(blank=True, default=None, max_length=10, null=True, verbose_name='Выполнить до'),
        ),
    ]
