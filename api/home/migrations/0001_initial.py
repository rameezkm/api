# Generated by Django 4.1 on 2022-12-22 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('product', models.CharField(max_length=20)),
                ('desc', models.TextField(max_length=10)),
            ],
        ),
    ]
