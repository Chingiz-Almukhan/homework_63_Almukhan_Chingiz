# Generated by Django 4.1.1 on 2022-10-28 16:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('accounts', '0002_alter_account_managers_account_liked_posts_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='commented_posts',
            field=models.ManyToManyField(related_name='user_comments', to='posts.post', verbose_name='Прокомментированные публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='liked_posts',
            field=models.ManyToManyField(related_name='user_likes', to='posts.post', verbose_name='Понравившиеся публикации'),
        ),
        migrations.AlterField(
            model_name='account',
            name='subscriptions',
            field=models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, verbose_name='Подписки'),
        ),
    ]
