import sys
import threading
import speech_recognition

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from Dragon_gui import Ui_MainWindow
from database import UnknownType, DataBase

class DragonMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.db = DataBase()
        self.setupUi(self)

        self.recognizeTimer = QtCore.QTimer(self)
        self.recognizeTimer.setInterval(200) #.5 seconds
        self.recognizeTimer.timeout.connect(self.recognize)

        self.doCommandsTimer = QtCore.QTimer(self)
        self.doCommandsTimer.setInterval(200)  # .5 seconds
        self.doCommandsTimer.timeout.connect(self.doCommands)


        self.fileName1.editingFinished.connect(self.changed)
        self.filePath1.editingFinished.connect(self.changed)
        self.folderName1.editingFinished.connect(self.changed)
        self.folderPath1.editingFinished.connect(self.changed)
        # self.removeFileButton1.clicked.connect(self.remove)
        # self.removeFolderButton1.clicked.connect(self.remove)
        self.browsefileButton1.clicked.connect(self.browse)
        self.browsefolderButton1.clicked.connect(self.browse)
        self.addFileButton.clicked.connect(self.add)
        self.addFolderButton.clicked.connect(self.add)
        self.addManyFilesButton.clicked.connect(self.addMany)
        self.addManyFoldersButton.clicked.connect(self.addMany)

        with speech_recognition.Microphone() as mic:
            self.recognizer = speech_recognition.Recognizer()
            self.recognizer.adjust_for_ambient_noise(source=mic, duration=0.05)

        self.startButton.clicked.connect(self.start)
        self.running = False
        self.to_recognize = []
        self.speech = []

    def doCommands(self) -> None:
        try:
            # print("aboba222")
            if len(self.speech) > 0:
                speech = self.speech.pop(0).split()
                if "открыть" in speech:
                    print("Открыто))))")
        except Exception as e:
            print(e)
    def recognize(self) -> None:
        try:
            # print("aboba")
            if len(self.to_recognize) > 0 and self.running:
                audiodata = self.to_recognize.pop(0)
                data = self.recognizer.recognize_google(audio_data=audiodata, language="ru-RU", show_all=False)
                print(data)
                self.speech.append(data)
        except Exception as e:
            print(e)

    def listen(self) -> None:
        while self.running:
            # print("aboba")
            with speech_recognition.Microphone() as mic:
                speech = self.recognizer.listen(source=mic, phrase_time_limit=5)
                self.to_recognize.append(speech)
                # self.recognize(speech)

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


    def changed(self) -> None:
        print("aboba")

    def addMany(self) -> None:
        addButton = self.centralwidget.sender()
        layout = addButton.parentWidget().layout()
        index = layout.indexOf(addButton)
        pos = layout.getItemPosition(index)[:2]
        print(pos)
        print(layout.itemAtPosition(pos[0], pos[1]).widget().text(), layout.itemAtPosition(pos[0], pos[1] - 2))

    def add(self) -> None:
        '''Логика для кнопки Add File/Folder'''
        try:
            addButton = self.centralwidget.sender()
            layout = addButton.parentWidget().layout()
            index = layout.indexOf(addButton)  # индекс Add кнопки
            pos = layout.getItemPosition(index)[:2]  # позиция Add кнопки
            type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
            path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете приложение', '')[0]
            name = path.split("/")[-1].split(".")[0]
            similarNames = self.db.getSimilarNames(name, type_)
            if len(similarNames) > 0:
                similarNames = sorted([i[0].split(name)[-1] for i in similarNames]) ####ПОФИКСЬ111!111
                name += str(len(similarNames))
            self.db.add(name, path, type_)
            # print(pos)
            addManyButton = layout.itemAtPosition(pos[0], pos[1] + 1).widget()
            spacerItem = layout.itemAtPosition(pos[0] + 1, pos[1])
            layout.removeItem(spacerItem)
            layout.removeWidget(addManyButton)
            layout.removeWidget(addButton)
            nameEdit = QtWidgets.QLineEdit(layout.parentWidget())
            nameEdit.editingFinished.connect(self.changed)
            pathEdit = QtWidgets.QLineEdit(layout.parentWidget())
            pathEdit.editingFinished.connect(self.changed)
            browseButton = QtWidgets.QPushButton(layout.parentWidget())
            browseButton.setText("Browse")
            browseButton.clicked.connect(self.browse)
            removeButton = QtWidgets.QPushButton(layout.parentWidget())
            removeButton.setText("Remove")
            removeButton.clicked.connect(self.remove)
            nameEdit.setText(name)
            pathEdit.setText(path)
            # Смещение виджетов на 1 вниз
            widgets = [nameEdit, pathEdit, browseButton, removeButton]
            for index, widget in enumerate(widgets):
                layout.addWidget(widget, pos[0], pos[1] + index)
            layout.addWidget(addButton, pos[0] + 1, pos[1])
            layout.addWidget(addManyButton, pos[0] + 1, pos[1] + 1)
            layout.addItem(spacerItem, pos[0] + 2, pos[1], 1, 1)
        except Exception as e:
            print(e)

    def remove(self) -> None:
        try:
            '''Логика для кнопки remove'''
            removeButton = self.centralwidget.sender()
            layout = removeButton.parentWidget().layout()# индекс remove кнопки
            index = layout.indexOf(removeButton)# позиция remove кнопки
            pos = list(layout.getItemPosition(index)[:2])
            type_ = layout.parentWidget().objectName().split("_")[1][0:-1]
            # Удаление записи из бд
            name = layout.itemAtPosition(pos[0], pos[1] - 3).widget().text()
            self.db.delete(name, type_)
            # Удаление виджетов в одной линии с remove конпкой
            for i in range(4):
                widget = layout.itemAtPosition(pos[0], pos[1] - i).widget()
                layout.removeWidget(widget)
            #Сдвиг виджетов
            while type(layout.itemAtPosition(pos[0] + 2, pos[1] - 3)) is not QtWidgets.QSpacerItem:
                nameEdit = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
                pathEdit = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
                browseButton = layout.itemAtPosition(pos[0] + 1, pos[1] - 1).widget()
                removeButton = layout.itemAtPosition(pos[0] + 1, pos[1]).widget()
                widgets = [nameEdit, pathEdit, browseButton, removeButton]
                for index, widget in enumerate(widgets):
                    layout.removeWidget(widget)
                    layout.addWidget(widget, pos[0], pos[1] - 3 + index, 1, 1)
                pos[0] += 1
            addButton = layout.itemAtPosition(pos[0] + 1, pos[1] - 3).widget()
            addManyButton = layout.itemAtPosition(pos[0] + 1, pos[1] - 2).widget()
            spacerItem = layout.itemAtPosition(pos[0] + 2, pos[1] - 3)
            layout.removeWidget(addButton)
            layout.removeWidget(addManyButton)
            layout.removeItem(spacerItem)
            layout.addWidget(addButton, pos[0], pos[1] - 3, 1, 1)
            layout.addWidget(addManyButton, pos[0], pos[1] - 2, 1, 1)
            layout.addItem(spacerItem, pos[0] + 1, pos[1] - 3, 1, 1)
        except Exception as e:
            print(e)

    def browse(self)-> None:
        try:
            '''Логика для кнопки browse'''
            path = QFileDialog.getOpenFileName(self.centralwidget, 'Выберете приложение', '')[0]
            # print(Path)
            sender = self.centralwidget.sender()
            layout = sender.parentWidget().layout()
            index = layout.indexOf(sender)
            pos = layout.getItemPosition(index)[:2]
            nameEdit = layout.itemAtPosition(pos[0], pos[1] - 2).widget()
            if nameEdit.text() == "":
                nameEdit.setText(path.split("/")[-1].split(".")[0])
            pathEdit = layout.itemAtPosition(pos[0], pos[1] - 1).widget()
            pathEdit.setText(path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        ex = DragonMainWindow()
        ex.show()
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
