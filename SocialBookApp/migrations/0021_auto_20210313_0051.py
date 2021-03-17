# Generated by Django 3.1.5 on 2021-03-12 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0020_booknewsfeed_friendnewsfeed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booknewsfeed',
            old_name='user',
            new_name='Author',
        ),
        migrations.AddField(
            model_name='booknewsfeed',
            name='Book',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booknewsfeed',
            name='referrer',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, related_name='feedreferrer', to='SocialBookApp.app_user'),
            preserve_default=False,
        ),
    ]