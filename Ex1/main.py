from modules import LoadJson, RoomsForStudents, UploadJson, UploadXml
import sys
import argparse

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students')
    parser.add_argument('-r', '--rooms')
    parser.add_argument('-f', '--format')

    return parser


if __name__ == "__main__":
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])

    students = LoadJson(namespace.students).loadfile()
    rooms = LoadJson(namespace.rooms).loadfile()

    rooms_students = RoomsForStudents(rooms, students).create_list()

    if namespace.format == 'json':
        UploadJson(rooms_students).create_file('rooms_students.json')
    elif namespace.format == 'xml':
        UploadXml(rooms_students).create_file('rooms_students.xml')
    else:
        print('Wrong format!')

# Command example: python main.py -s students.json -r rooms.json -f json      