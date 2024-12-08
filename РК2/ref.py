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
    """Связь библиотек и языков (многие-ко-многим)"""
    def __init__(self, library_id, language_id):
        self.library_id = library_id
        self.language_id = language_id


def one_to_many(libraries, languages):
    """Соединение данных один-ко-многим"""
    return [
        (lang.name, lang.popularity, lib.name)
        for lib in libraries
        for lang in languages
        if lang.library_id == lib.id
    ]


def many_to_many(libraries, libraries_languages, languages):
    """Соединение данных многие-ко-многим"""
    many_to_many_temp = [
        (lib.name, ll.library_id, ll.language_id)
        for lib in libraries
        for ll in libraries_languages
        if lib.id == ll.library_id
    ]
    return [
        (lang.name, lang.popularity, library_name)
        for library_name, library_id, language_id in many_to_many_temp
        for lang in languages
        if lang.id == language_id
    ]


def task_g1(libraries, one_to_many_data):
    """Задание Г1"""
    return [
        (lib.name, [lang[0] for lang in one_to_many_data if lang[2] == lib.name])
        for lib in libraries if lib.name.startswith("А")
    ]


def task_g2(libraries, languages):
    """Задание Г2"""
    result = [
        (lib.name, max(lang.popularity for lang in languages if lang.library_id == lib.id))
        for lib in libraries if any(lang.library_id == lib.id for lang in languages)
    ]
    return sorted(result, key=lambda x: x[1], reverse=True)


def task_g3(libraries, many_to_many_data):
    """Задание Г3"""
    return {
        lib.name: [lang[0] for lang in many_to_many_data if lang[2] == lib.name]
        for lib in libraries
    }
