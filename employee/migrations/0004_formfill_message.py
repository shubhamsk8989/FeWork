# Generated by Django 4.2.6 on 2024-03-29 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_formfill'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfill',
            name='message',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
