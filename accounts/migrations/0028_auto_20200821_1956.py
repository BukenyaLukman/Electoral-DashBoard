# Generated by Django 3.0.8 on 2020-08-21 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20200821_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electionresult',
            name='Constituency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Constituency'),
        ),
    ]
