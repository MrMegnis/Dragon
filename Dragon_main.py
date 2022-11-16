import sys
import threading
import speech_recognition
import os

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

        self.addFileButton.clicked.connect(self.add)
        self.addFolderButton.clicked.connect(self.add)
        # self.addManyFilesButton.clicked.connect(self.add_many)
        # self.addManyFoldersButton.clicked.connect(self.add_many)

        self.setup_commands_settings()

        with speech_recognition.Microphone() as mic:
            self.recognizer = speech_recognition.Recognizer()
            self.recognizer.adjust_for_ambient_noise(source=mic, duration=0.05)

        self.startButton.clicked.connect(self.start)
        self.running = False
        self.to_recognize = []
        self.speech = []

    def open_(self, path):
        os.startfile(path)

    def do_commands(self) -> None:
        try:
            if len(self.speech) > 0:
                speech = self.speech.pop(0)
                if "открыть" == speech.lower():
                    name = ""
                    for i in range(self.db.get_max()):
                        if len(self.speech) > 0:
                            name += self.speech.pop(0)
                        else:
                            break
                    print(name)
                    print([i[0].lower() for i in self.db.get_all_type_names("file")])
                    print([i[0].lower() for i in self.db.get_all_type_names("folder")])
                    if name.lower() in [i[0].lower() for i in self.db.get_all_type_names("file")]:
                        print("aboba file")
                        self.open_(self.db.get_path(name.lower(), "file"))
                    elif name.lower() in [i[0].lower() for i in self.db.get_all_type_names("folder")]:
                        print("aboba folder")
                        self.open_(self.db.get_path(name.lower(), "folder"))

        except Exception as e:
            print(e, "aboba")

    def recognize(self) -> None:
        try:
            if len(self.to_recognize) > 0 and self.running:
                audiodata = self.to_recognize.pop(0)
                data = self.recognizer.recognize_google(audio_data=audiodata, language="ru-RU", show_all=False)
                # data_en = self.recognizer.recognize_google(audio_data=audiodata, language="en-EN", show_all=False)
                print(data)
                for i in data.split():
                    self.speech.append(i.lower())
        except Exception as e:
            print(e)

    def listen(self) -> None:
        while self.running:
            with speech_recognition.Microphone() as mic:
                speech = self.recognizer.listen(source=mic, phrase_time_limit=5)
                self.to_recognize.append(speech)

    def start(self) -> None:
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

    def add_widgets_row(self, layout, name, path, x, y):
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

    def add_widgets(self, layout, widgets_data):
        if len(widgets_data) == 0:
            return
        add_button = layout.itemAtPosition(layout.rowCount() - 2, 0).widget()
        index = layout.indexOf(add_button)  # индекс Add кнопки
        pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
        type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
        add_many_button = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
        spacer_item = layout.itemAtPosition(pos[0] + 1, pos[1])
        layout.removeItem(spacer_item)
        layout.removeWidget(add_many_button)
        layout.removeWidget(add_button)
        for index, i in enumerate(widgets_data):
            self.add_widgets_row(layout, i[1], i[2], 0, index + 2)
        # print(layout.rowCount(), layout.columnCount(), type_)
        layout.addWidget(add_button, layout.rowCount(), 0)
        layout.addWidget(add_many_button)
        index = layout.indexOf(add_button)  # индекс Add кнопки
        pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
        # print(pos)
        layout.addItem(spacer_item, pos[0] + 1, pos[1])

    def setup_commands_settings(self):
        commands_files = self.db.get_all("file")
        commands_folders = self.db.get_all("folder")
        self.add_widgets(self.filesAreaWidgetLayout, commands_files)
        self.add_widgets(self.foldersAreaWidgetLayout, commands_folders)
        # addButton = self.foldersAreaWidgetLayout.itemAtPosition(self.foldersAreaWidgetLayout.rowCount() - 2, 0).widget()
        # print(addButton)

    def changed(self) -> None:
        name_widget = self.centralwidget.sender()
        layout = name_widget.parentWidget().layout()
        index = layout.indexOf(name_widget)
        type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
        pos = layout.getItemPosition(index)[:2]
        name = name_widget.text()
        path_widget = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
        path = path_widget.text()
        print(name, path)
        self.db.update_name(name, path, type_)

    # def add_many(self) -> None:
    """Логика для кнопки Add many File/Folder"""

    #     add_button = self.centralwidget.sender()
    #     layout = add_button.parentWidget().layout()
    #     index = layout.indexOf(add_button)
    #     pos = layout.getItemPosition(index)[:2]
    #     print(pos)
    #     print(layout.itemAtPosition(pos[0], pos[1]).widget().text(), layout.itemAtPosition(pos[0], pos[1] - 2))

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
                print(path)
                # path = QFileInfo(path).absoluteDir().absolutePath()
            else:
                raise UnknownType
            if path == "":
                return
            name = path.split("/")[-1].split(".")[0]
            similar_names = self.db.get_similar_names(name, type_)
            if len(similar_names) > 0:
                similar_names = sorted(
                    [i[0].split(name)[-1] for i in similar_names])  # -ПОФИКСЬ111!111   -потом пофикшу...
                name += str(len(similar_names))
            self.db.add(name, path, type_)
            # print(pos)
            add_many_button = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
            spacer_item = layout.itemAtPosition(pos[0] + 1, pos[1])
            layout.removeItem(spacer_item)
            layout.removeWidget(add_many_button)
            layout.removeWidget(add_button)
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
                layout.addWidget(widget, pos[0], pos[1] + index)
            layout.addWidget(add_button, pos[0] + 1, pos[1])
            layout.addWidget(add_many_button, pos[0] + 1, pos[1] + 1)
            layout.addItem(spacer_item, pos[0] + 2, pos[1], 1, 1)
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
            for i in range(4):
                widget = layout.itemAtPosition(pos[0], pos[1] - i).widget()
                layout.removeWidget(widget)
            # Сдвиг виджетов
            while type(layout.itemAtPosition(pos[0] + 2, pos[1] - 3)) is not QtWidgets.QSpacerItem:
                name_edit = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
                path_edit = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
                browse_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 1).widget()
                remove_button = layout.itemAtPosition(pos[0] + 1, pos[1]).widget()
                widgets = [name_edit, path_edit, browse_button, remove_button]
                for index, widget in enumerate(widgets):
                    layout.removeWidget(widget)
                    layout.addWidget(widget, pos[0], pos[1] - 3 + index, 1, 1)
                pos[0] += 1
            add_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
            add_many_button = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
            spacer_item = layout.itemAtPosition(pos[0] + 2, pos[1] - 3)
            layout.removeWidget(add_button)
            layout.removeWidget(add_many_button)
            layout.removeItem(spacer_item)
            layout.addWidget(add_button, pos[0], pos[1] - 3, 1, 1)
            layout.addWidget(add_many_button, pos[0], pos[1] - 2, 1, 1)
            layout.addItem(spacer_item, pos[0] + 1, pos[1] - 3, 1, 1)
        except Exception as e:
            print(e)

    def browse(self) -> None:
        """Логика для кнопки browse"""
        try:
            # print(Path)
            sender = self.centralwidget.sender()
            layout = sender.parentWidget().layout()
            type_ = layout.parentWidget().objectName().split("_")[1][:-1]
            print(layout.objectName().split("_"))
            path = ""
            print(type_, "aboba_type")
            if type_.lower() == "file":
                path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете приложение', '')[0]
            elif type_.lower() == "folder":
                path = QFileDialog.getExistingDirectory(self.centralwidget, 'Выберете папку', '')[0]
            else:
                raise UnknownType
            if path == "":
                return
            index = layout.indexOf(sender)
            pos = layout.getItemPosition(index)[:2]
            name_edit = layout.itemAtPosition(pos[0], pos[1] - 2).widget()
            if name_edit.text() == "":
                name_edit.setText(path.split("/")[-1].split(".")[0])
            path_edit = layout.itemAtPosition(pos[0], pos[1] - 1).widget()
            path_edit.setText(path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = DragonMainWindow()
        ex.show()
        # ex.db.connection.close()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
