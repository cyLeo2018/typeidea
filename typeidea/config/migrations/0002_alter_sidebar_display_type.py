# Generated by Django 4.1 on 2022-09-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sidebar',
            name='display_type',
            field=models.PositiveIntegerField(choices=[(1, 'HTML'), (2, '最新文章'), (3, '最热文章'), (4, '最新评论')], default=1, verbose_name='展示类型'),
        ),
    ]
