from django.db import models

# Create your models here.
class Constituency(models.Model):
	constituency_id = models.IntegerField(null=True)
	region_id = models.IntegerField(null=True)
	constituency_name = models.CharField(max_length=200,null=True)
	constituency_polling_stations = models.IntegerField(null=True)
	constituency_female_voters = models.IntegerField(null=True)
	constituency_male_voters = models.IntegerField(null=True)
	constituency_create_date = models.DateTimeField(null=True)
	constituency_popn = models.IntegerField(null=True)
	languages = models.CharField(max_length=200,null=True)
	political_history = models.CharField(max_length=6500,null=True)
	category_id = models.IntegerField(null=True)

	def __str__(self):
		return self.constituency_name

	class Meta:
		verbose_name_plural = "Constituency"

class Constituency_category(models.Model):
	category_id = models.IntegerField(null=True)
	cons_category_name = models.IntegerField(null=True)

	def __str__(self):
		return self.cons_category_name
	class Meta:
		verbose_name_plural = "Constituency_category"


class Country(models.Model):
	country_id = models.IntegerField(null=True)
	country_name = models.CharField(max_length=50,null=True)
	country_polling_stations = models.IntegerField(null=True)
	country_female_voters = models.IntegerField(null=True)
	country_male_voters = models.IntegerField(null=True)
	country_add_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.country_name
	class Meta:
		verbose_name_plural = "Country"

class Electoral_positions(models.Model):
	position_id = models.IntegerField(null=True)
	position_name = models.CharField(max_length=100,null=True)
	position_create_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.position_name
	class Meta:
		verbose_name_plural = "Electoral_position"

class Groups(models.Model):
	STATUS = (
			('',''),
			('','')
		)
	groupId = models.IntegerField(null=True)
	groupName = models.CharField(max_length=100,null=True)
	status = models.CharField(max_length=50,null=True,choices=STATUS)

	class Meta:
		verbose_name_plural = "Groups"


class Parties(models.Model):
	part_id = models.IntegerField(null=True)
	party_name = models.CharField(max_length=100,null=True)
	party_create_date = models.DateTimeField(max_length=50,null=True)


	def __str__(self):
		return self.party_name

	class Meta:
		verbose_name_plural = "Parties"

class Permissions(models.Model):
	permissionId = models.IntegerField(null=True)
	moduleName = models.CharField(max_length=100,null=True)
	fileName = models.CharField(max_length=100,null=True)
	createdAt = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.moduleName
	class Meta:
		verbose_name_plural = "Permissions"

class Permissions_map(models.Model):
	permissionMapId = models.IntegerField(null=True)
	groupId = models.IntegerField(null=True)
	permissionId = models.IntegerField(null=True)
	createdData = models.DateTimeField(auto_now_add=True,null=True)
	updateData = models.CharField(max_length=100,null=True)
	deleteData = models.CharField(max_length=100,null=True)
	viewData = models.CharField(max_length=100,null=True)
	dateMapped = models.DateTimeField(null=True)

	def __str__(self):
		return self.permissionMapId

	class Meta:
		verbose_name_plural = "Permissions_map"

class Politician_activities(models.Model):
	activity_id = models.IntegerField(null=True)
	politician_id = models.IntegerField(null=True)
	activity_desc = models.IntegerField(null=True)

	def __str__(self):
		return self.politician_id
	class Meta:
		verbose_name_plural = "Politician_activities"

class Politician_education(models.Model):
	education_id = models.IntegerField(null=True)
	politician_id = models.IntegerField(null=True)
	school_name = models.CharField(max_length=100,null=True)
	certificate_name = models.CharField(max_length=100,null=True)
	date_from = models.DateTimeField(null=True)
	date_to = models.DateTimeField(null=True)

	def __str__(self):
		return self.education_id
	class Meta:
		verbose_name_plural = "Politician_education"

