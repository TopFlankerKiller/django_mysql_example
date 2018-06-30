from django.db import models


class user(models.Model):
	'''This class simulates a user with an id and a name as attributes'''
	user_id=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=40)

	

class occupations(models.Model):
	'''This class simulates an occupation with an id and the name of occupation as attributes'''
	occup_id=models.IntegerField(primary_key=True)
	occupation=models.CharField(max_length=40)


class userhasoccupations(models.Model):
	'''This class simulates the connection between a user and an occupation. User id and occupation id are used as foreign keys to the database schema'''
	connection_id=models.IntegerField(primary_key=True)
	user_id=models.ForeignKey(user,db_column='user_id',on_delete=models.CASCADE)
	occup_id=models.ForeignKey(occupations,db_column='occup_id',on_delete=models.CASCADE)
