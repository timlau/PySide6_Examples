# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'videomode.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_VideoMode(object):
    def setupUi(self, VideoMode):
        if not VideoMode.objectName():
            VideoMode.setObjectName(u"VideoMode")
        VideoMode.resize(400, 300)
        self.gridLayout = QGridLayout(VideoMode)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ok = QPushButton(VideoMode)
        self.ok.setObjectName(u"ok")

        self.gridLayout.addWidget(self.ok, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.content = QGroupBox(VideoMode)
        self.content.setObjectName(u"content")
        self.content.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.formLayout = QFormLayout(self.content)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.content)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.width = QLineEdit(self.content)
        self.width.setObjectName(u"width")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.width)

        self.label_2 = QLabel(self.content)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.height = QLineEdit(self.content)
        self.height.setObjectName(u"height")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.height)

        self.label_3 = QLabel(self.content)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.fps = QLineEdit(self.content)
        self.fps.setObjectName(u"fps")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.fps)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.content, 0, 0, 1, 3)


        self.retranslateUi(VideoMode)

        QMetaObject.connectSlotsByName(VideoMode)
    # setupUi

    def retranslateUi(self, VideoMode):
        VideoMode.setWindowTitle(QCoreApplication.translate("VideoMode", u"Video Mode", None))
        self.ok.setText(QCoreApplication.translate("VideoMode", u"Ok", None))
        self.content.setTitle(QCoreApplication.translate("VideoMode", u"Video Mode", None))
        self.label.setText(QCoreApplication.translate("VideoMode", u"Width", None))
        self.label_2.setText(QCoreApplication.translate("VideoMode", u"Height", None))
        self.label_3.setText(QCoreApplication.translate("VideoMode", u"FPS", None))
    # retranslateUi

