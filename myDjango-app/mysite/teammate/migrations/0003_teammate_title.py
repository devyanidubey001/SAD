# Generated by Django 4.0.2 on 2022-02-03 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammate', '0002_alter_teammate_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammate',
            name='title',
            field=models.CharField(default='Mr.', max_length=10),
            preserve_default=False,
        ),
    ]