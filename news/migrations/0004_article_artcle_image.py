# Generated by Django 4.0.3 on 2022-03-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='artcle_image',
            field=models.ImageField(default='', upload_to='articles/'),
        ),
    ]