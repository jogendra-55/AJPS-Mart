# Generated by Django 4.0.2 on 2022-03-12 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grocerywebsite', '0006_orderplaced_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='product',
        ),
    ]
