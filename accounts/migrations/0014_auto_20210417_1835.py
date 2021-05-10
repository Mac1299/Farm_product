# Generated by Django 3.2 on 2021-04-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='product',
            name='transaction_id',
        ),
        migrations.AddField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
