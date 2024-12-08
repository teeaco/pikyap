import unittest
from ref import Language, Library, LibraryLanguage, one_to_many, many_to_many, task_g1, task_g2, task_g3

class TestProgram(unittest.TestCase):

    def setUp(self):
        self.libraries = [
            Library(1, 'Аллергики'),
            Library(2, 'Квадроберы'),
            Library(3, 'Арахнофобы'),
        ]
        self.languages = [
            Language(1, 'Python', 100, 1),
            Language(2, 'Nim', 85, 1),
            Language(3, 'JavaScript', 90, 2),
            Language(4, 'C++', 75, 2),
            Language(5, 'Rust', 80, 3),
            Language(6, 'Assembler', 79, 3),
        ]
        self.libraries_languages = [
            LibraryLanguage(1, 1),
            LibraryLanguage(1, 2),
            LibraryLanguage(2, 3),
            LibraryLanguage(2, 4),
            LibraryLanguage(3, 5),
            LibraryLanguage(3, 6),
        ]

    def test_task_g1(self):
        one_to_many_data = one_to_many(self.libraries, self.languages)
        result = task_g1(self.libraries, one_to_many_data)
        self.assertEqual(result, [
            ('Аллергики', ['Python', 'Nim']),
            ('Арахнофобы', ['Rust', 'Assembler']),
        ])

    def test_task_g2(self):
        result = task_g2(self.libraries, self.languages)
        self.assertEqual(result, [
            ('Аллергики', 100),
            ('Квадроберы', 90),
            ('Арахнофобы', 80),
        ])

    def test_task_g3(self):
        many_to_many_data = many_to_many(self.libraries, self.libraries_languages, self.languages)
        result = task_g3(self.libraries, many_to_many_data)
        self.assertEqual(result, {
            'Аллергики': ['Python', 'Nim'],
            'Квадроберы': ['JavaScript', 'C++'],
            'Арахнофобы': ['Rust', 'Assembler'],
        })

if __name__ == "__main__":
    unittest.main()
