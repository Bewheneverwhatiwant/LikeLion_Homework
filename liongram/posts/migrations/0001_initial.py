# Generated by Django 4.2.1 on 2023-05-12 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.IntegerField(verbose_name='이미지')),
                ('content', models.TimeField(verbose_name='내용')),
                ('created_at', models.DurationField(verbose_name='작성일')),
                ('view_count', models.IntegerField(verbose_name='조회수')),
            ],
        ),
    ]
