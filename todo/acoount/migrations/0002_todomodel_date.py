# Generated by Django 5.0.2 on 2024-02-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acoount', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
