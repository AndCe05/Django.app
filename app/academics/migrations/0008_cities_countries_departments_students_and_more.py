# Generated by Django 5.0.2 on 2024-03-18 03:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0007_alter_person_created_at_alter_person_updated_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('abrev', models.CharField(blank=True, max_length=10)),
                ('descrip', models.CharField(blank=True, max_length=10)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 222909))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 222909))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('abrev', models.CharField(blank=True, max_length=10)),
                ('descrip', models.CharField(blank=True, max_length=10)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 223906))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 223906))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('abrev', models.CharField(blank=True, max_length=10)),
                ('descrip', models.CharField(blank=True, max_length=10)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 223906))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 223906))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('abrev', models.CharField(blank=True, max_length=10)),
                ('descrip', models.CharField(blank=True, max_length=100)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 224904))),
                ('created_at', models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 224904))),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 222909)),
        ),
        migrations.AlterField(
            model_name='person',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 222909)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 194987)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 17, 22, 39, 50, 194987)),
        ),
    ]
