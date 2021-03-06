import json
from xml.dom import minidom


class JsonLoader:
    '''Class for json files loading'''

    def __init__(self, filename):
        self.filename = filename

    def loadfile(self):
        with open(self.filename, 'r') as readfile:
            return json.load(readfile)


class RoomsProcesser:
    '''Class for creating a list of rooms where each room contains a list of students who are in this room '''

    def __init__(self, rooms, students):
        self.rooms = rooms
        self.students = students

    def create_list(self):
        rooms_students = []
        for room in self.rooms:
            room_student = {room['id']: []}
            rooms_students.append(room_student)
        for student in self.students:
            rooms_students[student['room']][student['room']].append(student['name'])
        return rooms_students


class FileUploader():
    '''Base class for file uploading'''

    def __init__(self, rooms_students):
        self.rooms_students = rooms_students


class JsonUploader(FileUploader):
    '''Class for json file uploading'''

    def create_file(self):
        with open('rooms_students.json', 'w') as rooms_students_file:
            json.dump(self.rooms_students, rooms_students_file, indent=4, sort_keys=True)


class XmlUploader(FileUploader):
    '''Class for xml file uploading'''

    def create_file(self):
        doc = minidom.Document()
        root = doc.createElement('root')
        doc.appendChild(root)

        for room in self.rooms_students:
            room_el = doc.createElement('room')
            room_number_el = doc.createElement('room_number')
            text = doc.createTextNode('room # '+str(*room.keys()))
            room_number_el.appendChild(text)
            room_el.appendChild(room_number_el)
            students = list(room.values())[0]

            stud_count = 0
            for student in students:
                stud_count += 1
                student_el = doc.createElement('student'+str(stud_count))
                text = doc.createTextNode(student)
                student_el.appendChild(text)
                room_el.appendChild(student_el)

            root.appendChild(room_el)

        xml_str = doc.toprettyxml(indent='    ')
        with open('rooms_students.xml', 'w') as rooms_students_file:
            rooms_students_file.write(xml_str)
