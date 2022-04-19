# Generated by Django 4.0.2 on 2022-04-13 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_provider_occupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderPresentation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentationPhoto', models.ImageField(upload_to='images')),
                ('description', models.CharField(max_length=5000)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='user.provider')),
            ],
        ),
    ]
