from files_processors import JsonLoader, RoomsProcesser, JsonUploader, XmlUploader
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
    parser.add_argument('-s', '--students', required=True, type=lambda s: file_choice(('json'), s))
    parser.add_argument('-r', '--rooms', required=True, type=lambda s: file_choice(('json'), s))
    parser.add_argument('-f', '--format', required=True, type=lambda s: extention_choice(s))

    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = vars(parser.parse_args(sys.argv[1:]))
    
    students = JsonLoader(namespace['students']).loadfile()
    rooms = JsonLoader(namespace['rooms']).loadfile()

    rooms_students = RoomsProcesser(rooms, students).create_list()

    if namespace['format'] == 'json':
        JsonUploader(rooms_students).create_json('rooms_students.json')
    elif namespace['format'] == 'xml':
        XmlUploader(rooms_students).create_xml('rooms_students.xml')


# Command example: python main.py -s students.json -r rooms.json -f json
