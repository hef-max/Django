# Generated by Django 3.2.2 on 2021-06-04 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='alamat',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
