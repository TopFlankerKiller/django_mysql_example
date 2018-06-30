from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb


def get_user_has_occupation(request):

	'''This function connects to the MySQL database
	and fetches the data according to the query written from the user'''
	conn=MySQLdb.connect(host="localhost",user="root",passwd="",db="database1")
	cursor=conn.cursor()
	cursor.execute("select * from userhasoccupations")
	html=cursor.fetchall()

	# if cursor.rowcount==0:
	# 	html="<html><body>There are no connections to show.</body></html>"
	# else:
	# 	rows=cursor.fetchall()
	# 	for row in rows:

	# 		html="<html><body>The user %d is %d</body></html>"% (row[0], (row[1]))
			
	
	return HttpResponse(html)




