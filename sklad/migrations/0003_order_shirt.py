# Generated by Django 5.1.2 on 2024-10-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0002_remove_material_qty_remove_material_warehouse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Shirt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric_required', models.FloatField(default=0.8)),
                ('buttons_required', models.IntegerField(default=5)),
                ('thread_required', models.FloatField(default=10)),
            ],
        ),
    ]
