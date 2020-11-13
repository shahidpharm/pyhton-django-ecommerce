# Generated by Django 3.1.3 on 2020-11-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('keywords', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('phone', models.IntegerField()),
                ('fax', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('smtpserver', models.CharField(max_length=100)),
                ('smtpemail', models.EmailField(blank=True, max_length=50, null=True)),
                ('smtppassword', models.CharField(blank=True, max_length=50)),
                ('smtpport', models.CharField(blank=True, max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/')),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('address', models.TextField()),
                ('contact', models.TextField()),
                ('reference', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
