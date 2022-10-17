# Generated by Django 4.1.2 on 2022-10-17 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=10)),
                ('profile_pic', models.ImageField(upload_to='profile_pic')),
            ],
        ),
    ]