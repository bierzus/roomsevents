# Generated by Django 4.1.5 on 2023-01-31 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('number', models.CharField(max_length=5)),
                ('capacity', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]
