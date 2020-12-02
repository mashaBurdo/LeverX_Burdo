create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
        birthday DATETIME,
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        room INTEGER,
        sex TEXT
    )ENGINE=InnoDB AUTO_INCREMENT=0
    """
create_rooms_table = """
    CREATE TABLE IF NOT EXISTS rooms (
        id INTEGER PRIMARY KEY,
        room TEXT NOT NULL
    )ENGINE=InnoDB AUTO_INCREMENT=0
    """
student_count_query = '''
        SELECT rooms.room, COUNT(*)
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY rooms.id
    '''
min_age_query = '''
        SELECT rooms.room
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY AVG(students.birthday) DESC
        LIMIT 5
    '''
age_diffecrence_query = '''
        SELECT rooms.room
        FROM rooms, students
        WHERE rooms.id = students.room
        GROUP BY rooms.room
        ORDER BY DATEDIFF(MAX(students.birthday),MIN(students.birthday)) DESC
        LIMIT 5
    '''

different_sex_query = '''
        SELECT DISTINCT rooms.room
        FROM  rooms
        JOIN students ON rooms.id=students.room
        GROUP BY rooms.id
        HAVING COUNT(DISTINCT students.sex)=1
        ORDER BY rooms.id
    '''
fetch_queries = [('rooms_student_count', student_count_query, True), 
                ('top_5_rooms_min_avg_age', min_age_query, False),
                ('top_5_rooms_max_age_diff', age_diffecrence_query, False),
                ('rooms_different_sex', different_sex_query, False)]
