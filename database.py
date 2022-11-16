import sqlite3


class UnknownType(Exception):
    pass


class DataBase:
    def __init__(self, basename: str = 'database.db'):
        self.connection = sqlite3.connect(basename)
        self.cursor = self.connection.cursor()
        if self.connection:
            print("Connected successfully!")

        self.connection.execute(
            'create table if not exists Files(id integer primary key AUTOINCREMENT, name string unique, path string)')
        self.connection.execute(
            'create table if not exists Folders(id integer primary key AUTOINCREMENT, name string unique, path string)')
        self.connection.execute('create table if not exists Max(max integer primary key)')
        self.connection.commit()

    def add(self, name: str, path: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title() + "s"
        self.cursor.execute(f'insert into {type_}(name, path) values(?, ?)', (name.lower(), path))
        self.connection.commit()

    def get_path(self, name: str, type_: str) -> str:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        print(self.cursor.execute(f'select path from {type_}s where name == ?', (name.lower(),)).fetchone())

        return self.cursor.execute(f'select path from {type_}s where name == ?', (name.lower(),)).fetchone()[0]

    def update(self, old_name: str, new_name: str, path: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        self.cursor.execute(f'update {type_}s set name == ?, path == ? where name == ?',
                            (new_name.lower(), path, old_name))
        self.connection.commit()

    def update_name(self, new_name: str, path: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        self.cursor.execute(f'update {type_}s set name == ? where path == ?',
                            (new_name.lower(), path))
        self.connection.commit()

    def delete(self, name: str, type_: str) -> None:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title()
        self.cursor.execute(f'delete from {type_}s where name == ?', (name.lower(),))
        self.connection.commit()

    def get_all(self, type_: str) -> list:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title() + "s"
        return self.cursor.execute(f"select * from {type_}").fetchall()

    def get_all_type_names(self, type_: str) -> list:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        type_ = type_.title() + "s"
        return self.cursor.execute(f"select name from {type_}").fetchall()

    def get_all_names(self) -> list:
        return self.cursor.execute("select name from Files").fetchall() + self.cursor.execute(
            "select name from Folders").fetchall()

    def get_similar_names(self, name: str, type_: str) -> list:
        type_ = type_.lower()
        if type_ != "file" and type_ != "folder":
            raise UnknownType
        names = self.get_all_type_names(type_)
        similar_names = []
        for i in names:
            print(i)
            if name in i[0]:
                similar_names.append(i)
        return similar_names

    # def add_max(self, max: int) -> None:
    #     self.cursor.execute('insert into Max value(?)', (max,))

    def get_max(self) -> int:
        names = [len(i[0].split()) for i in self.get_all_names()]
        return max(names)
        # return int(self.cursor.execute('select max from Max').fetchone()[0])

    # def update_max(self, max: int) -> None:
    #     self.cursor.execute('update Max set max == ?', (max,))
    #     self.connection.commit()

    # def delete_max(self, max: int) -> None:
    #     self.cursor.execute('delete from Max')
    #     self.connection.commit()
