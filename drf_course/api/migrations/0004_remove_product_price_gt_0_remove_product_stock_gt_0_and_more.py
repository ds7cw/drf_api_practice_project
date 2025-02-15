# Generated by Django 5.1.5 on 2025-02-15 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_product_price_gt_0_product_stock_gt_0'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='product',
            name='price_gt_0',
        ),
        migrations.RemoveConstraint(
            model_name='product',
            name='stock_gt_0',
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(condition=models.Q(('price__gte', 0)), name='price_gte_0'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.CheckConstraint(condition=models.Q(('stock__gte', 0)), name='stock_gte_0'),
        ),
    ]
