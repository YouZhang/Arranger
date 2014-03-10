# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\PyQt_WorkSpace\test_UI.ui'
#
# Created: Tue Feb 11 13:33:15 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Arrange_top import Arranger

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 600, 700))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.input = QtGui.QWidget()
        self.input.setObjectName(_fromUtf8("input"))
        self.TabEdit = QtGui.QTextEdit(self.input)
        self.TabEdit.setGeometry(QtCore.QRect(30, 460, 490, 100))
        self.TabEdit.setObjectName(_fromUtf8("TabEdit"))
        self.Result = QtGui.QTextEdit(self.input)
        self.Result.setGeometry(QtCore.QRect(30, 30, 490, 400))
        self.Result.setObjectName(_fromUtf8("Result"))
        self.BtnArrange = QtGui.QPushButton(self.input)
        self.BtnArrange.setGeometry(QtCore.QRect(520, 500, 75, 23))
        self.BtnArrange.setObjectName(_fromUtf8("BtnArrange"))
        self.tabWidget.addTab(self.input, _fromUtf8(""))
        self.download = QtGui.QWidget()
        self.download.setObjectName(_fromUtf8("download"))
        self.Song = QtGui.QLineEdit(self.download)
        self.Song.setGeometry(QtCore.QRect(110, 60, 113, 20))
        self.Song.setObjectName(_fromUtf8("Song"))
        self.BtnSearch = QtGui.QPushButton(self.download)
        self.BtnSearch.setGeometry(QtCore.QRect(260, 60, 75, 23))
        self.BtnSearch.setObjectName(_fromUtf8("BtnSearch"))
        self.TabResult = QtGui.QTextEdit(self.download)
        self.TabResult.setGeometry(QtCore.QRect(80, 140, 601, 141))
        self.TabResult.setObjectName(_fromUtf8("TabResult"))
        self.tabWidget.addTab(self.download, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_midi_file = QtGui.QAction(MainWindow)
        self.actionOpen_midi_file.setObjectName(_fromUtf8("actionOpen_midi_file"))
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionOpen_midi_file)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Arranger", None))
        self.BtnArrange.setText(_translate("MainWindow", "Arrange", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input), _translate("MainWindow", "input", None))
        self.BtnSearch.setText(_translate("MainWindow", "Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.download), _translate("MainWindow", "download", None))
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.actionOpen.setText(_translate("MainWindow", "open tab file", None))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open tab file", None))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionOpen_midi_file.setText(_translate("MainWindow", "open midi file", None))

        #TODO: signal and cao
        self.ActionEvent();
        self.ObjectEvent();

    def ActionEvent(self):
        self.actionOpen.triggered.connect(self.ImportTab);


    def ObjectEvent(self):
        self.BtnArrange.clicked.connect(self.ShowResult);
        pass

    def ImportTab(self):
        fname = QtGui.QFileDialog.getOpenFileName(self.centralwidget,'open file','/home');
        fd = open(fname,'r');
        with fd:
            data = fd.read();
            self.TabEdit.setText(data);

    def ShowResult(self):
        # data = self.TabEdit()
        result = self.TabEdit.toPlainText()
        chord_name_list,chord_press_list,section = Arranger('C',str(result));
        # tab_str = '          '.join(chord_name_list);
        # tab_press =
        for i in range(len(chord_name_list)):
            if (i == 0):
                self.Result.setText(section[i]);
                self.Result.append(_fromUtf8(chord_name_list[i]));
                self.Result.append(_fromUtf8(chord_press_list[i]));
            else:
                self.Result.append(_fromUtf8(section[i]));
                self.Result.append(_fromUtf8(chord_name_list[i]));
                self.Result.append(_fromUtf8(chord_press_list[i]));


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

