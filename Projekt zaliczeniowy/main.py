# -*- coding: utf-8 -*-

import os
import sqlite3
import math
from itertools import *


class ApplicationState:

    def __init__(self): pass

    album_manager = None


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


class MenuBase:
    
    def __init__(self):
        self.header = ""
        self.actions = []

    def get_action(self, action_id):
        action_id = int(action_id)
        action = list(ifilter(lambda a: a["id"] == action_id, self.actions))
        return action[0] if len(action) else None

    def print_menu(self):
        separator = "+" + "-" * 50 + "+"
        print separator

        category = "|"
        cat_spacer = 25 - int(math.ceil(float(len(self.header))/2))
        category += " " * cat_spacer
        category += self.header
        category += " " * cat_spacer

        if len(self.header) % 2:
            category += " |"
        else:
            category += "|"

        print category

        blank_line = "|" + 50 * " " + "|"

        print blank_line

        for action in self.actions:
            line = "| "
            action = "[" + str(action["id"]) + "] " + action["text"]
            line += action
            line += " " * (49 - len(action))
            line += "|"
            print line

        print separator

    @classmethod
    def print_action_header(cls, action_name):
        spacer = 25 - int(math.ceil(float(len(action_name))/2))

        header = "=" * spacer
        header += " " + action_name + " "
        header += "=" * spacer
        header += "\n"

        print header


class DatabaseMenu(MenuBase):

    def __init__(self):
        self.header = "DATABASE MENU"
        self.actions = [
            {
                "id": 1,
                "text": "Create database",
                "func": self.create_database
            },
            {
                "id": 2,
                "text": "Delete database",
                "func": self.delete_database
            },
            {
                "id": 3,
                "text": "Load database",
                "func": self.load_database
            }
        ]

    @classmethod
    def create_database(cls):
        name = raw_input("Specify database name (default: music.db): ") or "music.db"
        ApplicationState.album_manager = AlbumManager(name)
        return MainMenu

    @classmethod
    def delete_database(cls):

        files = []

        for f in os.listdir("."):
            if f.endswith(".db"):
                files.append(f)

        if not files:
            print "No database files found."

            raw_input("\nPress ENTER to go back to the previous menu... ")

            return DatabaseMenu

        else:
            print "Databases found: "

            for f in files:
                print(f)

            print

            name = raw_input("Specify database name (default: music.db - type 'exit' to abort): ") or "music.db"

            if name == 'exit':
                return DatabaseMenu
            elif not os.path.exists(name):
                print "The specified file does not exist.\n"
                return None

            os.remove(name)
            return DatabaseMenu

    @classmethod
    def load_database(cls):

        files = []

        for f in os.listdir("."):
            if f.endswith(".db"):
                files.append(f)

        if not files:
            print "No database files found."

            raw_input("\nPress ENTER to go back to the previous menu... ")

            return DatabaseMenu

        else:
            print "Databases found: "

            for f in files:
                print(f)

            print

            name = raw_input("Specify database name (default: music.db - type 'exit' to abort): ") or "music.db"

            if name == 'exit':
                return DatabaseMenu
            elif not os.path.exists(name):
                print "The specified file does not exist.\n"
                return None

            ApplicationState.album_manager = AlbumManager(name)

            return MainMenu


class MainMenu(MenuBase):

    def __init__(self):
        self.header = "MAIN MENU"

        self.actions = [
            {
                "id": 1,
                "text": "Add album",
                "func": self.add_album_menu
            },
            {
                "id": 2,
                "text": "Delete album",
                "func": self.delete_album_menu
            },
            {
                "id": 3,
                "text": "Search",
                "func": self.search_menu
            },
            {
                "id": 4,
                "text": "Print collection",
                "func": self.print_collection_menu
            },
            {
                "id": 5,
                "text": "Go back",
                "func": lambda: DatabaseMenu
            }
        ]

    @classmethod
    def add_album_menu(cls):

        while True:
            artist = raw_input("Artist: ")

            if artist:
                break

        while True:
            album_name = raw_input("Album name: ")

            if album_name:
                break

        while True:
            release_year = raw_input("Release year: ")

            if release_year.isdigit():
                break

        AlbumManager.add_album(ApplicationState.album_manager, artist, album_name, release_year)
        return MainMenu

    def delete_album_menu(self): pass

    @classmethod
    def print_collection_menu(cls):
        return PrintCollection

    def search_menu(self): pass


