# Generated by Django 5.1.2 on 2024-10-25 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sklad', '0004_delete_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='materials',
        ),
    ]
