# Generated by Django 3.1.2 on 2020-12-08 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_order_pickup_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pickup_time_slot',
            field=models.CharField(blank=True, choices=[('m', 'Morning (9AM - 11AM'), ('n', 'Midday (12PM - 2PM)'), ('e', 'Evening (4PM - 6PM')], default='m', max_length=1),
        ),
    ]
