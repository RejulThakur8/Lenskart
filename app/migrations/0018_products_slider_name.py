# Generated by Django 5.1.3 on 2024-12-07 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_slider_slider_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slider_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='s_name', to='app.slider'),
            preserve_default=False,
        ),
    ]
