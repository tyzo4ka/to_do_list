# Generated by Django 2.2.5 on 2019-09-09 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20190909_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='detailed',
            field=models.TextField(blank=True, default=None, max_length=5000, null=True, verbose_name='Подробнее'),
        ),
    ]