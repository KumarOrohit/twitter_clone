# Generated by Django 3.2.7 on 2021-09-17 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='tweets',
            field=models.TextField(default='', max_length=300),
        ),
    ]
