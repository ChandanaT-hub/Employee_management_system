# Generated by Django 4.2.6 on 2023-10-26 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=200)),
                ('a_name', models.CharField(max_length=200)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
