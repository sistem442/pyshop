# Generated by Django 2.1 on 2020-01-01 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='Fruits', max_length=255),
        ),
    ]