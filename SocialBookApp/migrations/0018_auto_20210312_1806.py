# Generated by Django 3.1.5 on 2021-03-12 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0017_bookusertree_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownbook',
            name='referrer',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, related_name='referrer', to='SocialBookApp.app_user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ownbook',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Buyer', to='SocialBookApp.app_user'),
        ),
        migrations.CreateModel(
            name='BookTreeDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tree', models.IntegerField(default=0)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book')),
            ],
        ),
    ]
