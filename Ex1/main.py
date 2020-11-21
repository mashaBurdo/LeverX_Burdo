from modules import LoadJson, RoomsForStudents, UploadJson, UploadXml

rooms = LoadJson('rooms.json').loadfile()
students = LoadJson('students.json').loadfile()

rooms_students = RoomsForStudents(rooms, students).create_list()

UploadJson(rooms_students).create_file('rooms_students.json')
UploadXml(rooms_students).create_file('rooms_students.xml')
