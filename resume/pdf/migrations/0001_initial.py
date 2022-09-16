# Generated by Django 4.1.1 on 2022-09-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('skills', models.TextField(max_length=1000)),
                ('about_you', models.TextField(max_length=1000)),
                ('previous_work', models.TextField(max_length=1000)),
            ],
        ),
    ]
