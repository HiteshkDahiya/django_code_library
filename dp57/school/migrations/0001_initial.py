# Generated by Django 5.2 on 2025-04-11 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('name', models.CharField(max_length=80)),
                ('roll', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
