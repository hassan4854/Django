# Generated by Django 3.1.2 on 2022-05-16 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelapp', '0003_auto_20220516_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='factory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='modelapp.factory'),
        ),
        migrations.AlterField(
            model_name='factory',
            name='name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
