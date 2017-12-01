# Generated by Django 2.0rc1 on 2017-12-01 12:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('address_IP', models.CharField(max_length=15)),
                ('mac_IP', models.CharField(blank=True, max_length=17, null=True)),
                ('address_IPMI', models.CharField(blank=True, max_length=15, null=True)),
                ('mac_IPMI', models.CharField(blank=True, max_length=17, null=True)),
                ('os', models.CharField(max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('system_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('warranty_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
