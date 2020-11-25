from modules import LoadJson, RoomsForStudents, UploadJson, UploadXml
import sys
import argparse
import os.path

def file_choice(extention, fname):
    ext = os.path.splitext(fname)[1][1:]
    if ext != extention:
       parser.error("File extention not {}".format(extention))
    return fname

def extention_choice(ext):
    if ext != 'xml' and ext != 'json':
         parser.error("File extention not xml or json")
    return ext

def create_parser(): 
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--students', required=True, type=lambda s:file_choice(('json'),s))
    parser.add_argument('-r', '--rooms', required=True, type=lambda s:file_choice(('json'),s))
    parser.add_argument('-f', '--format', required=True, type=lambda s:extention_choice(s))

    return parser




if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    students = LoadJson(namespace.students).loadfile()
    rooms = LoadJson(namespace.rooms).loadfile()

    rooms_students = RoomsForStudents(rooms, students).create_list()

    if namespace.format == 'json':
        UploadJson(rooms_students).create_file('rooms_students.json')
    elif namespace.format == 'xml':
        UploadXml(rooms_students).create_file('rooms_students.xml')


# Command example: python main.py -s students.json -r rooms.json -f json      