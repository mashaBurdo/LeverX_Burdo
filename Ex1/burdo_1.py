'''import json
import xml.etree.ElementTree as xml

rooms = []
students = []
rooms_students = []

with open('rooms.json', 'r') as rooms_file, open('students.json', 'r') as students_file:
    rooms = json.load(rooms_file)
    students = json.load(students_file)

for room in rooms:
    room_student = {room['id'] : []}
    for student in students:
        if student['room'] == room['id']:
            room_student[room['id']].append(student['name'])
    rooms_students.append(room_student)

def create_json(rooms_students):
    with open('rooms_students.json', 'w') as rooms_students_file:
        json.dump(rooms_students, rooms_students_file, indent=4, sort_keys=True)

def create_xml(rooms_students):
    root_el = xml.Element('root')

    for room in rooms_students:
        room_el = xml.SubElement(root_el, 'room '+str(*room.keys()))
        students = list(room.values())[0]
        for student in students:
            student_el = xml.SubElement(room_el, 'student')
            student_el.text = student
    
    tree = xml.ElementTree(root_el)
    with open('rooms_students.xml', 'wb') as rooms_students_file:
        tree.write(rooms_students_file)

create_xml(rooms_students)

'''

name = input("Whats your nane: ")
print(name*5)