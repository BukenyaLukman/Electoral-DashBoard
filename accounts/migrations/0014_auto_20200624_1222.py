# Generated by Django 3.0.6 on 2020-06-24 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200618_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_create_date',
            new_name='constituency_create_date',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_female_voters',
            new_name='constituency_female_voters',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_male_voters',
            new_name='constituency_male_voters',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_name',
            new_name='constituency_name',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_polling_stations',
            new_name='constituency_polling_stations',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_popn',
            new_name='constituency_popn',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Constituency_update_date',
            new_name='constituency_update_date',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Delete_status',
            new_name='delete_status',
        ),
        migrations.RenameField(
            model_name='constituency',
            old_name='Languages',
            new_name='languages',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_create_date',
            new_name='country_create_date',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_female_voters',
            new_name='country_female_voters',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_languages',
            new_name='country_languages',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_male_voters',
            new_name='country_male_voters',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_name',
            new_name='country_name',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_political_history',
            new_name='country_political_history',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_polling_stations',
            new_name='country_polling_stations',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_popn',
            new_name='country_popn',
        ),
        migrations.RenameField(
            model_name='country',
            old_name='Country_update_date',
            new_name='country_update_date',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='Department_name',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='Dept_create_date',
            new_name='dept_create_date',
        ),
        migrations.RenameField(
            model_name='electoral_positions',
            old_name='Position_create_date',
            new_name='position_create_date',
        ),
        migrations.RenameField(
            model_name='electoral_positions',
            old_name='Position_name',
            new_name='position_name',
        ),
        migrations.RenameField(
            model_name='electoral_positions',
            old_name='Position_update_date',
            new_name='position_update_date',
        ),
        migrations.RenameField(
            model_name='parties',
            old_name='Party_create_date',
            new_name='party_create_date',
        ),
        migrations.RenameField(
            model_name='parties',
            old_name='Party_update_date',
            new_name='party_update_date',
        ),
        migrations.RenameField(
            model_name='politician_education',
            old_name='Certificate_name',
            new_name='certificate_name',
        ),
        migrations.RenameField(
            model_name='politician_education',
            old_name='Date_from',
            new_name='date_from',
        ),
        migrations.RenameField(
            model_name='politician_education',
            old_name='Date_to',
            new_name='date_to',
        ),
        migrations.RenameField(
            model_name='politician_education',
            old_name='School_name',
            new_name='school_name',
        ),
        migrations.RemoveField(
            model_name='department',
            name='Dept_update_date',
        ),
        migrations.RemoveField(
            model_name='parties',
            name='Party_name',
        ),
        migrations.AddField(
            model_name='department',
            name='dept_update_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parties',
            name='party_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]