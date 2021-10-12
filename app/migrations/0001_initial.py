# Generated by Django 3.2.7 on 2021-10-08 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.PositiveIntegerField()),
                ('is_favorite', models.BooleanField()),
            ],
        ),
    ]
