# Generated by Django 3.0.5 on 2020-05-28 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20200528_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicians',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]