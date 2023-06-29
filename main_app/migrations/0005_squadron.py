# Generated by Django 4.2.2 on 2023-06-28 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_spacecraft'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squadron',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('Spacecraft', models.ManyToManyField(to='main_app.spacecraft')),
            ],
        ),
    ]
