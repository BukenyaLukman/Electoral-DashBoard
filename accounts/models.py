from django.db import models

# Create your models here.
class Constituency(models.Model):
	constituency_id = models.IntegerField(max_length=100,null=True)
	region_id = models.IntegerField(max_length=100,null=True)
	constituency_name = models.CharField(max_length=200,null=True)
	constituency_polling_stations = models.IntegerField(max_length=100,null=True)
	constituency_female_voters = models.IntegerField(max_length=100,null=True)
	constituency_male_voters = models.IntegerField(max_length=100,null=True)
	constituency_create_date = models.DateTimeField(null=True)
	constituency_popn = models.IntegerField(max_length=100,null=True)
	languages = models.CharField(max_length=200,null=True)
	political_history = models.CharField(max_length=6500,null=True)
	category_id = models.IntegerField(max_length=100,null=True)

	def __str__(self):
		return self.constituency_name

class Constituency_category(models.Model):
	category_id = models.IntegerField(max_length=100,null=True)
	cons_category_name = models.IntegerField(max_length=100,null=True)

	def __str__(self):
		return self.cons_category_name


class Country(models.Model):
	country_id = models.IntegerField(max_length=50,null=True)
	country_name = models.CharField(max_length=50,null=True)
	country_polling_stations = models.IntegerField(max_length=50,null=True)
	country_female_voters = models.IntegerField(max_length=50,null=True)
	country_male_voters = models.IntegerField(max_length=50, null=True)
	country_add_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.country_name

class Electoral_positions(models.Model):
	position_id = models.IntegerField(max_length=40,null=True)
	position_name = models.CharField(max_length=100,null=True)
	position_create_date = models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.position_name

class Groups(models.Model):
	STATUS = (
			('',''),
			('','')
		)
	groupId = models.IntegerField(max_length=50,null=True)
	groupName = models.CharField(max_length=100,null=True)
	status = models.CharField(max_length=50,null=True,choices=STATUS)


class Parties(models.Model):
	part_id = models.IntegerField(max_length=50,null=True)
	party_name = models.CharField(max_length=100,null=True)
	party_create_date = models.DateTimeField(max_length=50,null=True)


	def __str__(self):
		return self.party_name

class Permissions(models.Model):
	permissionId = models.IntegerField(max_length=20,null=True)
	moduleName = models.CharField(max_length=100,null=True)
	fileName = models.CharField(max_length=100,null=True)
	createdAt = models.DateTimeField(auto_now_add=True,null=True)