# Generated by Django 2.0.2 on 2019-07-23 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_Name', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'mood',
            },
        ),
    ]
