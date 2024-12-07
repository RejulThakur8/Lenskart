# Generated by Django 5.1.3 on 2024-12-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_products_frame_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(default='air', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_color', models.CharField(default='black', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='size',
            name='frame_size',
            field=models.CharField(default='medium', max_length=50),
        ),
    ]