# -*- coding: utf-8 -*-

import sqlite3


class DatabaseLayer:

    def __init__(self, database='music.db'):
        self.database = database

    def query(self, statements, data=()):
        with sqlite3.connect(self.database) as connection:
            cursor = connection.cursor()
            result = cursor.execute(statements, data)
            connection.commit()

        return result


class Album:
    def __init__(self, artist, album_name, release_year):
        self.artist = artist
        self.album_name = album_name
        self.release_year = release_year

class AlbumManager:

    def __init__(self, database='music.db'):
        self.database = DatabaseLayer(database)
        self.create_new()

    def create_new(self):
        self.database.query("CREATE TABLE IF NOT EXISTS Collection(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Artist TEXT NOT NULL, AlbumName TEXT NOT NULL, ReleaseYear INTEGER NOT NULL);")

    def add_album(self, artist, album_name, release_year):
        self.database.query("INSERT INTO Collection (Artist, AlbumName, ReleaseYear) VALUES (?, ?, ?)", (artist, album_name, release_year))

    def remove_album(self, artist, album_name, release_year): pass

    def print_collection(self):
        results = self.database.query("SELECT ID, Artist, AlbumName, ReleaseYear FROM Collection")

        for row in results:
            print row[0],
            print " ",
            print row[1],
            print " ",
            print row[2],
            print " ",
            print row[3]

    def albums_by_artist(self, artist): pass

    def albums_by_name(self, album_name): pass

    def albums_by_year(self, release_year): pass


my_collection = AlbumManager()
my_collection.add_album("Artysta ziemniak", "Album", "2012")
my_collection.print_collection()