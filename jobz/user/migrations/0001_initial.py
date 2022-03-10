# Generated by Django 4.0.2 on 2022-03-06 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('name', models.CharField(max_length=500)),
                ('cpf', models.BigIntegerField(primary_key=True, serialize=False)),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.person')),
            ],
            bases=('user.person',),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='user.person')),
            ],
            bases=('user.person',),
        ),
    ]