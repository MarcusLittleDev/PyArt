# Generated by Django 2.1.1 on 2018-09-11 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('out_of_stock', models.BooleanField(default=False)),
                ('picture', models.ImageField(upload_to='art/')),
            ],
        ),
    ]