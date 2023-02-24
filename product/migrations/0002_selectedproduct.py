# Generated by Django 4.1.6 on 2023-02-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='selectedProduct',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('picture', models.URLField()),
                ('productName', models.CharField(max_length=200)),
                ('availableQuantity', models.IntegerField()),
                ('pricePerUnit', models.FloatField()),
                ('description', models.TextField()),
            ],
        ),
    ]
