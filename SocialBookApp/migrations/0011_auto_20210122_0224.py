# Generated by Django 3.1.5 on 2021-01-21 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0010_bookcomments_ownbook_textbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilecomment',
            name='friend',
        ),
        migrations.RemoveField(
            model_name='profilecomment',
            name='you',
        ),
        migrations.DeleteModel(
            name='friendlist',
        ),
        migrations.DeleteModel(
            name='profileComment',
        ),
    ]
