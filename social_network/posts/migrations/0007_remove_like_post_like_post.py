# Generated by Django 4.2.11 on 2024-03-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_like_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post',
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='posts.post'),
        ),
    ]
