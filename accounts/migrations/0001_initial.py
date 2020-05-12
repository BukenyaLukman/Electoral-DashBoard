# Generated by Django 3.0.6 on 2020-05-11 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('constituency_id', models.IntegerField(null=True)),
                ('region_id', models.IntegerField(null=True)),
                ('constituency_name', models.CharField(max_length=200, null=True)),
                ('constituency_polling_stations', models.IntegerField(null=True)),
                ('constituency_female_voters', models.IntegerField(null=True)),
                ('constituency_male_voters', models.IntegerField(null=True)),
                ('constituency_create_date', models.DateTimeField(null=True)),
                ('constituency_popn', models.IntegerField(null=True)),
                ('languages', models.CharField(max_length=200, null=True)),
                ('political_history', models.CharField(max_length=6500, null=True)),
                ('category_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constituency_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(null=True)),
                ('cons_category_name', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField(null=True)),
                ('country_name', models.CharField(max_length=50, null=True)),
                ('country_polling_stations', models.IntegerField(null=True)),
                ('country_female_voters', models.IntegerField(null=True)),
                ('country_male_voters', models.IntegerField(null=True)),
                ('country_add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Electoral_positions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_id', models.IntegerField(null=True)),
                ('position_name', models.CharField(max_length=100, null=True)),
                ('position_create_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupId', models.IntegerField(null=True)),
                ('groupName', models.CharField(max_length=100, null=True)),
                ('status', models.CharField(choices=[('', ''), ('', '')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_id', models.IntegerField(null=True)),
                ('party_name', models.CharField(max_length=100, null=True)),
                ('party_create_date', models.DateTimeField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissionId', models.IntegerField(null=True)),
                ('moduleName', models.CharField(max_length=100, null=True)),
                ('fileName', models.CharField(max_length=100, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permissions_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permissionMapId', models.IntegerField(null=True)),
                ('groupId', models.IntegerField(null=True)),
                ('permissionId', models.IntegerField(null=True)),
                ('createdData', models.DateTimeField(auto_now_add=True, null=True)),
                ('updateData', models.CharField(max_length=100, null=True)),
                ('deleteData', models.CharField(max_length=100, null=True)),
                ('viewData', models.CharField(max_length=100, null=True)),
                ('dateMapped', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Politician_activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_id', models.IntegerField(null=True)),
                ('politician_id', models.IntegerField(null=True)),
                ('activity_desc', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Politician_education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_id', models.IntegerField(null=True)),
                ('politician_id', models.IntegerField(null=True)),
                ('school_name', models.CharField(max_length=100, null=True)),
                ('certificate_name', models.CharField(max_length=100, null=True)),
                ('date_from', models.DateTimeField(null=True)),
                ('date_to', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Politicians',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('politician_id', models.IntegerField(null=True)),
                ('position_id', models.IntegerField(null=True)),
                ('constituency_id', models.IntegerField(null=True)),
                ('party_id', models.IntegerField(null=True)),
                ('politician_status', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('other_name', models.CharField(max_length=100, null=True)),
                ('DOB', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField(null=True)),
                ('country_id', models.IntegerField(null=True)),
                ('region_name', models.CharField(max_length=100, null=True)),
                ('region_polling_stations', models.IntegerField(null=True)),
                ('region_female_voters', models.IntegerField(null=True)),
                ('region_male_voters', models.IntegerField(null=True)),
                ('region_create_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Systemlogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logId', models.IntegerField(null=True)),
                ('userId', models.IntegerField(null=True)),
                ('modelName', models.CharField(max_length=100, null=True)),
                ('action', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=100, null=True)),
                ('timeAccessed', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moduleName', models.CharField(max_length=50, null=True)),
                ('groupId', models.IntegerField(null=True)),
                ('fileName', models.CharField(max_length=100, null=True)),
                ('createData', models.CharField(max_length=50, null=True)),
                ('updateData', models.CharField(max_length=50, null=True)),
                ('deleteData', models.CharField(max_length=50, null=True)),
                ('viewData', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('groupId', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('primaryTelephone', models.CharField(max_length=50, null=True)),
                ('secondaryTelephone', models.CharField(max_length=50, null=True)),
                ('secondaryEmail', models.EmailField(max_length=254, null=True)),
                ('DOB', models.DateTimeField(null=True)),
                ('regDate', models.DateTimeField(null=True)),
                ('modifyDate', models.DateTimeField(null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50)),
                ('groupId', models.IntegerField(null=True)),
                ('verificationCode', models.IntegerField(null=True)),
                ('verificationStatus', models.CharField(max_length=50, null=True)),
                ('verificationExpiry', models.DateTimeField(null=True)),
                ('accountStatus', models.CharField(max_length=50, null=True)),
                ('firstName', models.CharField(max_length=50, null=True)),
                ('lastName', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('primaryTelephone', models.CharField(max_length=50, null=True)),
                ('secondaryTelephone', models.CharField(max_length=50, null=True)),
                ('secondaryEmail', models.EmailField(max_length=254, null=True)),
                ('DOB', models.DateTimeField(null=True)),
                ('regDate', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users_session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(null=True)),
                ('hash', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
