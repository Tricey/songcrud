# Generated by Django 4.1.2 on 2022-10-27 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('likes', models.IntegerField()),
                ('date_released', models.DateField()),
                ('artiste_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artiste')),
            ],
        ),
        migrations.CreateModel(
            name='lyrics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=400)),
                ('song_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.song')),
            ],
        ),
    ]
