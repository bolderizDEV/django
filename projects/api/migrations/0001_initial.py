# Generated by Django 2.1.5 on 2019-01-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField(max_length=6)),
                ('department_id', models.IntegerField(max_length=2)),
            ],
        ),
    ]
