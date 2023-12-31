# Generated by Django 3.0 on 2023-07-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='access',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_timme', models.DateTimeField(auto_now_add=True, db_column='create_time', verbose_name='创建时间')),
                ('no', models.CharField(max_length=16, verbose_name='学号')),
                ('results', models.CharField(max_length=8, verbose_name='结果')),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='姓名')),
                ('sex', models.CharField(max_length=2, verbose_name='性别')),
                ('address', models.CharField(max_length=40, verbose_name='地址')),
                ('no', models.CharField(max_length=10, verbose_name='学号')),
            ],
            options={
                'unique_together': {('name', 'sex', 'address')},
            },
        ),
    ]
