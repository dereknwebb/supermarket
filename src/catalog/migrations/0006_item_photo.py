# Generated by Django 3.1.2 on 2020-12-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201121_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='items/default.png', upload_to='items'),
        ),
    ]
