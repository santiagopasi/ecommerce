# Generated by Django 4.1.7 on 2023-03-31 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_profile_email_profile_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
