# Generated by Django 3.2 on 2021-04-17 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20210417_1831'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Vegitables', 'Vegitables'), ('Grains', 'Grains'), ('Fruits', 'Fruits')], max_length=200, null=True),
        ),
    ]
