# Generated by Django 4.0 on 2023-07-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpostmodel_slug_alter_blogpostmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostmodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='post-images'),
        ),
    ]
