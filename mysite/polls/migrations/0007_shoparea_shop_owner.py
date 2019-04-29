# Generated by Django 2.1.7 on 2019-04-29 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0006_shoparea_isbooking'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoparea',
            name='shop_owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
