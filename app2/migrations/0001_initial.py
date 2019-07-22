# Generated by Django 2.1 on 2019-07-22 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('landmark', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
            ],
            options={
                'db_table': 'country_Info',
            },
        ),
    ]
