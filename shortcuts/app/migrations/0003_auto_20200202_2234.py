# Generated by Django 2.2.5 on 2020-02-02 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('pdf', models.FileField(upload_to='static/media')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
