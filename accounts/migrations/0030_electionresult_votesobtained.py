# Generated by Django 3.0.8 on 2020-08-22 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0029_auto_20200822_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionresult',
            name='votesObtained',
            field=models.IntegerField(null=True),
        ),
    ]
