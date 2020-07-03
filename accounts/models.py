from django.db import models



class Constituency_category(models.Model):
	cons_category_name = models.CharField(max_length=100,null=True)

	def __str__(self):
		return self.cons_category_name
	class Meta:
		verbose_name_plural = "Constituency_category"


class Constituency(models.Model):
	DELETE_STATUS = (
			('DELETED','DELETED'),
			('NOT DELETED','NOT DELETED'),
		)
	category = models.ForeignKey(Constituency_category,null=True,blank=True,on_delete=models.SET_NULL)
	constituency_name = models.CharField(max_length=200,null=True)
	constituency_polling_stations = models.IntegerField(null=True)
	constituency_female_voters = models.CharField(max_length=200,null=True)
	constituency_male_voters = models.CharField(max_length=200,null=True)
	constituency_create_date = models.DateTimeField(null=True)
	constituency_popn = models.IntegerField(null=True)
	languages = models.CharField(max_length=200,null=True)
	political_history = models.CharField(max_length=6500,null=True)
	delete_status = models.CharField(max_length=100, null=True,choices=DELETE_STATUS)
	constituency_update_date = models.DateTimeField(auto_now_add=True,null=True)
	def __str__(self):
		return self.constituency_name

	class Meta:
		verbose_name_plural = "Constituency"


class Country(models.Model):
	country_name = models.CharField(max_length=50,null=True)
	country_polling_stations = models.IntegerField(null=True)
	country_female_voters = models.IntegerField(null=True)
	country_male_voters = models.IntegerField(null=True)
	country_create_date = models.DateTimeField(auto_now_add=True,null=True)
	country_popn = models.IntegerField(null=True)
	country_languages = models.CharField(max_length=500,null=True, blank=True)
	country_political_history = models.CharField(max_length=1000,null=True, blank=True)
	country_update_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)


	def __str__(self):
		return self.country_name
	class Meta:
		verbose_name_plural = "Country"

class Department(models.Model):
	department_name = models.CharField(max_length=500,null=True, blank=True)
	dept_create_date = models.DateTimeField(auto_now_add=True,null=True)
	dept_update_date = models.DateTimeField(null=True,blank=True)

	def __str__(self):
		return self.department_name


class Electoral_positions(models.Model):
	position_name = models.CharField(max_length=100,null=True)
	position_create_date = models.DateTimeField(auto_now_add=True,null=True)
	position_update_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.position_name
	class Meta:
		verbose_name_plural = "Electoral Position"

class Groups(models.Model):
	STATUS = (
			('ACTIVE','ACTIVE'),
			('NOT ACTIVE','NOT ACTIVE')
		)
	groupName = models.CharField(max_length=100,null=True)
	status = models.CharField(max_length=50,null=True,choices=STATUS)

	def __str__(self):
		return self.groupName

	class Meta:
		verbose_name_plural = "Groups"


class Parties(models.Model):
	party_name = models.CharField(max_length=300,null=True,blank=True)
	party_create_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
	party_update_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)

	def __str__(self):
		return str(self.party_name)

	class Meta:
		verbose_name_plural = "Parties"

class Permissions(models.Model):
	moduleName = models.CharField(max_length=100,null=True)
	fileName = models.CharField(max_length=100,null=True)
	createdAt = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.moduleName
	class Meta:
		verbose_name_plural = "Permissions"

class Permissions_map(models.Model):
	createdData = models.DateTimeField(auto_now_add=True,null=True)
	updateData = models.CharField(max_length=100,null=True)
	deleteData = models.CharField(max_length=100,null=True)
	viewData = models.CharField(max_length=100,null=True)
	dateMapped = models.DateTimeField(null=True)

	# def __str__(self):
	# 	return str(self.createdData)

	class Meta:
		verbose_name_plural = "Permissions_map"

class Politician_activities(models.Model):
	activity_desc = models.CharField(max_length=500,null=True)

	def __str__(self):
		return self.activity_desc
	class Meta:
		verbose_name_plural = "Politician_activities"


