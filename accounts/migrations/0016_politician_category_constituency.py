# Generated by Django 3.0.5 on 2020-06-25 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20200625_0717'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician_category',
            name='constituency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Constituency_category'),
        ),
    ]
