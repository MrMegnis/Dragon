from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(500, 500)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        MainWindow.setMaximumSize(QtCore.QSize(500, 500))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color: #2B2D42;\n"
"}\n"
"\n"
"/*Buttons settings*/\n"
"QPushButton {\n"
"    color: #F9F5E3;\n"
"    border: #414464;\n"
"    border-radius: 5px;\n"
"    background-color: #414464;\n"
"    min-width: 80px;\n"
"    min-height: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #D90429;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #EF233C;\n"
"}\n"
"\n"
"/*Label settings*/\n"
"QLabel {\n"
"    color: #F9F5E3;\n"
"    border: 0px solid #414464;\n"
"    border-radius: 2px;\n"
"    padding: 2px #642669;\n"
"    background-color: #2B2D42;\n"
"    min-width: 80px;\n"
"    min-height: 15px;\n"
"}\n"
"\n"
"/*Line edit settings*/\n"
"QLineEdit {\n"
"    color: #F9F5E3;\n"
"    border: 2px solid #414464;\n"
"    border-radius: 2px;\n"
"    padding: 5px ;\n"
"    background-color: #2B2D42;\n"
"    min-width: 80px;\n"
"    min-height: 15px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Pages = QtWidgets.QTabWidget(self.centralwidget)
        self.Pages.setEnabled(True)
        self.Pages.setStyleSheet("/*TAB WIDGET*/\n"
"QTabWidget::pane {\n"
"    border: 2px solid #414464;\n"
"    border-bottom-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"QTabBar::tab {\n"
"    color: #F9F5E3;\n"
"    background-color: #414464;\n"
"    border: #642669;\n"
"    border-bottom-color: #2B2D42; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 10ex;\n"
"    padding: 2px;\n"
"}\n"
"QTabBar::tab:hover {\n"
"    background-color: #D90429;\n"
"}\n"
"QTabBar::tab:pressed {\n"
"    background-color: #EF233C;\n"
"}\n"
"\n"
"/*SCROLL BAR*/\n"
"QScrollBar:vertical {\n"
"    border:none;\n"
"    background-color: #2B2D42;\n"
"    width:14px;\n"
"    margin: 15px 0 15px 0;\n"
"    boder-radius: 0px;\n"
"}\n"
"QScrollBar:handle:vertical {\n"
"    background-color: #414464;\n"
"    min-height: 30px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar:handle:vertical:hover {\n"
"    background-color: #D90429;\n"
"}\n"
"QScrollBar:handle:vertical:pressed {\n"
"    background-color: #EF233C;\n"
"}\n"
"\n"
"/*Btn top*/\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: #414464;\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {\n"
"    background-color: #D90429;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed {\n"
"    background-color: #EF233C;\n"
"}\n"
"\n"
"/*Btn bottom*/\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: #414464;\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {\n"
"    background-color: #D90429;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {\n"
"    background-color: #EF233C;\n"
"}\n"
"\n"
"\n"
"/*Reset arrow*/\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background:none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background:none;\n"
"}\n"
"\n"
"/*Scroll Area settings*/\n"
"QScrollArea{\n"
"    border: none;\n"
"}\n"
"")
        self.Pages.setObjectName("Pages")
        self.Start = QtWidgets.QWidget()
        self.Start.setStyleSheet("")
        self.Start.setObjectName("Start")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Start)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Name = QtWidgets.QLabel(self.Start)
        self.Name.setAlignment(QtCore.Qt.AlignCenter)
        self.Name.setObjectName("Name")
        self.gridLayout_2.addWidget(self.Name, 0, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.Start)
        self.startButton.setStyleSheet("")
        self.startButton.setObjectName("startButton")
        self.gridLayout_2.addWidget(self.startButton, 1, 0, 1, 1)
        self.Pages.addTab(self.Start, "")
        self.filestoOpen = QtWidgets.QWidget()
        self.filestoOpen.setMinimumSize(QtCore.QSize(0, 0))
        self.filestoOpen.setObjectName("filestoOpen")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.filestoOpen)
        self.gridLayout_3.setObjectName("gridLayout_3")
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
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Files)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fileName1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_Files)
        self.fileName1.setMinimumSize(QtCore.QSize(94, 29))
        self.fileName1.setObjectName("fileName1")
        self.gridLayout_4.addWidget(self.fileName1, 1, 0, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.fileNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout_4.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 3, 0, 1, 1)
        self.addFileButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.addFileButton.setObjectName("addFileButton")
        self.gridLayout_4.addWidget(self.addFileButton, 2, 0, 1, 1)
        self.filePathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.filePathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.filePathLabel.setObjectName("filePathLabel")
        self.gridLayout_4.addWidget(self.filePathLabel, 0, 1, 1, 1)
        self.filePath1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_Files)
        self.filePath1.setMinimumSize(QtCore.QSize(94, 29))
        self.filePath1.setObjectName("filePath1")
        self.gridLayout_4.addWidget(self.filePath1, 1, 1, 1, 1)
        self.addManyFilesButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.addManyFilesButton.setObjectName("addManyFilesButton")
        self.gridLayout_4.addWidget(self.addManyFilesButton, 2, 1, 1, 1)
        self.browsefileButton1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.browsefileButton1.setObjectName("browsefileButton1")
        self.gridLayout_4.addWidget(self.browsefileButton1, 1, 2, 1, 1)
        self.browseFileButtonLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Files)
        self.browseFileButtonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browseFileButtonLabel.setObjectName("browseFileButtonLabel")
        self.gridLayout_4.addWidget(self.browseFileButtonLabel, 0, 2, 1, 1)
        self.removeAllFilesButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.removeAllFilesButton.setObjectName("removeAllFilesButton")
        self.gridLayout_4.addWidget(self.removeAllFilesButton, 0, 3, 1, 1)
        self.removeFileButton1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Files)
        self.removeFileButton1.setObjectName("removeFileButton1")
        self.gridLayout_4.addWidget(self.removeFileButton1, 1, 3, 1, 1)
        self.scrollareaFiles.setWidget(self.scrollAreaWidgetContents_Files)
        self.gridLayout_3.addWidget(self.scrollareaFiles, 0, 1, 1, 1)
        self.Pages.addTab(self.filestoOpen, "")
        self.folderstoOpen = QtWidgets.QWidget()
        self.folderstoOpen.setObjectName("folderstoOpen")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.folderstoOpen)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.scrollareaFolders = QtWidgets.QScrollArea(self.folderstoOpen)
        self.scrollareaFolders.setWidgetResizable(True)
        self.scrollareaFolders.setObjectName("scrollareaFolders")
        self.scrollAreaWidgetContents_Folders = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_Folders.setGeometry(QtCore.QRect(0, 0, 458, 500))
        self.scrollAreaWidgetContents_Folders.setMinimumSize(QtCore.QSize(0, 500))
        self.scrollAreaWidgetContents_Folders.setObjectName("scrollAreaWidgetContents_Folders")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_Folders)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.addFolderButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.addFolderButton.setObjectName("addFolderButton")
        self.gridLayout_6.addWidget(self.addFolderButton, 2, 0, 1, 1)
        self.removeFolderButton1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.removeFolderButton1.setObjectName("removeFolderButton1")
        self.gridLayout_6.addWidget(self.removeFolderButton1, 1, 3, 1, 1)
        self.folderName1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_Folders)
        self.folderName1.setObjectName("folderName1")
        self.gridLayout_6.addWidget(self.folderName1, 1, 0, 1, 1)
        self.folderPath1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_Folders)
        self.folderPath1.setObjectName("folderPath1")
        self.gridLayout_6.addWidget(self.folderPath1, 1, 1, 1, 1)
        self.folderPathLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.folderPathLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.folderPathLabel.setObjectName("folderPathLabel")
        self.gridLayout_6.addWidget(self.folderPathLabel, 0, 1, 1, 1)
        self.folderNameLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.folderNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.folderNameLabel.setObjectName("folderNameLabel")
        self.gridLayout_6.addWidget(self.folderNameLabel, 0, 0, 1, 1)
        self.browsefolderButton1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.browsefolderButton1.setObjectName("browsefolderButton1")
        self.gridLayout_6.addWidget(self.browsefolderButton1, 1, 2, 1, 1)
        self.browseFolderButtonLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_Folders)
        self.browseFolderButtonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.browseFolderButtonLabel.setObjectName("browseFolderButtonLabel")
        self.gridLayout_6.addWidget(self.browseFolderButtonLabel, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem1, 3, 0, 1, 1)
        self.removeAllFoldersButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.removeAllFoldersButton.setObjectName("removeAllFoldersButton")
        self.gridLayout_6.addWidget(self.removeAllFoldersButton, 0, 3, 1, 1)
        self.addManyFoldersButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_Folders)
        self.addManyFoldersButton.setObjectName("addManyFoldersButton")
        self.gridLayout_6.addWidget(self.addManyFoldersButton, 2, 1, 1, 1)
        self.scrollareaFolders.setWidget(self.scrollAreaWidgetContents_Folders)
        self.gridLayout_5.addWidget(self.scrollareaFolders, 0, 0, 1, 1)
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
        self.fileName1.setText(_translate("MainWindow", "Voice command(Name)"))
        self.fileNameLabel.setText(_translate("MainWindow", "Voice command(Name)"))
        self.addFileButton.setText(_translate("MainWindow", "Add File"))
        self.filePathLabel.setText(_translate("MainWindow", "File to open(Path)"))
        self.filePath1.setText(_translate("MainWindow", "File to open(Path)"))
        self.addManyFilesButton.setText(_translate("MainWindow", "Add many Files"))
        self.browsefileButton1.setText(_translate("MainWindow", "Browse"))
        self.browseFileButtonLabel.setText(_translate("MainWindow", "Tap to browse path"))
        self.removeAllFilesButton.setText(_translate("MainWindow", "Remove all"))
        self.removeFileButton1.setText(_translate("MainWindow", "Remove"))
        self.Pages.setTabText(self.Pages.indexOf(self.filestoOpen), _translate("MainWindow", "Files to open"))
        self.addFolderButton.setText(_translate("MainWindow", "Add Folder"))
        self.removeFolderButton1.setText(_translate("MainWindow", "Remove"))
        self.folderName1.setText(_translate("MainWindow", "Voice command(Name)"))
        self.folderPath1.setText(_translate("MainWindow", "Folder to open(Path)"))
        self.folderPathLabel.setText(_translate("MainWindow", "Folder to open(Path)"))
        self.folderNameLabel.setText(_translate("MainWindow", "Voice command(Name)"))
        self.browsefolderButton1.setText(_translate("MainWindow", "Browse"))
        self.browseFolderButtonLabel.setText(_translate("MainWindow", "Tap to browse path"))
        self.removeAllFoldersButton.setText(_translate("MainWindow", "Remove all"))
        self.addManyFoldersButton.setText(_translate("MainWindow", "Add many Folders"))
        self.Pages.setTabText(self.Pages.indexOf(self.folderstoOpen), _translate("MainWindow", "Folders to open"))
