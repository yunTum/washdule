# Generated by Django 3.0.3 on 2020-02-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_number', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('prefecture', models.CharField(max_length=10, verbose_name='都道府県')),
                ('time_start', models.TimeField(verbose_name='仕事開始時間')),
                ('time_end', models.TimeField(verbose_name='仕事終了時間')),
                ('scale', models.IntegerField(verbose_name='洗濯機の大きさ')),
            ],
        ),
    ]
