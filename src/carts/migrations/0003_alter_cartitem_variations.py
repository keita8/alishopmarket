# Generated by Django 3.2.4 on 2021-12-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_variation'),
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='variations',
            field=models.ManyToManyField(to='store.Variation', verbose_name='Caracteristiques'),
        ),
    ]
