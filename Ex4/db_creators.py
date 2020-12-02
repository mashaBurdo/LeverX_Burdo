from db_queries_executors import QueryExecuter
from files_processors import JsonLoader


def get_in_db(connection):
    QueryExecuter(connection, 'CREATE DATABASE IF NOT EXISTS rooms_students').execute_query()
    QueryExecuter(connection, 'USE rooms_students').execute_query()


def create_indexes(connection):
    sex_index = 'ALTER TABLE students ADD INDEX (sex(1))'
    QueryExecuter(connection, sex_index).execute_query()
    birthday_index = 'ALTER TABLE students ADD INDEX (birthday)'
    QueryExecuter(connection, birthday_index).execute_query()


def fill_students(connection, filename):
    students = JsonLoader(filename).loadfile()
    student_list = [(student['birthday'], student['id'], student['name'], student['room'], student['sex']) for student in students]
    create_students_values = """INSERT IGNORE INTO `students` (`birthday`,`id`, `name`, `room`, `sex`) VALUES (%s, %s, %s, %s, %s)"""
    QueryExecuter(connection, create_students_values, student_list).execute_query()


def fill_rooms(connection, filename):
    rooms = JsonLoader(filename).loadfile()
    room_list = [(room['id'], room['name']) for room in rooms]
    create_rooms_values = """INSERT IGNORE INTO `rooms` (`id`,`room`) VALUES (%s, %s)"""
    QueryExecuter(connection, create_rooms_values, room_list).execute_query()
