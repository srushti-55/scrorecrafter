# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(519, 472)
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Scanner))
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"font: 500 11pt \"Ubuntu\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"font: 670 22pt \"Ubuntu Sans\";")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.select_file_widget = QWidget(self.centralwidget)
        self.select_file_widget.setObjectName(u"select_file_widget")
        self.horizontalLayout = QHBoxLayout(self.select_file_widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, -1)
        self.file_name = QLabel(self.select_file_widget)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.file_name)

        self.select_file_btn = QPushButton(self.select_file_widget)
        self.select_file_btn.setObjectName(u"select_file_btn")
        self.select_file_btn.setMaximumSize(QSize(110, 16777215))
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.select_file_btn.setIcon(icon1)

        self.horizontalLayout.addWidget(self.select_file_btn)

        self.process_pdf_btn = QPushButton(self.select_file_widget)
        self.process_pdf_btn.setObjectName(u"process_pdf_btn")
        self.process_pdf_btn.setMaximumSize(QSize(120, 16777215))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentProperties))
        self.process_pdf_btn.setIcon(icon2)

        self.horizontalLayout.addWidget(self.process_pdf_btn)


        self.verticalLayout.addWidget(self.select_file_widget)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.instructions_label = QTextBrowser(self.centralwidget)
        self.instructions_label.setObjectName(u"instructions_label")

        self.verticalLayout.addWidget(self.instructions_label)

        self.course_select_widget = QWidget(self.centralwidget)
        self.course_select_widget.setObjectName(u"course_select_widget")
        self.verticalLayout_8 = QVBoxLayout(self.course_select_widget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 9, 0, 0)
        self.select_course_label = QLabel(self.course_select_widget)
        self.select_course_label.setObjectName(u"select_course_label")
        self.select_course_label.setStyleSheet(u"font: 500 14pt \"Ubuntu\";")
        self.select_course_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_8.addWidget(self.select_course_label)

        self.course_container_widget = QWidget(self.course_select_widget)
        self.course_container_widget.setObjectName(u"course_container_widget")
        self.verticalLayout_10 = QVBoxLayout(self.course_container_widget)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 3, 0, 0)
        self.scroll_area = QScrollArea(self.course_container_widget)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setWidgetResizable(True)
        self.scrollarea_widget = QWidget()
        self.scrollarea_widget.setObjectName(u"scrollarea_widget")
        self.scrollarea_widget.setGeometry(QRect(0, 0, 499, 68))
        self.verticalLayout_11 = QVBoxLayout(self.scrollarea_widget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.scroll_area.setWidget(self.scrollarea_widget)

        self.verticalLayout_10.addWidget(self.scroll_area)


        self.verticalLayout_8.addWidget(self.course_container_widget)

        self.export_btn_widget = QWidget(self.course_select_widget)
        self.export_btn_widget.setObjectName(u"export_btn_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.export_btn_widget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 9, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.export_as_docx_btn = QPushButton(self.export_btn_widget)
        self.export_as_docx_btn.setObjectName(u"export_as_docx_btn")
        self.export_as_docx_btn.setMinimumSize(QSize(0, 30))
        self.export_as_docx_btn.setMaximumSize(QSize(150, 16777215))
        icon3 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentSave))
        self.export_as_docx_btn.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.export_as_docx_btn)


        self.verticalLayout_8.addWidget(self.export_btn_widget)


        self.verticalLayout.addWidget(self.course_select_widget)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ScoreCraftr", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"ScoreCraftr", None))
        self.file_name.setText(QCoreApplication.translate("MainWindow", u"File: no file selected...", None))
        self.select_file_btn.setText(QCoreApplication.translate("MainWindow", u"Select PDF", None))
#if QT_CONFIG(shortcut)
        self.select_file_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.process_pdf_btn.setText(QCoreApplication.translate("MainWindow", u"Process PDF", None))
#if QT_CONFIG(shortcut)
        self.process_pdf_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.instructions_label.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:500; font-style:normal;\">\n"
"<h3 style=\" margin-top:14px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:large; font-weight:700;\">How to Use This App</span></h3>\n"
"<ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\">\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Select PDF File</span><br />Click on the <sp"
                        "an style=\" font-weight:700;\">&quot;Select PDF&quot;</span> button to upload your PDF document.</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Process the PDF</span><br />After selecting the file, click <span style=\" font-weight:700;\">&quot;Process PDF&quot;</span> to extract the course data from the PDF.</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Choose the Data You Need</span><br />Once the data is extracted, use the <span style=\" font-weight:700;\">selection panel</span> to pick the specific course information you want to export.</li>\n"
"<li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:700;\">Export to DOCX</span><br />Click the <span style=\" font-weight:700;\">"
                        "&quot;Export as DOCX&quot;</span> button to download your selected data as a Word document.</li></ol></body></html>", None))
        self.select_course_label.setText(QCoreApplication.translate("MainWindow", u"Select Course", None))
        self.export_as_docx_btn.setText(QCoreApplication.translate("MainWindow", u"Export as DOCX", None))
#if QT_CONFIG(shortcut)
        self.export_as_docx_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

