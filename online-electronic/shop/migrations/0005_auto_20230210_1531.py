# Generated by Django 3.2.17 on 2023-02-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201230_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='user',
        ),
    ]
