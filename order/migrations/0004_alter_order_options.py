# Generated by Django 4.1.5 on 2023-01-30 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_paid_amount_orderitem_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
