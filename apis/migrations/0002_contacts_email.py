# Generated by Django 3.1.3 on 2020-12-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
