# Generated by Django 3.1.2 on 2022-05-16 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
        migrations.RemoveField(
            model_name='car',
            name='factory',
        ),
        migrations.RemoveField(
            model_name='car',
            name='name',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price',
        ),
    ]
