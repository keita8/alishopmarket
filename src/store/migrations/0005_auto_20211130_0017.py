# Generated by Django 3.1.4 on 2021-11-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20211130_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('Neuf', 'Neuf'), ('Usagé', 'Usagé'), ('Ancien', 'Ancien')], max_length=200),
        ),
    ]
