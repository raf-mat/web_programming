# Generated by Django 5.1.4 on 2025-03-08 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(blank=True, default='image.png', upload_to='media/'),
        ),
    ]
