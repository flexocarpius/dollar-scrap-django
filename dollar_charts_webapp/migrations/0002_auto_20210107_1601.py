# Generated by Django 3.1.5 on 2021-01-08 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dollar_charts_webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
