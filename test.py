'''
Created on 2016.07.15

@author: Anshare_LY
'''

import sys  
from PyQt5 import QtWidgets,QtCore, QtGui
  
class MainWindow(QtWidgets.QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
    
    def Group1(self, grpname):
        group = QtWidgets.QGroupBox(grpname)
        group.setCheckable(False)
        
        hbox = QtWidgets.QHBoxLayout()
        
        row = 0
        gridLayout = QtWidgets.QGridLayout()
        
        gridLayout.addWidget(QtWidgets.QLabel("卢加文的昵称是什么:"), row, 0)
        combo = QtWidgets.QComboBox()
        combo.addItem("小闹闹")
        combo.addItem("小吃货")
        combo.addItem("睡神")
        combo.addItem("小乖乖")
        combo.addItem("小美美")
        combo.addItem("……")
        gridLayout.addWidget(combo, row, 1)
        gridLayout.addWidget(QtWidgets.QLabel("     嘿嘿嘿  有点可爱呦~"), row, 2)
        row = row + 2
        gridLayout.addWidget(QtWidgets.QLabel("你爱什么呢:"), row, 0)
        checkbox1 = QtWidgets.QCheckBox("爱刘裕")
        gridLayout.addWidget(checkbox1, row, 1)
        row = row + 1
        
        checkbox2 = QtWidgets.QCheckBox("爱生活")
        gridLayout.addWidget(checkbox2, row, 1)
        row = row + 1
        
        checkbox3 = QtWidgets.QCheckBox("爱美食")
        gridLayout.addWidget(checkbox3, row, 1)
        row = row + 1
        
        checkbox4 = QtWidgets.QCheckBox("爱偷懒")
        gridLayout.addWidget(checkbox4, row, 1)
        row = row + 1
        
        checkbox5 = QtWidgets.QCheckBox("爱追剧")
        gridLayout.addWidget(checkbox5, row, 1)
        row = row + 1
            
        hbox.addLayout(gridLayout)
        hbox.addStretch()
        group.setLayout(hbox)
        return group
    
    
    def Group2(self, grpname):
        group = QtWidgets.QGroupBox(grpname)
        group.setCheckable(False)
        
        hbox = QtWidgets.QHBoxLayout()
        
        row = 0
        gridLayout = QtWidgets.QGridLayout()
        
        gridLayout.addWidget(QtWidgets.QLabel("每天玩耍时间是:"), row, 0)
        time_start = QtWidgets.QLineEdit()
        time_start.setText("7:00")
        gridLayout.addWidget(time_start, row, 1)
        gridLayout.addWidget(QtWidgets.QLabel("  ~  "), row, 2)
        time_stop = QtWidgets.QLineEdit()
        time_stop.setText("22:00")
        gridLayout.addWidget(time_stop, row, 3)
        gridLayout.addWidget(QtWidgets.QLabel("  嘿嘿 有点夸张~~"), row, 4)
        row = row + 1
        
        gridLayout.addWidget(QtWidgets.QLabel("喜欢的事情:"), row, 0)
        checkbox1 = QtWidgets.QCheckBox("看电影")
        gridLayout.addWidget(checkbox1, row, 1)
        row = row + 1
        
        checkbox2 = QtWidgets.QCheckBox("玩游戏")
        gridLayout.addWidget(checkbox2, row, 1)
        row = row + 1
        
        checkbox3 = QtWidgets.QCheckBox("去逛街")
        gridLayout.addWidget(checkbox3, row, 1)
        row = row + 1
        
        checkbox4 = QtWidgets.QCheckBox("刷知乎")
        gridLayout.addWidget(checkbox4, row, 1)
        row = row + 1
        
        checkbox5 = QtWidgets.QCheckBox("聊聊天")
        gridLayout.addWidget(checkbox5, row, 1)
        row = row + 2
        
        gridLayout.addWidget(QtWidgets.QLabel("你的愿望是:"), row, 0)
        LJW_wish = QtWidgets.QLineEdit()
        LJW_wish.setText("再来几个愿望吧……")
        gridLayout.addWidget(LJW_wish, row, 1)        
        row = row + 1
                    
        hbox.addLayout(gridLayout)
        hbox.addStretch()
        group.setLayout(hbox)
        return group    
         
    def initUI(self):              
        
        
        self.mainVertLayout = QtWidgets.QVBoxLayout()

        self.vlayout = QtWidgets.QVBoxLayout()
        self.vlayout.addWidget(self.Group1("选我 选我 快选我~"))
        self.vlayout.addWidget(self.Group2("我们一起来玩耍~"))
        self.vlayout.addStretch()
        self.mainVertLayout.addLayout(self.vlayout)
       
        self.boxLayout = QtWidgets.QHBoxLayout()
        self.boxLayout.addStretch()
                
        close = QtWidgets.QPushButton("关闭")
        self.boxLayout.addWidget(close)
        close.clicked.connect(self.onOkClicked)
        
        self.mainVertLayout.addLayout(self.boxLayout)
        
        self.setLayout(self.mainVertLayout)
        self.resize(640, 480)
        self.center() 
        self.setWindowTitle('I Love You !')   
        self.show()
         
         
    def center(self):
         
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
            
    
    def OnOK(self): 
        pass
        
    def onOkClicked(self):
        self.OnOK()
        self.accept()        
         
if __name__ == '__main__':
     
    app = QtWidgets.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())