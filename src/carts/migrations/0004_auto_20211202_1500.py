# Generated by Django 3.1.4 on 2021-12-02 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20211201_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='cart_id',
            field=models.CharField(blank=True, max_length=250, verbose_name='Panier'),
        ),
    ]
