# Generated by Django 3.0.4 on 2020-03-08 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='type',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
