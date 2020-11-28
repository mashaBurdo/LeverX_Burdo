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
    files_types = {'json': JsonUploader, 'xml': XmlUploader}

    students = JsonLoader(namespace['students']).loadfile()
    rooms = JsonLoader(namespace['rooms']).loadfile()
    rooms_students = RoomsProcesser(rooms, students).create_list()

    files_types[namespace['format']](rooms_students).create_file()


# Command example: python main.py -s students.json -r rooms.json -f json
