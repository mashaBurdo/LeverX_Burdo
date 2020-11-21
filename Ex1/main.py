import json
import xml.etree.ElementTree as xml


class LoadJson:
    '''Class for json files loading'''

    def __init__(self, filename):
        self.filename = filename

    def loadfile(self):
        with open(self.filename, 'r') as readfile:
            return json.load(readfile)


class RoomsForStudents:
    '''Class for creating a list of rooms where each room contains a list of students who are in this room'''

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students = students

    def create_list(self):
        rooms_students = []
        for room in self.rooms:
            room_student = {room['id']: []}
            for student in self.students:
                if student['room'] == room['id']:
                    room_student[room['id']].append(student['name'])
            rooms_students.append(room_student)
        return rooms_students


class UploadJson:
    '''Class for json file uploading'''

    def __init__(self, rooms_students):
        self.rooms_students = rooms_students

    def create_file(self, filename):
        with open(filename, 'w') as rooms_students_file:
            json.dump(self.rooms_students, rooms_students_file, indent=4, sort_keys=True)


class UploadXml:
    '''Class for xml file uploading'''

    def __init__(self, rooms_students):
        self.rooms_students = rooms_students

    def create_file(self, filename):
        root_el = xml.Element('root')

        for room in self.rooms_students:
            room_el = xml.SubElement(root_el, 'room '+str(*room.keys()))
            students = list(room.values())[0]
            for student in students:
                student_el = xml.SubElement(room_el, 'student')
                student_el.text = student

        tree = xml.ElementTree(root_el)
        with open(filename, 'wb') as rooms_students_file:
            tree.write(rooms_students_file)


rooms = LoadJson('rooms.json').loadfile()
students = LoadJson('students.json').loadfile()

rooms_students = RoomsForStudents(rooms, students).create_list()

UploadJson(rooms_students).create_file('rooms_students.json')
UploadXml(rooms_students).create_file('rooms_students.xml')
