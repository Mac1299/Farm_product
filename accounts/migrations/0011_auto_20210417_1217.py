# Generated by Django 3.2 on 2021-04-17 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20210412_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]