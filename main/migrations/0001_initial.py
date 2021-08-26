# Generated by Django 3.2.3 on 2021-07-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=122, null=True)),
                ('email', models.CharField(blank=True, max_length=70, null=True)),
                ('subject', models.CharField(blank=True, default='', max_length=12, null=True)),
                ('message', models.TextField(blank=True, default='', max_length=12, null=True)),
                ('date', models.DateField(blank=True, default='', max_length=12, null=True)),
            ],
        ),
    ]
