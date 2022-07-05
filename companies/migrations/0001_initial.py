# Generated by Django 4.0.6 on 2022-07-05 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('last_update_at', models.DateTimeField(auto_now=True, verbose_name='')),
                ('locale', models.CharField(default='-03:00', max_length=50)),
                ('lang', models.CharField(default='pt', max_length=5)),
                ('created_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_users', to='users.users')),
                ('users', models.ManyToManyField(to='users.users')),
            ],
        ),
    ]