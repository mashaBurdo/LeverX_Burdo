import json
import pymysql
from pymysql.cursors import DictCursor
from xml.dom import minidom

class JsonLoader:
    '''Class for json files loading'''

    def __init__(self, filename):
        self.filename = filename

    def loadfile(self):
        with open(self.filename, 'r') as readfile:
            return json.load(readfile)

#rooms = JsonLoader('rooms.json').loadfile()
#students = JsonLoader('students.json').loadfile()
#sprint(students)

connection = pymysql.connect(
    host='localhost', 
    user='masha', 
    password='SQfavorit007'
)

print('Connected')

with connection.cursor() as cursor:

    sql = 'CREATE DATABASE IF NOT EXISTS rooms_students'
    cursor.execute(sql)


connection.close()