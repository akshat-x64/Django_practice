# Generated by Django 4.2.2 on 2023-07-10 12:36

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50)),
                ('news_description', tinymce.models.HTMLField()),
            ],
        ),
    ]