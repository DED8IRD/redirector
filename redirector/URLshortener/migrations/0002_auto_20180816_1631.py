# Generated by Django 2.0 on 2018-08-16 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('URLshortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='access_count',
            field=models.IntegerField(default=0),
        ),
    ]
