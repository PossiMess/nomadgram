# Generated by Django 2.0.9 on 2019-01-10 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_like_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='images.Image'),
        ),
    ]
