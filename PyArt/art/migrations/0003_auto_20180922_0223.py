# Generated by Django 2.1.1 on 2018-09-22 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0002_art_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='/static/assets/placeholder.png', upload_to='media')),
            ],
        ),
        migrations.RemoveField(
            model_name='art',
            name='picture',
        ),
        migrations.AddField(
            model_name='picture',
            name='art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_picture', to='art.Art'),
        ),
    ]
