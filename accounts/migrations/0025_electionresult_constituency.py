# Generated by Django 3.0.8 on 2020-08-21 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_remove_electionresult_constituency'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionresult',
            name='Constituency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Constituency'),
        ),
    ]
