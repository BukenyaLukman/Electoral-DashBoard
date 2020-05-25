# Generated by Django 3.0.6 on 2020-05-22 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='constituency',
            options={'verbose_name_plural': 'Constituency'},
        ),
        migrations.AlterModelOptions(
            name='constituency_category',
            options={'verbose_name_plural': 'Constituency_category'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Country'},
        ),
        migrations.AlterModelOptions(
            name='electoral_positions',
            options={'verbose_name_plural': 'Electoral_position'},
        ),
        migrations.AlterModelOptions(
            name='groups',
            options={'verbose_name_plural': 'Groups'},
        ),
        migrations.AlterModelOptions(
            name='parties',
            options={'verbose_name_plural': 'Parties'},
        ),
        migrations.AlterModelOptions(
            name='permissions',
            options={'verbose_name_plural': 'Permissions'},
        ),
        migrations.AlterModelOptions(
            name='permissions_map',
            options={'verbose_name_plural': 'Permissions_map'},
        ),
        migrations.AlterModelOptions(
            name='politician_activities',
            options={'verbose_name_plural': 'Politician_activities'},
        ),
        migrations.AlterModelOptions(
            name='politician_education',
            options={'verbose_name_plural': 'Politician_education'},
        ),
        migrations.AlterModelOptions(
            name='politicians',
            options={'verbose_name_plural': 'Politician'},
        ),
        migrations.AlterModelOptions(
            name='regions',
            options={'verbose_name_plural': 'Regions'},
        ),
        migrations.AlterModelOptions(
            name='systemlogs',
            options={'verbose_name_plural': 'Systemlogs'},
        ),
        migrations.AlterModelOptions(
            name='user_permissions',
            options={'verbose_name_plural': 'Users_permissions'},
        ),
        migrations.AlterModelOptions(
            name='user_profile',
            options={'verbose_name_plural': 'User_profile'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='users_session',
            options={'verbose_name_plural': 'Users_session'},
        ),
        migrations.RemoveField(
            model_name='politicians',
            name='constituency_id',
        ),
        migrations.AddField(
            model_name='politicians',
            name='constituency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Constituency'),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='constituency_female_voters',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='constituency',
            name='constituency_male_voters',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='constituency_category',
            name='cons_category_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='groups',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'ACTIVE'), ('NOT ACTIVE', 'NOT ACTIVE')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='politician_activities',
            name='activity_desc',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]