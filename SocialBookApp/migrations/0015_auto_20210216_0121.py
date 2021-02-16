# Generated by Django 3.1.5 on 2021-02-15 19:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SocialBookApp', '0014_auto_20210215_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_user',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