class Politician_Category(models.Model):
	constituency = models.ForeignKey(Constituency_category,null=True,blank=True,on_delete=models.SET_NULL)
	categoryName = models.CharField(max_length=100,null=True)
	def __str__(self):
		return self.categoryName

	class Meta:
		verbose_name_plural = "Politician_Category"
class category(models.Model):
	categoryName = models.CharField(max_length=500, null=True)

	def __str__(self):
		return self.categoryName


class Politician_education(models.Model):
	school_name = models.CharField(max_length=100,null=True)
	certificate_name = models.CharField(max_length=100,null=True)
	date_from = models.DateTimeField(null=True)
	date_to = models.DateTimeField(null=True)


	def __str__(self):
		return self.school_name
	class Meta:
		verbose_name_plural = "Politician_education"



class Regions(models.Model):
	region_name = models.CharField(max_length=100,null=True)
	region_polling_stations = models.IntegerField(null=True)
	region_female_voters = models.IntegerField(null=True)
	region_male_voters = models.IntegerField(null=True)
	region_create_date = models.DateTimeField(null=True)

	def __str__(self):
		return self.region_name
	class Meta:
		verbose_name_plural = "Regions"


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Politicians(models.Model):  
	category = models.ForeignKey(Politician_Category,null=True,blank=True,on_delete=models.SET_NULL)
	region = models.ForeignKey(Regions,null=True,blank=True,on_delete=models.SET_NULL)
	education = models.ForeignKey(Politician_education,null=True,blank=True,on_delete=models.SET_NULL)
	party = models.ForeignKey(Parties,null=True,blank=True,on_delete=models.SET_NULL)
	activities = models.ForeignKey(Politician_activities,null=True,blank=True,on_delete=models.SET_NULL)
	country = models.ForeignKey(Country,null=True,blank=True,on_delete=models.SET_NULL)
	constituency = models.ForeignKey(Constituency,null=True,blank=True,on_delete=models.SET_NULL)
	electoral_positions = models.ForeignKey(Electoral_positions,null=True,blank=True,on_delete=models.SET_NULL)

	STATUS = (
			('INCUMBENT','INCUMBENT'),
			('FIRST TIME CONTESTANT','FIRST TIME CONTESTANT'),
			('CONTESTED BEFORE','CONTESTED BEFORE')
		)
	MARITAL_STATUS = (
		('MARRIED','MARRIED'),
		('SINGLE','SINGLE'),
		('DIVORCED','DIVORCED'),
	)
	politician_status = models.CharField(max_length=100,null=True,choices=STATUS)
	first_name = models.CharField(max_length=100,null=True)
	last_name = models.CharField(max_length=100,null=True)
	other_name = models.CharField(max_length=100,null=True)
	image = models.ImageField(null=True,blank=True)
	DOB = models.DateTimeField(null=True)
	marital_status = models.CharField(max_length=300,null=True,choices=MARITAL_STATUS)
	children = models.CharField(max_length=300,null=True,blank=True)

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
		
	

	

	def __str__(self):
		return self.first_name
	class Meta:
		verbose_name_plural = "Politician"


class Systemlogs(models.Model):
	userId = models.IntegerField(null=True)
	modelName = models.CharField(max_length=100,null=True)
	action = models.CharField(max_length=100,null=True)
	message = models.CharField(max_length=100,null=True)
	timeAccessed = models.DateTimeField(null=True)

	def __str__(self):
		return self.modelName
	class Meta:
		verbose_name_plural = "Systemlogs"
class User_permissions(models.Model):
	moduleName = models.CharField(max_length=50,null=True)
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
	#userId = models.IntegerField(null=True)
	#groupId = models.IntegerField(null=True)
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
	username = models.CharField(max_length=50,null=True)
	password = password = models.CharField(max_length=50)
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
	#userId = models.IntegerField(null=True)
	hash = models.CharField(max_length=200,null=True)

	def __str__(self):
		return str(self.userId)
	class Meta:
		verbose_name_plural = "Users_session"