class DeleteAlbum(MenuBase):

    def __init__(self):
        self.header = "DELETE ALBUM"

        self.actions = [
            {
                "id": 1,
                "text": "Sorted by artist",
                "func": self.sorted_by_artist
            },
            {
                "id": 2,
                "text": "Sorted by album name",
                "func": self.sorted_by_album
            },
            {
                "id": 3,
                "text": "Sorted by release year",
                "func": self.sorted_by_year
            },
            {
                "id": 4,
                "text": "Go back",
                "func": lambda: MainMenu
            }
        ]


class PrintCollection(MenuBase):
    
    def __init__(self):
        self.header = "PRINT MENU"

        self.actions = [
            {
                "id": 1,
                "text": "Sorted by artist",
                "func": self.sorted_by_artist
            },
            {
                "id": 2,
                "text": "Sorted by album name",
                "func": self.sorted_by_album
            },
            {
                "id": 3,
                "text": "Sorted by release year",
                "func": self.sorted_by_year
            },
            {
                "id": 4,
                "text": "Go back",
                "func": lambda: MainMenu
            }
        ]

    @classmethod
    def sorted_by_artist(cls):
        AlbumPrinter.print_albums(AlbumManager.get_albums(ApplicationState.album_manager))
        raw_input("\nPress ENTER to go back to the previous menu... ")
        return PrintCollection

    @classmethod
    def sorted_by_album(cls):
        AlbumPrinter.print_albums(AlbumManager.get_albums(ApplicationState.album_manager, 'AlbumName'))
        raw_input("\nPress ENTER to go back to the previous menu... ")
        return PrintCollection

    @classmethod
    def sorted_by_year(cls):
        AlbumPrinter.print_albums(AlbumManager.get_albums(ApplicationState.album_manager, 'ReleaseYear'))
        raw_input("\nPress ENTER to go back to the previous menu... ")
        return PrintCollection


class UserInterface:
    
    current_menu = None

    def __init__(self): pass

    @classmethod
    def change_menu(cls, new_menu):
        cls.current_menu = new_menu
        cls.clear_screen()
        cls.current_menu.print_menu()
        cls.perform_actions()

    @classmethod
    def perform_actions(cls):
        while True:
            action_id = raw_input("\nEnter your choice: ")
            action = cls.current_menu.get_action(action_id)

            if action is not None:
                break
            
            print "Index out of range"

        cls.clear_screen()
        cls.current_menu.print_action_header(action["text"])

        new_menu = None

        while True:
            if new_menu is not None:
                break

            new_menu = action["func"]()

        cls.change_menu(new_menu())

    @classmethod
    def print_logo(cls):
        print r"""
       _    _ _                     ____  ____
      / \  | | |__  _   _ _ __ ___ |  _ \| __ )
     / _ \ | | '_ \| | | | '_ ` _ \| | | |  _ \
    / ___ \| | |_) | |_| | | | | | | |_| | |_) |
   /_/   \_\_|_.__/ \__,_|_| |_| |_|____/|____/
                                     version 1.0"""
        print

    @classmethod
    def clear_screen(cls):
        os.system('cls' if os.name == 'nt' else 'clear')
        cls.print_logo()


class AlbumManager:

    def __init__(self, database='music.db'):
        self.database = DatabaseLayer(database)
        self.database.query("CREATE TABLE IF NOT EXISTS Collection(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Artist TEXT NOT NULL, AlbumName TEXT NOT NULL, ReleaseYear INTEGER NOT NULL)")

    def delete_database(self):
        self.database.query("DROP DATABASE Collection")

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


class AlbumPrinter:
    def __init__(self):
        pass

    @classmethod
    def print_albums(cls, data):

        data = list(data)

        if not data:
            print "Database is empty."
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


UserInterface.change_menu(DatabaseMenu())
