# Generated by Django 2.1.2 on 2018-12-05 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='oj_proxies',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]