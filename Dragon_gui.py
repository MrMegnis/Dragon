from PyQt5 import QtCore, QtGui, QtWidgets
from StyleSheet import pages_StyleSheet, centralwidget_StyleSheet


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 800)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(centralwidget_StyleSheet)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Pages = QtWidgets.QTabWidget(self.centralwidget)
        self.Pages.setEnabled(True)
        self.Pages.setStyleSheet(pages_StyleSheet)
        self.Pages.setObjectName("Pages")
        self.Start = QtWidgets.QWidget()
        self.Start.setStyleSheet("")
        self.Start.setObjectName("Start")
        self.startLayout = QtWidgets.QGridLayout(self.Start)
        self.startLayout.setVerticalSpacing(4)
        self.startLayout.setObjectName("startLayout")
        self.Name = QtWidgets.QLabel(self.Start)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.startLayout.addWidget(self.Name, 0, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.Start)
        self.startButton.setStyleSheet("")
        self.startButton.setObjectName("startButton")
        self.startLayout.addWidget(self.startButton, 1, 0, 1, 1)
        self.Pages.addTab(self.Start, "")
        self.filestoOpen = QtWidgets.QWidget()
        self.filestoOpen.setMinimumSize(QtCore.QSize(0, 0))
        self.filestoOpen.setObjectName("filestoOpen")
        self.filesLayout = QtWidgets.QGridLayout(self.filestoOpen)
        self.filesLayout.setObjectName("filesLayout")
        self.scrollareaFiles = QtWidgets.QScrollArea(self.filestoOpen)
        self.scrollareaFiles.setStyleSheet("")
        self.scrollareaFiles.setWidgetResizable(True)
        self.scrollareaFiles.setObjectName("scrollareaFiles")
        self.scrollAreaWidgetContents_Files = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Files.setGeometry(QtCore.QRect(0, 0, 458, 500))
        self.scrollAreaWidgetContents_Files.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents_Files.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollAreaWidgetContents_Files.setAutoFillBackground(False)
        self.scrollAreaWidgetContents_Files.setObjectName("scrollAreaWidgetContents_Files")
        self.filesAreaWidgetLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Files)
        self.filesAreaWidgetLayout.setObjectName("filesAreaWidgetLayout")
        self.filePathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.filePathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filePathLabel.setObjectName("filePathLabel")
        self.filesAreaWidgetLayout.addWidget(self.filePathLabel, 0, 1, 1, 1)
        self.addManyFilesButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.addManyFilesButton.setObjectName("addManyFilesButton")
        self.filesAreaWidgetLayout.addWidget(self.addManyFilesButton, 1, 1, 1, 1)
        self.browseFileButtonLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.browseFileButtonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browseFileButtonLabel.setObjectName("browseFileButtonLabel")
        self.filesAreaWidgetLayout.addWidget(self.browseFileButtonLabel, 0, 2, 1, 1)
        self.removeAllFilesButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.removeAllFilesButton.setObjectName("removeAllFilesButton")
        self.filesAreaWidgetLayout.addWidget(self.removeAllFilesButton, 0, 3, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.fileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.filesAreaWidgetLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.filesAreaWidgetLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.addFileButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.addFileButton.setObjectName("addFileButton")
        self.filesAreaWidgetLayout.addWidget(self.addFileButton, 1, 0, 1, 1)
        self.scrollareaFiles.setWidget(self.scrollAreaWidgetContents_Files)
        self.filesLayout.addWidget(self.scrollareaFiles, 0, 0, 1, 1)
        self.Pages.addTab(self.filestoOpen, "")
        self.folderstoOpen = QtWidgets.QWidget()
        self.folderstoOpen.setObjectName("folderstoOpen")
        self.foldersLayout = QtWidgets.QGridLayout(self.folderstoOpen)
        self.foldersLayout.setObjectName("foldersLayout")
        self.scrollareaFolders = QtWidgets.QScrollArea(self.folderstoOpen)
        self.scrollareaFolders.setWidgetResizable(True)
        self.scrollareaFolders.setObjectName("scrollareaFolders")
        self.scrollAreaWidgetContents_Folders = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Folders.setGeometry(QtCore.QRect(0, 0, 458, 500))
        self.scrollAreaWidgetContents_Folders.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents_Folders.setObjectName("scrollAreaWidgetContents_Folders")
        self.foldersAreaWidgetLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Folders)
        self.foldersAreaWidgetLayout.setObjectName("foldersAreaWidgetLayout")
        self.addFolderButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.addFolderButton.setObjectName("addFolderButton")
        self.foldersAreaWidgetLayout.addWidget(self.addFolderButton, 1, 0, 1, 1)
        self.addManyFoldersButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.addManyFoldersButton.setObjectName("addManyFoldersButton")
        self.foldersAreaWidgetLayout.addWidget(self.addManyFoldersButton, 1, 1, 1, 1)
        self.folderPathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.folderPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.folderPathLabel.setObjectName("folderPathLabel")
        self.foldersAreaWidgetLayout.addWidget(self.folderPathLabel, 0, 1, 1, 1)
        self.folderNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.folderNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.folderNameLabel.setObjectName("folderNameLabel")
        self.foldersAreaWidgetLayout.addWidget(self.folderNameLabel, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.foldersAreaWidgetLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.removeAllFoldersButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.removeAllFoldersButton.setObjectName("removeAllFoldersButton")
        self.foldersAreaWidgetLayout.addWidget(self.removeAllFoldersButton, 0, 3, 1, 1)
        self.browseFolderButtonLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.browseFolderButtonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browseFolderButtonLabel.setObjectName("browseFolderButtonLabel")
        self.foldersAreaWidgetLayout.addWidget(self.browseFolderButtonLabel, 0, 2, 1, 1)
        self.scrollareaFolders.setWidget(self.scrollAreaWidgetContents_Folders)
        self.foldersLayout.addWidget(self.scrollareaFolders, 0, 0, 1, 1)
        self.Pages.addTab(self.folderstoOpen, "")
        self.gridLayout.addWidget(self.Pages, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Pages.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Name.setText(_translate("MainWindow", "Dragon"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.Pages.setTabText(self.Pages.indexOf(self.Start), _translate("MainWindow", "Start"))
        self.filePathLabel.setText(_translate("MainWindow", "File to open(Path)"))
        self.addManyFilesButton.setText(_translate("MainWindow", "Add many Files"))
        self.browseFileButtonLabel.setText(_translate("MainWindow", "Tap to browse path"))
        self.removeAllFilesButton.setText(_translate("MainWindow", "Remove all"))
        self.fileNameLabel.setText(_translate("MainWindow", "Voice command(Name)"))
        self.addFileButton.setText(_translate("MainWindow", "Add File"))
        self.Pages.setTabText(self.Pages.indexOf(self.filestoOpen), _translate("MainWindow", "Files to open"))
        self.addFolderButton.setText(_translate("MainWindow", "Add Folder"))
        self.addManyFoldersButton.setText(_translate("MainWindow", "Add many Folders"))
        self.folderPathLabel.setText(_translate("MainWindow", "Folder to open(Path)"))
        self.folderNameLabel.setText(_translate("MainWindow", "Voice command(Name)"))
        self.removeAllFoldersButton.setText(_translate("MainWindow", "Remove all"))
        self.browseFolderButtonLabel.setText(_translate("MainWindow", "Tap to browse path"))
        self.Pages.setTabText(self.Pages.indexOf(self.folderstoOpen), _translate("MainWindow", "Folders to open"))
