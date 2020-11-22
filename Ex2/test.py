'''Расширить реализацию класса Version (см. файл task_2.py), чтобы позволять использовать его для семантического сравнения.

Пример:

 Version('1.1.3') < Version('2.2.3')
True

 Version('1.3.0') > Version('0.3.0')
True

 Version('0.3.0b') < Version('1.2.42')
True

 Version('1.3.42') == Version('42.3.1')
False
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
'''
from distutils.version import LooseVersion
tup1 = ('1','1','0-alpha')
tup2 = ('1','2','0-alpha', '1')
print(type(LooseVersion("1.0.0")))