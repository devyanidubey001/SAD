# Generated by Django 4.0.2 on 2022-02-03 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammate',
            name='last_name',
            field=models.CharField(max_length=200),
        ),
    ]
