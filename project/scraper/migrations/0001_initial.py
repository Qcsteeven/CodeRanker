# Generated by Django 5.1.4 on 2024-12-19 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Нет названия', max_length=255)),
                ('author', models.CharField(blank=True, default='Нет автора', max_length=255)),
                ('price', models.CharField(blank=True, default='Нет цены', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ind', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=255)),
                ('rating', models.CharField(max_length=50)),
                ('change', models.CharField(max_length=50)),
            ],
        ),
    ]
