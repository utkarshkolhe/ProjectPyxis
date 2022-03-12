import sys
from PyQt5 import QtCore,QtGui,QtWidgets



USER=0
SYS=1

BUBBLES={USER:"#a9a9a9",SYS:"#a5d6a7"}
TRANSLATE_USER={USER:QtCore.QPoint(20, 0),SYS:QtCore.QPoint(0, 0)}

BUBBLES_PAD=QtCore.QMargins(15,5,35,5)
TEXT_PAD=QtCore.QMargins(25,15,45,15)


class MessageChoice(QtWidgets.QStyledItemDelegate):
    _font=None
    def paint(self,painter,option,index):
        painter.save()
        user,text=index.model().data(index,QtCore.Qt.DisplayRole)
        user_translate=TRANSLATE_USER[user]
        painter.translate(user_translate)
        bubble_rectangle=option.rect.marginsRemoved(BUBBLES_PAD)
        text_rectangle=option.rect.marginsRemoved(TEXT_PAD)
        painter.setPen(QtCore.Qt.NoPen)
        colors=QtGui.QColor(BUBBLES[user])
        painter.setBrush(colors)
        painter.drawRoundedRect(bubble_rectangle,10,10)
        if user==USER:
            set_text=bubble_rectangle.topRight()
        else:
            set_text=bubble_rectangle.topLeft()
        painter.drawPolygon(set_text+QtCore.QPoint(-20,0),set_text+QtCore.QPoint(20,0),set_text+QtCore.QPoint(0,20))
        text_option=QtGui.QTextOption()
        text_option.setWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        docs=QtGui.QTextDocument(text)
        docs.setTextWidth(text_rectangle.width())
        docs.setDefaultTextOption(text_option)
        docs.setDocumentMargin(0)
        painter.translate(text_rectangle.topLeft())
        docs.drawContents(painter)
        painter.restore()
    def sizeHint(self,option,index):
        _,text=index.model().data(index,QtCore.Qt.DisplayRole)
        rectangular_text=option.rect.marginsRemoved(TEXT_PAD)
        text_option=QtGui.QTextOption()
        text_option.setWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        docs=QtGui.QTextDocument(text)
        docs.setTextWidth(rectangular_text.width())
        docs.setDefaultTextOption(text_option)
        docs.setDocumentMargin(0)
        rectangular_text.setHeight(docs.size().height())
        rectangular_text=rectangular_text.marginsAdded(TEXT_PAD)
        return rectangular_text.size()


class Messages(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(Messages, self).__init__(*args, **kwargs)
        self.messages = []
    
    def data(self,index,role):
        if role==QtCore.Qt.DisplayRole:
            return self.messages[index.row()]
    def setData(self,index,role,value):
        self._size[index.row()]

    def rowCount(self,index):
        return len(self.messages)
    def add_message(self,who,text):
        if text:
            self.messages.append((who,text))
            self.layoutChanged.emit()

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        l=QtWidgets.QVBoxLayout()
        self.input_msg=QtWidgets.QLineEdit("")
        self.button1=QtWidgets.QPushButton('User')
        self.button2=QtWidgets.QPushButton('System')
        self.messages_entered=QtWidgets.QListView()
        self.messages_entered.setResizeMode(QtWidgets.QListView.Adjust)
        self.messages_entered.setItemDelegate(MessageChoice())
        self.model=Messages()
        self.messages_entered.setModel(self.model)
        self.button1.pressed.connect(self.message_to)
        self.button2.pressed.connect(self.message_from)
        l.addWidget(self.messages_entered)
        l.addWidget(self.input_msg)
        l.addWidget(self.button1)
        l.addWidget(self.button2)
        self.widget=QtWidgets.QWidget()
        self.widget.setLayout(l)
        self.setCentralWidget(self.widget)

    def resizeEvent(self,e):
        self.model.layoutChanged.emit()
    def message_to(self):
        self.model.add_message(USER,self.input_msg.text())


    def message_from(self):
        self.model.add_message(SYS,self.input_msg.text())

    




app=QtWidgets.QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()


