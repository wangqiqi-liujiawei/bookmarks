# Generated by Django 4.2.3 on 2023-07-16 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_alter_image_slug_alter_image_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='total_likes',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
