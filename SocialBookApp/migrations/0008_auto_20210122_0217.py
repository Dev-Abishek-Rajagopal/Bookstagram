# Generated by Django 3.1.5 on 2021-01-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0007_auto_20210122_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_user',
            name='username',
            field=models.CharField(default='user', max_length=200),
        ),
    ]
