import sys
import threading
import speech_recognition
import os
import pymorphy2
import csv

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Dragon_gui import Ui_MainWindow
from database import UnknownType, DataBase


class DragonMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.db = DataBase()
        self.setupUi(self)

        self.recognizeTimer = QtCore.QTimer(self)
        self.recognizeTimer.setInterval(200)  # .5 seconds
        self.recognizeTimer.timeout.connect(self.recognize)

        self.doCommandsTimer = QtCore.QTimer(self)
        self.doCommandsTimer.setInterval(200)  # .5 seconds
        self.doCommandsTimer.timeout.connect(self.do_commands)

        self.startButton.clicked.connect(self.start)
        self.addFileButton.clicked.connect(self.add)
        self.addFolderButton.clicked.connect(self.add)
        # self.addManyFilesButton.clicked.connect(self.add_many)
        # self.addManyFoldersButton.clicked.connect(self.add_many)

        self.setup_commands_settings()

        with speech_recognition.Microphone() as mic:
            self.recognizer = speech_recognition.Recognizer()
            self.recognizer.adjust_for_ambient_noise(source=mic, duration=0.05)
        self.morph = pymorphy2.MorphAnalyzer()
        self.running = False
        self.to_recognize = []
        self.speech = []

    def open_(self, path) -> None:
        os.startfile(path)

    def normalize(self, name : str) -> str:
        """Преобразование слов в строке в начальную форму"""
        normalized_name = []
        for i in name.split():
            normalized_name.append(self.morph.parse(i)[0].normal_form)
        return " ".join(normalized_name)

    def do_commands(self) -> None:
        """Выполнение команд"""
        try:
            if len(self.speech) > 0:
                speech = self.speech.pop(0)
                # Проверка, является ли новое слово коммандой
                if "открыть" == self.normalize(speech.lower()):
                    name = ""
                    max_ = self.db.get_max()
                    # Получаем все следующие n слов, где n - максимальное кол-во слов в названии файла/папки
                    for i in range(max_):
                        if len(self.speech) > 0:
                            name += " " + self.speech.pop(0)
                        else:
                            break
                    # Ставим все слова в начальную форму
                    name_normalized = self.normalize(name)
                    print(name, name_normalized)
                    file_names = self.db.get_all_type_names("file", lambda x : x[0].lower())
                    folder_names = self.db.get_all_type_names("folder", lambda x : x[0].lower())
                    # Смотрю есть ли имя длинны i, если есть, то открываю
                    for i in range(min(max_, len(name.split())), 0, -1):
                        name_i = name.split()[0: i + 1]
                        name_normalized_i = name_normalized.split()[0: i + 1]
                        print(name_i, name_normalized_i)
                        if " ".join(name_i).lower() in file_names:
                            self.open_(self.db.get_path(name.lower(), "file"))
                            break
                        elif " ".join(name_normalized_i).lower() in file_names:
                            self.open_(self.db.get_path(name_normalized.lower(), "file"))
                            break
                        elif " ".join(name_i).lower() in folder_names:
                            self.open_(self.db.get_path(name.lower(), "folder"))
                            break
                        elif " ".join(name_normalized_i).lower() in folder_names:
                            self.open_(self.db.get_path(name_normalized.lower(), "folder"))
                            break

        except Exception as e:
            print(e)

    def recognize(self) -> None:
        """Распознование сказаного"""
        try:
            if len(self.to_recognize) > 0 and self.running:
                audiodata = self.to_recognize.pop(0)
                data = self.recognizer.recognize_google(audio_data=audiodata, language="ru-RU", show_all=False)
                for i in data.split():
                    self.speech.append(i.lower())
        except Exception as e:
            print(e)

    def listen(self) -> None:
        """Запись звука"""
        while self.running:
            with speech_recognition.Microphone() as mic:
                speech = self.recognizer.listen(source=mic, phrase_time_limit=5)
                self.to_recognize.append(speech)

    def start(self) -> None:
        """Запуск/Остановка прослушивания"""
        self.running = not self.running
        if self.running:
            self.recognizeTimer.start()
            self.doCommandsTimer.start()
            self.startButton.setText("Stop")
            thread = threading.Thread(target=self.listen)
            thread.start()
        else:
            self.recognizeTimer.stop()
            self.doCommandsTimer.stop()
            self.startButton.setText("Start")

    def add_widgets_row(self, layout, name, path, x, y) -> None:
        """Добавление строки виджетов nameEdit, pathEdit, browseButton, removeButton"""
        try:
            name_edit = QtWidgets.QLineEdit(layout.parentWidget())
            name_edit.editingFinished.connect(self.changed)
            path_edit = QtWidgets.QLineEdit(layout.parentWidget())
            path_edit.editingFinished.connect(self.changed)
            browse_button = QtWidgets.QPushButton(layout.parentWidget())
            browse_button.setText("Browse")
            browse_button.clicked.connect(self.browse)
            remove_button = QtWidgets.QPushButton(layout.parentWidget())
            remove_button.setText("Remove")
            remove_button.clicked.connect(self.remove)
            name_edit.setText(name)
            path_edit.setText(path)
            # Смещение виджетов на 1 вниз
            widgets = [name_edit, path_edit, browse_button, remove_button]
            for index, widget in enumerate(widgets):
                layout.addWidget(widget, y, x + index)
        except Exception as e:
            print(e)

    def add_widgets(self, layout, widgets_data, x, y) -> None:
        """Добавление несколько строк виджетов"""
        if len(widgets_data) == 0:
            return
        add_button = layout.itemAtPosition(y, x).widget()
        index = layout.indexOf(add_button)  # индекс Add кнопки
        pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
        type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
        add_many_button = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
        spacer_item = layout.itemAtPosition(pos[0] + 1, pos[1])
        layout.removeItem(spacer_item)
        layout.removeWidget(add_many_button)
        layout.removeWidget(add_button)
        for index, i in enumerate(widgets_data):
            self.add_widgets_row(layout, i[1], i[2], x, index + y)
        layout.addWidget(add_button, layout.rowCount(), 0)
        layout.addWidget(add_many_button)
        index = layout.indexOf(add_button)  # индекс Add кнопки
        pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
        layout.addItem(spacer_item, pos[0] + 1, pos[1])

    def setup_commands_settings(self) -> None:
        """Добавление всех виджетов из бд (нужно для запуска приложения)"""
        commands_files = self.db.get_all("file")
        commands_folders = self.db.get_all("folder")
        self.add_widgets(self.filesAreaWidgetLayout, commands_files, 0, 1)
        self.add_widgets(self.foldersAreaWidgetLayout, commands_folders, 0, 1)

    def changed(self) -> None:
        """Смена имени/пути"""
        name_widget = self.centralwidget.sender()
        layout = name_widget.parentWidget().layout()
        index = layout.indexOf(name_widget)
        type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
        pos = layout.getItemPosition(index)[:2]
        name = name_widget.text()
        path_widget = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
        path = path_widget.text()
        self.db.update_name(name, path, type_)

    def add_many(self) -> None:
        """Логика для кнопки Add many File/Folder"""
        try:
            add_button = self.centralwidget.sender()
            layout = add_button.parentWidget().layout()
            index = layout.indexOf(add_button)
            pos = layout.getItemPosition(index)[:2]
            path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете файл', '')[0]
            with open(path, encoding="utf8") as file:
                reader = csv.reader(file, delimiter=';', quotechar='"')
        except Exception as e:
            print(e)
    def add(self) -> None:
        """Логика для кнопки Add File/Folder"""
        try:
            add_button = self.centralwidget.sender()
            layout = add_button.parentWidget().layout()
            index = layout.indexOf(add_button)  # индекс Add кнопки
            pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
            type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
            path = ""
            if type_.lower() == "file":
                path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете приложение', '')[0]
            elif type_.lower() == "folder":
                path = QFileDialog.getExistingDirectoryUrl(self.centralwidget, 'Выберете папку').path()[1:]
            else:
                raise UnknownType
            if path == "":
                return
            all_names = self.db.get_all_type_names(type_, lambda x : x[0].lower())
            name = path.split("/")[-1].split(".")[0]
            similar_names = self.db.get_similar_names(name, type_)
            print(similar_names)
            if len(similar_names) > 0:
                similar_names = sorted(
                    [i[0].split(name.lower())[-1] for i in similar_names if i[0].split(name.lower())[-1].isdigit()])
                print(similar_names, "aboba")
                if len(similar_names) == 0:
                    name += "1"
                elif similar_names[-1].isdigit():
                    name += str(int(similar_names[-1]) + 1)
            if name.lower() in all_names:
                return

            # Добавление строки виджетов
            # add_many_button = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
            # spacer_item = layout.itemAtPosition(pos[0] + 1, pos[1])
            # layout.removeItem(spacer_item)
            # layout.removeWidget(add_many_button)
            # layout.removeWidget(add_button)
            # self.add_widgets_row(layout, name, path, pos[1], pos[0])
            # layout.addWidget(add_button, pos[0] + 1, pos[1])
            # layout.addWidget(add_many_button, pos[0] + 1, pos[1] + 1)
            # layout.addItem(spacer_item, pos[0] + 2, pos[1])
            self.add_widgets(layout,[[0, name, path]], pos[1], pos[0])
            # Добавление записи в бд
            self.db.add(name, path, type_)
        except Exception as e:
            print(e)

    def remove(self) -> None:
        """Логика для кнопки remove"""
        try:
            remove_button = self.centralwidget.sender()
            layout = remove_button.parentWidget().layout()  # индекс remove кнопки
            index = layout.indexOf(remove_button)  # позиция remove кнопки
            pos = list(layout.getItemPosition(index)[:2])
            type_ = layout.parentWidget().objectName().split("_")[1][:-1]
            # Удаление записи из бд
            name = layout.itemAtPosition(pos[0], pos[1] - 3).widget().text()
            self.db.delete(name, type_)
            # Удаление виджетов в одной линии с remove конпкой
            print("pivo")
            for i in range(4):
                widget = layout.itemAtPosition(pos[0], pos[1] - i).widget()
                layout.removeWidget(widget)
            print("pivo1")
            # Сдвиг виджетов
            while type(layout.itemAtPosition(pos[0] + 2, pos[1] - 3)) is not QtWidgets.QSpacerItem:
                print("aboba111")
                name_edit = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
                path_edit = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
                browse_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 1).widget()
                remove_button = layout.itemAtPosition(pos[0] + 1, pos[1]).widget()
                widgets = [name_edit, path_edit, browse_button, remove_button]
                for index, widget in enumerate(widgets):
                    layout.removeWidget(widget)
                    layout.addWidget(widget, pos[0], pos[1] - 3 + index)
                pos[0] += 1
                print("aboba222")
            # Сдвиг addButton, addManyButton и spacerItem
            add_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
            add_many_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
            spacer_item = layout.itemAtPosition(pos[0] + 2, pos[1] - 3)
            layout.removeWidget(add_button)
            layout.removeWidget(add_many_button)
            layout.removeItem(spacer_item)
            layout.addWidget(add_button, pos[0], pos[1] - 3)
            layout.addWidget(add_many_button, pos[0], pos[1] - 2)
            layout.addItem(spacer_item, pos[0] + 1, pos[1] - 3)
        except Exception as e:
            print(e)

    def browse(self) -> None:
        """Логика для кнопки browse"""
        try:
            browse_button = self.centralwidget.sender()
            layout = browse_button.parentWidget().layout()
            type_ = layout.parentWidget().objectName().split("_")[1][:-1]
            path = ""
            if type_.lower() == "file":
                path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете приложение', '')[0]
            elif type_.lower() == "folder":
                path = QFileDialog.getExistingDirectory(self.centralwidget, 'Выберете папку', '')[0]
            else:
                raise UnknownType

            index = layout.indexOf(browse_button)
            pos = layout.getItemPosition(index)[:2]
            name_edit = layout.itemAtPosition(pos[0], pos[1] - 2).widget()
            path_edit = layout.itemAtPosition(pos[0], pos[1] - 1).widget()
            if path == "" or path_edit.text() == path:
                return
            if name_edit.text() == "":
                name_edit.setText(path.split("/")[-1].split(".")[0])
            path_edit = layout.itemAtPosition(pos[0], pos[1] - 1).widget()
            path_edit.setText(path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = DragonMainWindow()
        ex.show()
        sys.exit(app.exec_())
