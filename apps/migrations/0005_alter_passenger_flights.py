# Generated by Django 5.1.2 on 2024-10-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_rename_passanger_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='flights',
            field=models.ManyToManyField(blank=True, related_name='passangers', to='apps.flight'),
        ),
    ]