class Politicians(models.Model):
	politician_id = models.IntegerField(null=True)
	position_id = models.IntegerField(null=True)
	constituency_id = models.IntegerField(null=True)
	party_id = models.IntegerField(null=True)
	politician_status = models.CharField(max_length=100,null=True)
	first_name = models.CharField(max_length=100,null=True)
	last_name = models.CharField(max_length=100,null=True)
	other_name = models.CharField(max_length=100,null=True)
	DOB = models.DateTimeField(null=True)

	def __str__(self):
		return self.first_name
	class Meta:
		verbose_name_plural = "Politician"

class Regions(models.Model):
	region_id = models.IntegerField(null=True)
	country_id = models.IntegerField(null=True)
	region_name = models.CharField(max_length=100,null=True)
	region_polling_stations = models.IntegerField(null=True)
	region_female_voters = models.IntegerField(null=True)
	region_male_voters = models.IntegerField(null=True)
	region_create_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.region_name
	class Meta:
		verbose_name_plural = "Regions"
class Systemlogs(models.Model):
	logId = models.IntegerField(null=True)
	userId = models.IntegerField(null=True)
	modelName = models.CharField(max_length=100,null=True)
	action = models.CharField(max_length=100,null=True)
	message = models.CharField(max_length=100,null=True)
	timeAccessed = models.DateTimeField(null=True)

	def __str__(self):
		return self.logId
	class Meta:
		verbose_name_plural = "Systemlogs"
class User_permissions(models.Model):
	moduleName = models.CharField(max_length=50,null=True)
	groupId = models.IntegerField(null=True)
	fileName = models.CharField(max_length=100, null=True)
	createData = models.CharField(max_length=50,null=True)
	updateData = models.CharField(max_length=50,null=True)
	deleteData = models.CharField(max_length=50,null=True)
	viewData = models.CharField(max_length=50,null=True)

	def __str__(self):
		return self.moduleName
	class Meta:
		verbose_name_plural = "Users_permissions"

class User_profile(models.Model):
	userId = models.IntegerField(null=True)
	groupId = models.IntegerField(null=True)
	username = models.CharField(max_length=50,null=True)
	firstName = models.CharField(max_length=50,null=True)
	lastName = models.CharField(max_length=50,null=True)
	address = models.CharField(max_length=50,null=True)
	primaryTelephone = models.CharField(max_length=50,null=True)
	secondaryTelephone = models.CharField(max_length=50,null=True)
	secondaryEmail = models.EmailField(max_length=254,null=True)
	DOB = models.DateTimeField(null=True)
	regDate = models.DateTimeField(null=True)
	modifyDate = models.DateTimeField(null=True)
	image = models.ImageField(null=True)

	def __str__(self):
		return self.username
	class Meta:
		verbose_name_plural = "User_profile"

class Users(models.Model):
	userId = models.IntegerField(null=True)
	username = models.CharField(max_length=50,null=True)
	password = password = models.CharField(max_length=50)
	groupId = models.IntegerField(null=True)
	verificationCode = models.IntegerField(null=True)
	verificationStatus = models.CharField(max_length=50,null=True)
	verificationExpiry = models.DateTimeField(null=True)
	accountStatus = models.CharField(max_length=50,null=True)
	firstName = models.CharField(max_length=50,null=True)
	lastName = models.CharField(max_length=50,null=True)
	address = models.CharField(max_length=50,null=True)
	primaryTelephone = models.CharField(max_length=50,null=True)
	secondaryTelephone = models.CharField(max_length=50,null=True)
	secondaryEmail = models.EmailField(max_length=254,null=True)
	DOB = models.DateTimeField(null=True)
	regDate = models.DateTimeField(null=True)


	def __str__(self):
		return self.username
	class Meta:
		verbose_name_plural = "Users"

class Users_session(models.Model):
	userId = models.IntegerField(null=True)
	hash = models.CharField(max_length=200,null=True)

	def __str__(self):
		return self.userId
	class Meta:
		verbose_name_plural = "Users_session"


