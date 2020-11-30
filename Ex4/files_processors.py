from xml.dom import minidom
import json
import argparse
import os.path


class Parser:
    '''Class for arguments parsing and validation'''

    def __init__(self):
        self.parser = self.create_parser()

    def file_choice(self, extention, fname):
        ext = os.path.splitext(fname)[1][1:]
        if ext != extention:
            self.parser.error("File extention not {}".format(extention))
        return fname

    def extention_choice(self, ext):
        if ext != 'xml' and ext != 'json':
            self.parser.error("File extention not xml or json")
        return ext

    def create_parser(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-s', '--students', required=True, type=lambda s: self.file_choice(('json'), s))
        parser.add_argument('-r', '--rooms', required=True, type=lambda s: self.file_choice(('json'), s))
        parser.add_argument('-f', '--format', required=True, type=lambda s: self.extention_choice(s))

        return parser


class JsonLoader:
    '''Class for json files loading'''

    def __init__(self, filename):
        self.filename = filename

    def loadfile(self):
        with open(self.filename, 'r') as readfile:
            return json.load(readfile)


class FileUploader():
    '''Base class for file uploading'''

    def __init__(self, data, filename):
        self.data = data
        self.filename = filename


class JsonUploader(FileUploader):
    '''Class for json file uploading'''

    def create_file(self):
        with open(self.filename, 'w') as upload_file:
            json.dump(self.data, upload_file, indent=4, sort_keys=True)


class XmlUploader(FileUploader):
    '''Class for xml file uploading'''

    def create_doc_tuple(self):
        doc = minidom.Document()
        root = doc.createElement('root')
        doc.appendChild(root)
        for room in self.data:
            room_el = doc.createElement('room')
            room_number_el = doc.createElement('room_number')
            text = doc.createTextNode(str(room[0]))
            room_number_el.appendChild(text)
            room_el.appendChild(room_number_el)
            root.appendChild(room_el)
        return doc

    def create_doc_list(self):
        doc = minidom.Document()
        root = doc.createElement('root')
        doc.appendChild(root)
        for room in self.data:
            room_el = doc.createElement('room')

            room_number_el = doc.createElement('room_number')
            text = doc.createTextNode(room['room'])
            room_number_el.appendChild(text)
            room_el.appendChild(room_number_el)

            students_number_el = doc.createElement('students_number')
            text = doc.createTextNode(str(room['students']))
            students_number_el.appendChild(text)
            room_el.appendChild(students_number_el)

            root.appendChild(room_el)

        return doc

    def create_file(self):
        doc = ''
        if isinstance(self.data, tuple):
            doc = self.create_doc_tuple()
        if isinstance(self.data, list):
            doc = self.create_doc_list()

        xml_str = doc.toprettyxml(indent='    ')
        with open(self.filename, 'w') as rooms_students_file:
            rooms_students_file.write(xml_str)
