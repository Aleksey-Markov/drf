# Generated by Django 4.2 on 2024-08-19 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_payments_link_remove_payments_session_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursepurchase',
            name='amount',
            field=models.PositiveIntegerField(verbose_name='Сумма оплаты'),
        ),
    ]
