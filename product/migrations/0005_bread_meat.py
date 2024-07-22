# Generated by Django 5.0.7 on 2024-07-21 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_turi_turi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('foydalari', models.CharField(max_length=200)),
                ('turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.turi')),
            ],
        ),
        migrations.CreateModel(
            name='Meat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('foydalari', models.CharField(max_length=200)),
                ('turi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.turi')),
            ],
        ),
    ]
