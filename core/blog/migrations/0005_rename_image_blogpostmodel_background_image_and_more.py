# Generated by Django 4.0 on 2023-07-29 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpostmodel_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpostmodel',
            old_name='image',
            new_name='background_image',
        ),
        migrations.AddField(
            model_name='blogpostmodel',
            name='image1',
            field=models.ImageField(blank=True, upload_to='post-images'),
        ),
        migrations.AddField(
            model_name='blogpostmodel',
            name='image2',
            field=models.ImageField(blank=True, upload_to='post-images'),
        ),
    ]