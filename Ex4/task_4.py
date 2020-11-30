import sys
from db_queries import DbConnector, QueryExecuter, QueriesExecuter, DataFetcher
from files_processors import XmlUploader, JsonUploader, JsonLoader, Parser


def get_in_db(connection):
    QueryExecuter(connection, 'CREATE DATABASE IF NOT EXISTS rooms_students').execute_query()
    QueryExecuter(connection, 'USE rooms_students').execute_query()


def create_indexes():
    sex_index = 'ALTER TABLE students ADD INDEX (sex(1))'
    QueryExecuter(connection, sex_index).execute_query()
    birthday_index = 'ALTER TABLE students ADD INDEX (birthday)'
    QueryExecuter(connection, birthday_index).execute_query()


def fill_students(connection, filename):
    students = JsonLoader(filename).loadfile()
    student_list = [(student['birthday'], student['id'], student['name'], student['room'], student['sex']) for student in students]
    create_students_values = """INSERT IGNORE INTO `students` (`birthday`,`id`, `name`, `room`, `sex`) VALUES (%s, %s, %s, %s, %s)"""
    QueriesExecuter(connection, create_students_values).execute_queries(student_list)


def fill_rooms(connection, filename):
    rooms = JsonLoader(filename).loadfile()
    room_list = [(room['id'], room['name']) for room in rooms]
    create_rooms_values = """INSERT IGNORE INTO `rooms` (`id`,`room`) VALUES (%s, %s)"""
    QueriesExecuter(connection, create_rooms_values).execute_queries(room_list)


def create_all_json_files(student_count, min_age, age_diffecrence, different_sex):
    JsonUploader(student_count, 'json_files/student_count.json').create_file()
    JsonUploader(min_age, 'json_files/min_avg_age.json').create_file()
    JsonUploader(age_diffecrence, 'json_files/max_age_difference.json').create_file()
    JsonUploader(different_sex, 'json_files/different_sex.json').create_file()


def create_all_xml_files(student_count, min_age, age_diffecrence, different_sex):
    XmlUploader(student_count, 'xml_files/student_count.xml').create_file()
    XmlUploader(min_age, 'xml_files/min_avg_age.xml').create_file()
    XmlUploader(age_diffecrence, 'xml_files/max_age_difference.xml').create_file()
    XmlUploader(different_sex, 'xml_files/different_sex.xml').create_file()


if __name__ == "__main__":

    parser = Parser().create_parser()
    namespace = vars(parser.parse_args(sys.argv[1:]))
    files_types = {'json': create_all_json_files, 'xml': create_all_xml_files}

    connection = DbConnector("localhost", "masha", "").create_connection()
    get_in_db(connection)

    create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        birthday DATETIME,
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        room INTEGER,
        sex TEXT
    )ENGINE=InnoDB AUTO_INCREMENT=0
    """
    QueryExecuter(connection, create_students_table).execute_query()
    fill_students(connection, namespace['students'])

    create_rooms_table = """
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        room TEXT NOT NULL
    )ENGINE=InnoDB AUTO_INCREMENT=0
    """
    QueryExecuter(connection, create_rooms_table).execute_query()
    fill_rooms(connection, namespace['rooms'])

    create_indexes()

    student_count_query = '''
        SELECT rooms.room, COUNT(*)
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY rooms.id
    '''

    student_count_primary = DataFetcher(connection, student_count_query).fetch_data()
    student_count = [{'room': s[0], 'students': s[1]} for s in student_count_primary]

    min_age_query = '''
        SELECT rooms.room
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY AVG(students.birthday) DESC
        LIMIT 5
    '''
    min_age = DataFetcher(connection, min_age_query).fetch_data()

    age_diffecrence_query = '''
        SELECT rooms.room
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY DATEDIFF(MAX(students.birthday),MIN(students.birthday)) DESC
        LIMIT 5
    '''
    age_diffecrence = DataFetcher(connection, age_diffecrence_query).fetch_data()

    different_sex_query = '''
        SELECT rooms.room FROM rooms
        WHERE rooms.id IN (
            SELECT rooms.id FROM rooms, students
            WHERE rooms.id = students.room AND students.sex = 'M'
            GROUP BY rooms.id
            )
        AND rooms.id IN (
            SELECT rooms.id
            FROM rooms, students
            WHERE rooms.id = students.room
            AND students.sex = 'F'
            GROUP BY rooms.id
            )
        GROUP BY rooms.room
        ORDER BY rooms.id
    '''
    different_sex = DataFetcher(connection, different_sex_query).fetch_data()

    files_types[namespace['format']](student_count, min_age, age_diffecrence, different_sex)

    connection.close()

# Command example: python task_4.py -s students.json -r rooms.json -f json
