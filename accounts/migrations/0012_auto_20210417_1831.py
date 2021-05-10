# Generated by Django 3.2 on 2021-04-17 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210417_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.AddField(
            model_name='product',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]