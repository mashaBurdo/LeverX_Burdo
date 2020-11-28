class Version:
    '''Class for lexicographical version comparison. Versions are represented as tuples. Leading zeros problem is solved. '''
    def __init__(self, version):
        self.str_version = self.to_no_int_tuple(version)
        self.version = self.to_tuple(version)

    def to_tuple(self, version):
        while version[len(version)-2:] == '.0':
            version = version[:len(version)-2]
        version = version.split('.')
        new_version = []
        for i in version:
            try:
                i = int(i)
                new_version.append(i)
            except ValueError:
                new_version.append(i)
        return tuple(new_version)

    def to_no_int_tuple(self, version):
        while version[len(version)-2:] == '.0':
            version = version[:len(version)-2]
        version = version.split('.')
        return tuple(version)

    def _cmp(self, other):
        try:
            if self.version == other.version:
                return 0
            if self.version < other.version:
                return -1
            if self.version > other.version:
                return 1
        except TypeError:
            if self.str_version == other.str_version:
                return 0
            if self.str_version < other.str_version:
                return -1
            if self.str_version > other.str_version:
                return 1

    def __gt__(self, other):
        c = self._cmp(other)
        return c > 0

    def __eq__(self, other):
        c = self._cmp(other)
        return c == 0

    def __ge__(self, other):
        c = self._cmp(other)
        return c >= 0


def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0")

    ]

    for version_1, version_2 in to_test:

        # print(Version(version_1).version, Version(version_2).version)
<<<<<<< HEAD
        # print(f"{version_1} < {version_2}",Version(version_1) < Version(version_2))
=======
<<<<<<< HEAD
        # print(f"{version_1} < {version_2}",Version(version_1) < Version(version_2))
=======
        # print(f"{version_1} and {version_2}", "<")
        # print(Version(version_1) < Version(version_2))
>>>>>>> b57a419 (ready for check)
>>>>>>> b26ea79b296ec76d0877121905e9995eec28aa05
        assert Version(version_1) < Version(version_2), "le failed"
        assert Version(version_2) > Version(version_1), "ge failed"
        assert Version(version_2) != Version(version_1), "neq failed"


if __name__ == "__main__":
    main()

''' Command examples:
>>> from task_2 import Version
>>> Version('1.1.3') < Version('2.2.3')
True
>>> Version('1.3.0') > Version('0.3.0')
True
>>> Version('0.3.0b') < Version('1.2.42')
True
>>> Version('1.3.42') == Version('42.3.1')
False
>>> Version('1.3.42') >= Version('00042.3.1')
False
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> b26ea79b296ec76d0877121905e9995eec28aa05
>>> Version('1.0.0-rc.1') > Version('1.0')
True
>>> Version('1.0.0-rc.1') == Version('1.0')
False
>>> Version('000000000000000001.0') == Version('1.0')
True
>>> Version('1.0.0-rc.1') >  Version('1.0.0')
True
>>> Version('1.0.0') !=  Version('1')
False
<<<<<<< HEAD
=======
=======
>>>>>>> b57a419 (ready for check)
>>>>>>> b26ea79b296ec76d0877121905e9995eec28aa05
'''
