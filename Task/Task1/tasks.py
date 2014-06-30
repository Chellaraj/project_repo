from __future__ import absolute_import

from Task1.celery import app
import MySQLdb
import csv
import settings
import urllib

@app.task
def getting_data_from_mysql( table_name ):
	#open database connection
	db = MySQLdb.connect ( settings.Mysql_Url,settings.Username,settings.Password,settings.Database )

	#prepare cursor object using cursor() method
	cursor = db.cursor()
	
	#preapre the query to get form the tabe .

	sql = "SELECT * FROM %s" % table_name

	try:
   	   # Execute the SQL command
   	   cursor.execute(sql)
   	   # Fetch all the rows in a list of lists.
           results = cursor.fetchall()
           csv_out = open("%s.csv" % table_name,'wb')
           mywriter = csv.writer(csv_out)
           mywriter.writerows(results)  
           csv_out.close()  
           
      
        except (MySQLdb.OperationalError, MySQLdb.ProgrammingError), e:
    	   return str(e)
    	
	   #disconnected from server
	finally:
           db.close ( )
        return 1
