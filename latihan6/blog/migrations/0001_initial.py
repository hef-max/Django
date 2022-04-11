# Generated by Django 3.2.2 on 2021-06-11 01:21

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
                ('judul', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('category', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
