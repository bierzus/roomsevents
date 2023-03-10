# Generated by Django 4.1.5 on 2023-01-31 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Public'), (2, 'Private')], default=1)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateTimeField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='room.room')),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='CustomerBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event.event')),
            ],
            options={
                'db_table': 'customer_book',
            },
        ),
        migrations.AddConstraint(
            model_name='customerbook',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'email', 'event'), name='unique_event_per_user'),
        ),
    ]
