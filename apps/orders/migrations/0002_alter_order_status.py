# Generated by Django 4.2.6 on 2023-10-12 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('inproses', 'В обработке')], default='new', max_length=20),
        ),
    ]
