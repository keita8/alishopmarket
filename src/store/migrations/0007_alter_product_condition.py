# Generated by Django 3.2.9 on 2021-11-30 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211130_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='condition',
            field=models.CharField(blank=True, choices=[('Nouveauté', 'Nouveauté'), ('Usagé', 'Usagé'), ('Ancien', 'Ancien')], max_length=200),
        ),
    ]
