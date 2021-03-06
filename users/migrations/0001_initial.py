# Generated by Django 4.0.6 on 2022-07-05 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=256)),
                ('last_password_redefinition', models.DateTimeField(auto_now=True, verbose_name='')),
                ('email_verified', models.BooleanField(default=False)),
                ('password', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('last_update_at', models.DateTimeField(auto_now=True, verbose_name='')),
            ],
        ),
    ]
