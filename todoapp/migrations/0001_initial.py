# Generated by Django 4.1.1 on 2022-10-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('status', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]
