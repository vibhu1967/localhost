# Generated by Django 4.0.6 on 2022-08-14 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('factories', '0002_products_alter_companies_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='factories.companies'),
        ),
    ]
