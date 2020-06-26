# Generated by Django 3.0.5 on 2020-06-25 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20200624_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='electoral_positions',
            options={'verbose_name_plural': 'Electoral Position'},
        ),
        migrations.RemoveField(
            model_name='constituency_category',
            name='constituency',
        ),
        migrations.AddField(
            model_name='constituency',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Constituency_category'),
        ),
        migrations.AlterField(
            model_name='electoral_positions',
            name='position_update_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='parties',
            name='party_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='politician_activities',
            name='activity_desc',
            field=models.CharField(max_length=500, null=True),
        ),
    ]