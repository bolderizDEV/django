# Generated by Django 2.1.5 on 2019-01-06 09:39

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
                ('employee_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('phone_number', models.CharField(max_length=20)),
                ('hire_date', models.DateField()),
                ('job_id', models.CharField(max_length=10)),
                ('salary', models.FloatField(max_length=8.2)),
                ('commission_pct', models.FloatField(max_length=2.2)),
                ('manager_id', models.IntegerField()),
                ('department_id', models.IntegerField()),
            ],
        ),
    ]
