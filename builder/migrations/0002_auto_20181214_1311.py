# Generated by Django 2.1.3 on 2018-12-14 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='colors',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='flavor',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='manaCost',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
