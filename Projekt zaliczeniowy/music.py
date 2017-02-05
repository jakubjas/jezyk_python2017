# -*- coding: utf-8 -*-

import sqlite3
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


class DatabaseLayer:

    def __init__(self, database='music.db'):
        self.database = database

    def query(self, statements, data=()):
        with sqlite3.connect(self.database) as connection:
            connection.text_factory = lambda x: unicode(x, "utf-8", "ignore")
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            result = cursor.execute(statements, data)
            connection.commit()

        return result


class UserInterface:

    def __init__(self): pass

    def main_menu(self): pass

    def database_menu(self): pass

    def add_album_menu(self): pass

    def delete_album_menu(self): pass

    def search_menu(self): pass

    def print_menu(self): pass


class AlbumPrinter:

    def __init__(self): pass

    @classmethod
    def print_albums(cls, data):

        data = list(data)

        if not data:
            print "Database is empty"
            return

        header = ["Artist", "Album name", "Release year"]
        widths = [len(header[0]), len(header[1]), len(header[2])]
        max_values = []

        max_values.append(max([len(row['Artist']) for row in data]))
        max_values.append(max([len(row['AlbumName']) for row in data]))
        max_values.append(max([len(str(row['ReleaseYear'])) for row in data]))

        for i in range(3):
            if max_values[i] > widths[i]:
                widths[i] = max_values[i]

        separator = "+"
        row_format = "|"

        for width in widths:
            row_format += " %-" + "%ss |" % (width,)
            separator += "-" * width + "--+"

        print separator
        print (row_format % (header[0], header[1], header[2]))
        print separator

        for row in data:
            print (row_format % (row["Artist"], row["AlbumName"], row["ReleaseYear"]))

        print separator


class AlbumManager:

    def __init__(self, database='music.db'):
        self.database = DatabaseLayer(database)
        self.database.query("CREATE TABLE IF NOT EXISTS Collection(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Artist TEXT NOT NULL, AlbumName TEXT NOT NULL, ReleaseYear INTEGER NOT NULL)")

    def reset(self):
        self.database.query("DELETE FROM Collection")

    def add_album(self, artist, album_name, release_year):
        self.database.query("INSERT INTO Collection (Artist, AlbumName, ReleaseYear) VALUES (?, ?, ?)", (artist, album_name, release_year))

    def delete_album(self, artist, album_name, release_year):
        self.database.query("DELETE FROM Collection WHERE Artist=? AND AlbumName=? AND ReleaseYear=?", (artist, album_name, release_year))

    def delete_all_by_artist(self, artist):
        self.database.query("DELETE FROM Collection WHERE Artist=?", (artist, ))

    def get_albums(self, key='Artist'):
        return self.database.query("SELECT Artist, AlbumName, ReleaseYear FROM Collection ORDER BY " + key)

    def get_by_artist(self, artist, key='ReleaseYear'):
        return self.database.query("SELECT Artist, AlbumName, ReleaseYear FROM Collection WHERE Artist=? ORDER BY " + key, (artist, ))

    def get_by_name(self, album_name, key='Artist'):
        return self.database.query("SELECT Artist, AlbumName, ReleaseYear FROM Collection WHERE AlbumName=? ORDER BY " + key, (album_name,))

    def get_by_year(self, release_year, key='Artist'):
        return self.database.query("SELECT Artist, AlbumName, ReleaseYear FROM Collection WHERE ReleaseYear=? ORDER BY " + key, (release_year,))


logo = r"""
       _    _ _                     ____  ____
      / \  | | |__  _   _ _ __ ___ |  _ \| __ )
     / _ \ | | '_ \| | | | '_ ` _ \| | | |  _ \
    / ___ \| | |_) | |_| | | | | | | |_| | |_) |
   /_/   \_\_|_.__/ \__,_|_| |_| |_|____/|____/
                                     version 1.0"""


print logo

separator = "+"
separator += "-" * 50
separator += "+"
print separator

actions = [
    "[1] Create a new database",
    "[2] Open existing database",
    "[3] Add album",
    "[4] Delete album",
    "[5] Search",
    "[6] Print collection",
    "[7] By release year",
    "[8] Delete all albums by...",
    "[9] Go back"
]

for action in actions:
    line = "| "
    line += action
    line += " " * (49-len(action))
    line += "|"
    print line

print separator

print

my_collection = AlbumManager()
AlbumPrinter.print_albums(my_collection.get_albums())

cls()
