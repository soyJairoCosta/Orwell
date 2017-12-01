# Generated by Django 2.0rc1 on 2017-12-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrwellWeb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='os',
        ),
        migrations.AddField(
            model_name='node',
            name='gpu_info',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='gpu_number',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='operative_system',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='processor_name',
            field=models.CharField(blank=True, max_length=17, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='processor_number',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=1, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='ram_info',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='node',
            name='ram_number',
            field=models.IntegerField(blank=True, max_length=2, null=True),
        ),
    ]
