# Generated by Django 2.1.7 on 2019-04-28 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190428_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='shop_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]