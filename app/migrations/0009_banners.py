# Generated by Django 5.1.3 on 2024-12-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_frame'),
    ]

    operations = [
        migrations.CreateModel(
            name='banners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banners_image', models.ImageField(default='air', upload_to='statics/images')),
                ('banners_name', models.CharField(max_length=50)),
                ('banner_head', models.CharField(default='Hustlr', max_length=60)),
            ],
        ),
    ]