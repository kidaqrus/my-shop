# Generated by Django 2.2.2 on 2019-06-11 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_braintree_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='braintree_id',
        ),
    ]
