# Generated by Django 5.1.3 on 2024-12-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_remove_products_airess10_remove_products_airess9_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='slider_name',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
    ]