# Generated by Django 4.0.2 on 2022-04-01 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='occupation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='search.occupation'),
        ),
    ]
