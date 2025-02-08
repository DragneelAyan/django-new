# Generated by Django 5.1.5 on 2025-02-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=250)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=10000)),
                ('genre', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reader', models.ManyToManyField(related_name='book', to='libraryapp.reader')),
            ],
        ),
    ]
