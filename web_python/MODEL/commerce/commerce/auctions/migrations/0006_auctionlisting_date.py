# Generated by Django 5.1.4 on 2025-03-03 21:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
