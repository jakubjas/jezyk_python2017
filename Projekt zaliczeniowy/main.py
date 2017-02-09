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

        for action in self.actions:
            line = "| "
            action = "[" + str(action["id"]) + "] " + action["text"]
            line += action
            line += " " * (49 - len(action))
            line += "|"
            print line

        print separator

    def print_action_bar(self, action_name):
        spacer = 25 - int(math.ceil(float(len(action_name))/2))

        text = "=" * spacer
        text += " " + action_name + " "
        text += "=" * spacer
        text += "\n"

        print text


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
                "text": "Load database",
                "func": self.load_database
            }
        ]
    
    def create_database(self):
        name = raw_input("Specify database name (default: music.db): ")
        ApplicationState.album_manager = AlbumManager(name)
        return MainMenu

    def load_database(self):
        name = raw_input("Specify database name (default: music.db): ")

        if not os.path.exists(name):
            print "No such database has been found."
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
                "func": self.print_menu
            },
            {
                "id": 5,
                "text": "Go back",
                "func": lambda: DatabaseMenu
            }
        ]

    def add_album_menu(self):
        return TestMenu

    def delete_album_menu(self): pass

    def search_menu(self): pass

    def database_menu(self): pass


class TestMenu(MenuBase):
    
    def __init__(self):
        self.header = "TEST MENU"

        self.actions = [
            {
                "id": 1,
                "text": "Ziemniak",
                "func": self.ziemniak
            },
            {
                "id": 2,
                "text": "frytki",
                "func": self.frytki
            }
        ]

    def ziemniak(self):
        return MainMenu

    def frytki(self):
        print "lol"
        return MainMenu


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
            action_id = raw_input("\nEnter your choice : ")
            action = cls.current_menu.get_action(action_id)

            if action is not None:
                break 
            
            print "Index out of range"

        cls.clear_screen()
        cls.current_menu.print_action_bar(action["text"])

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


class AlbumPrinter:
    def __init__(self):
        pass

    @classmethod
    def print_albums(cls, data):

        data = list(data)

        if not data:
            print "\nDatabase is empty"
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
