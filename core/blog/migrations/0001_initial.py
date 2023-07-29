# Generated by Django 4.0 on 2023-07-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('slug', models.SlugField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]