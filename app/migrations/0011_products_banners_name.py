# Generated by Django 5.1.3 on 2024-12-06 19:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_banners_banners_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='banners_name',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, related_name='ban_name', to='app.banners'),
        ),
    ]