# Generated by Django 4.0.2 on 2022-03-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePurchase', models.DateField()),
                ('dateSevice', models.DateField()),
                ('serviceDesription', models.CharField(max_length=5000)),
            ],
        ),
    ]
