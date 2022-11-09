import sqlite3


class UnknownType(BaseException):
    pass


class DataBase:
    def __init__(self, filename: str = 'database.db'):
        self.connection = sqlite3.connect('database.db')
        self.cursor = self.connection.cursor()
        if self.connection:
            print("Connected successfully!")

        self.connection.execute(
            'create table if not exists Files(id int primary key, name string unique, path string)')
        self.connection.execute(
            'create table if not exists Folders(id int primary key, name string unique, path string)')
        self.connection.commit()

    def add(self, name: str, path: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title() + "s"
        ids = self.cursor.execute(f'select id from {type_}').fetchall()
        id = 0
        if len(ids) > 0:
            id = sorted(ids)[-1][0] + 1
        self.cursor.execute(f'insert into {type_} values(?, ?, ?)', (id, name, path))
        self.connection.commit()

    def get_path(self, name: str, type_: str) -> str:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()

        return self.cursor.execute(f'select path from {type_}s where name == ?', (name,)).fetchone()[0]

    def update(self, old_name: str, new_name: str, path: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        self.cursor.execute(f'update {type_}s set name == ?, path == ? where name == ?',
                            (new_name, path, old_name))
        self.connection.commit()

    def delete(self, name: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        self.cursor.execute(f'delete from {type_}s where name == ?', (name,))
        self.connection.commit()

    def getAllNames(self, type_: str) -> list:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title() + "s"
        return self.cursor.execute(f"select name from {type_}").fetchall()

    def getSimilarNames(self, name: str, type_: str) -> list:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        names = self.getAllNames(type_)
        similarNames = []
        for i in names:
            print(i)
            if name in i[0]:
                similarNames.append(i)
        return similarNames
