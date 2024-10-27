from operator import itemgetter

class Language:
    """Язык программирования"""
    def __init__(self, id, name, popularity, library_id):
        self.id = id
        self.name = name
        self.popularity = popularity
        self.library_id = library_id


class Library:
    """Библиотека"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibraryLanguage:
    """
    'Языки библиотек' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, library_id, language_id):
        self.library_id = library_id
        self.language_id = language_id


# Библиотеки
libraries = [
    Library(1, 'Аллергики'),
    Library(2, 'Квадроберы'),
    Library(3, 'Арахнофобы'),
]

# Языки программирования
languages = [
    Language(1, 'Python', 100, 1),
    Language(2, 'Nim', 85, 1),
    Language(3, 'JavaScript', 90, 2),
    Language(4, 'C++', 75, 2),
    Language(5, 'Rust', 80, 3),
    Language(6, 'Assembler', 79, 3),
]

# Связь многие-ко-многим
libraries_languages = [
    LibraryLanguage(1, 1),
    LibraryLanguage(1, 2),
    LibraryLanguage(2, 3),
    LibraryLanguage(2, 4),
    LibraryLanguage(3, 5),
    LibraryLanguage(3, 6),
]

def main():
    # Соединение данных один-ко-многим
    one_to_many = []
    for l in libraries:
        for lang in languages:
            if lang.library_id == l.id:
                one_to_many.append((lang.name, lang.popularity, l.name))

    # Соединение данных многие-ко-многим
    many_to_many_temp = []
    for l in libraries:
        for ll in libraries_languages:
            if l.id == ll.library_id:
                many_to_many_temp.append((l.name, ll.library_id, ll.language_id))

    many_to_many = []
    for library_name, library_id, language_id in many_to_many_temp:
        for lang in languages:
            if lang.id == language_id:
                many_to_many.append((lang.name, lang.popularity, library_name))

    # Задание Г1: Библиотеки, названия которых начинаются с "А", и их языки
    print("Задание Г1")
    g1 = []
    for l in libraries:
        if l.name.startswith("А"):
            languages_list = []
            for lang in one_to_many:
                if lang[2] == l.name:
                    languages_list.append(lang[0])  
            g1.append((l.name, languages_list))
    
    for library, languages_list in g1:
        print(library, ": ", ", ".join(languages_list) if languages_list else "Языков нет")

    # Задание Г2: Библиотеки с максимальной популярностью языков, отсортировано по популярности
    print("\nЗадание Г2")
    g2 = []
    for l in libraries:
        language_popularity = []
        for lang in languages:
            if lang.library_id == l.id:
                language_popularity.append(lang.popularity)
        
        if language_popularity:
            max_popularity = max(language_popularity)
            g2.append((l.name, max_popularity))
    
    g2 = sorted(g2, key = lambda x : x[1], reverse = True)
    
    for library, max_popularity in g2:
        print(library, ": ", max_popularity)

    # Задание Г3: Все библиотеки и их языки, сортировка по библиотекам
    print("\nЗадание Г3")
    g3 = {}
    for l in libraries:
        library_languages = []
        for lang in many_to_many:
            if lang[2] == l.name:
                library_languages.append(lang[0])  
        g3[l.name] = library_languages
    
    for library, languages_list in g3.items():
        print(library, ": ", ", ".join(languages_list) if languages_list else "Языков нет")

if __name__ == "__main__":
    main()
