# Generated by Django 5.2 on 2025-04-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='medicine_images/'),
        ),
    ]
