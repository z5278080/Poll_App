# Generated by Django 3.0.6 on 2020-06-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_loggedinuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four',
            field=models.CharField(default=4, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]