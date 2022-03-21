# Generated by Django 4.0.3 on 2022-03-21 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('countryclub_app', '0002_remove_club_is_deleted_remove_clubmembers_is_deleted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClubEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=512)),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='countryclub_app.clubmembers')),
            ],
            options={
                'db_table': 'club_events',
            },
        ),
    ]
