# Generated by Django 3.2.19 on 2023-05-31 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('url', models.CharField(max_length=200)),
                ('user_name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('time_ago', models.CharField(max_length=200)),
                ('comments', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
