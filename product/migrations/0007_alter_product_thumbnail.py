# Generated by Django 4.1.5 on 2023-02-01 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
    ]