# Generated by Django 2.0.3 on 2018-03-14 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceryapp', '0003_auto_20180314_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grocerylist',
            name='coupons',
        ),
        migrations.AddField(
            model_name='grocerylist',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groceryapp.Coupon'),
        ),
    ]