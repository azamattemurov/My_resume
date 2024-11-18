# Generated by Django 5.0.7 on 2024-11-17 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='album_image',
            new_name='album_thumbnail',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='title',
            new_name='artist_name',
        ),
        migrations.RemoveField(
            model_name='song',
            name='duration',
        ),
        migrations.AddField(
            model_name='song',
            name='song_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_file',
            field=models.FileField(upload_to='songs/'),
        ),
        migrations.AlterField(
            model_name='song',
            name='download_count',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
