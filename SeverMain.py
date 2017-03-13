'''
Created on 2016年10月3日

@author: Anshare_LY
'''
import sys  
from PyQt5 import *
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWidgets import *



class MainWindow(QMainWindow):
     
    def __init__(self, parent = None):
        super().__init__(parent)
        #显示暂存量
        self.name_input="安 夏"
        self.WindowsTitle="安夏电子席卡   ——V 1.3.2"
        PictureResource="AXLogo.png"
        self.Fort_color_R=Qt.black
        self.BG_color_R=Qt.white
        #初始化显示暂存状态
        self.font=None
        self.Fort_color=None
        self.BG_color=None
        #关于图片
        self.DisplayPicture=QPixmap(PictureResource)#读取图片 AXLogo.png
        self.MDP_Zoom_R=1
        self.MDP_Rote_R=0
        self.MDP_Opacity_R=0
        self.MDP_Move_W=0
        self.MDP_Move_H=0
        #关于字体
        self.font=None
        self.font_R0="华文新魏"
        self.font_R1=130
        self.font_R2=-1
        self.font_R3=5
        self.font_R4=50
        self.font_R5=0
        self.font_R6=0
        self.font_R7=0
        self.font_R8=0
        self.font_R9=0
        self.Font_Opacity=1
        self.Font_Move_W=0
        self.Font_Move_H=0
        
        
        self.initUI()
    # 控制面板部分
    def Group1(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #界面编程
        hbox = QHBoxLayout()
        row = 0
        gridLayout = QGridLayout()
        gridLayout.addWidget(QLabel("名字输入:"), row, 0)
        Name_Input_button = QPushButton("文字设置")
        gridLayout.addWidget(Name_Input_button, row, 1)
        Name_Input_button.clicked.connect(self.Set_Name)
        
        gridLayout.addWidget(QLabel("显示设置:"), row, 2)
        Fort_Set_Button = QPushButton("字体设置")
        gridLayout.addWidget(Fort_Set_Button, row, 3)
        Fort_Set_Button.clicked.connect(self.onFontEidt)
        
        Font_ColorSet_Button = QPushButton("颜色设置")
        gridLayout.addWidget(Font_ColorSet_Button, row, 4)
        Font_ColorSet_Button.clicked.connect(self.OnFort_Color)
        
        BGPicture_Set_Button = QPushButton("背景设置")
        gridLayout.addWidget(BGPicture_Set_Button, row, 5)
        BGPicture_Set_Button.clicked.connect(self.onPictureEidt)
        
        row = row + 1
        self.Name_Input_Lable=QLabel("请设置名字")
        gridLayout.addWidget(self.Name_Input_Lable, row, 1)
        self.Name_Input_Lable.setAlignment(Qt.AlignCenter)
        
        self.Fort_Lable=QLabel(" ")
        gridLayout.addWidget(self.Fort_Lable, row, 3)
        self.Fort_Lable.setAlignment(Qt.AlignCenter)
        
        self.Font_color_Lable=QLabel(" ")
        gridLayout.addWidget(self.Font_color_Lable, row, 4)
        self.Font_color_Lable.setAlignment(Qt.AlignCenter)
        
        self.PIC_Lable=QLabel("剪裁需要的图片")
        gridLayout.addWidget(self.PIC_Lable, row, 5)
        self.PIC_Lable.setAlignment(Qt.AlignCenter)
                   
        hbox.addLayout(gridLayout)
        
        group.setLayout(hbox)
        return group 
    # 模拟显示部分
    def Group2(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #编写显示内容
        hbox = QHBoxLayout()#垂直布局
        QGW=QGraphicsView()#控件
        QGP=QGraphicsScene()#控件
        QGW.setAlignment(Qt.AlignCenter)#居中
        QGP.setBackgroundBrush(QColor("#ece8e4"))
        #新的版本
        self.screen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸 
        QGP.setSceneRect(0,0,self.screen.width(),self.screen.height())
        #加载图片
        self.BGPIC_NameDisPlay=self.DisplayPicture #读取图片 AXLogo.png
        self.QGBGPIC=QGraphicsPixmapItem()#定义一个图片项目
        self.QGBGPIC.setPixmap(self.BGPIC_NameDisPlay)#设置图片
        self.QGBGPIC.setOpacity(0)#设置透明度
        #缩放控制
        #BGPICScale_H=float(self.screen.height()/self.BGPIC_NameDisPlay.height())
        #BGPICScale_W=float(self.screen.width()/self.BGPIC_NameDisPlay.width())
        #if BGPICScale_H>BGPICScale_W : BGPICScale=BGPICScale_H
        #else : BGPICScale=BGPICScale_W
        #if BGPICScale > 1 : BGPICScale=1
        #self.QGBGPIC.setScale(BGPICScale)#缩放
        #self.QGBGPIC.setPos(self.screen.width()/2-self.BGPIC_NameDisPlay.width()*(self.QGBGPIC.scale())/2,self.screen.height()/2-self.BGPIC_NameDisPlay.height()*(self.QGBGPIC.scale())/2)
        #加载文字
        self.QGNAMEDP=QGraphicsTextItem()
        self.QGNAMEDP.setPlainText("电子席卡 内容预览显示区域")
        #字体横向居中
        document = self.QGNAMEDP.document()
        option = document.defaultTextOption()
        option.setAlignment(Qt.AlignCenter)
        document.setDefaultTextOption(option)
        #设置文字初始化
        self.QGNAMEDP.setFont(QFont(self.font_R0,50))#设置字体
        self.QGNAMEDP.setTextWidth(self.screen.width())#设置文字宽度
        self.QGNAMEDP.setDefaultTextColor(QColor(self.Fort_color_R))#设置颜色
        self.QGNAMEDP.setPos(0,self.screen.height()/2-25)

        #添加控件
        QGP.addItem(self.QGBGPIC)
        QGP.addItem(self.QGNAMEDP)
        QGP.addRect(0,0,self.screen.width(),self.screen.height(), Qt.red)#添加边框
        #添加显示
        QGW.scale(QGW.width()/(1.5*QGP.width()),QGW.width()/(1.5*QGP.width()))
        QGW.setScene(QGP)
        hbox.addWidget(QGW)
        group.setLayout(hbox)
        
        return group 
    # 控制面板部分
    def Group3(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #界面编程
        hbox = QHBoxLayout()
        row = 0
        gridLayout = QGridLayout()
        Help_button = QPushButton("帮助")
        gridLayout.addWidget(Help_button, row, 0)
        Help_button.clicked.connect(self.UseHelp)
        row=row+1
        About_Button = QPushButton("关于")
        gridLayout.addWidget(About_Button, row, 0)
        About_Button.clicked.connect(self.about)
                   
        hbox.addLayout(gridLayout)
        
        group.setLayout(hbox)
        return group
       
    #初始化界面
    def initUI(self):
        self.leftContentTabWidget = QtWidgets.QTabWidget()
        self.rightContentTabWidget = QtWidgets.QTabWidget()
        self.addWidget(self.leftContentTabWidget)
        self.addWidget(self.rightContentTabWidget)
        self.setOrientation(QtCore.Qt.Horizontal)
        self.setStretchFactor(1,13)
        
        self.rightContentTabWidget.setTabsClosable(True)
        '''
        
        self.mainarea=QWidget()
        self.mainVertLayout = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        #上层预览部分
        self.vlayout2.addWidget(self.Group2("预览"))
        self.mainVertLayout.addLayout(self.vlayout2)
        #下层控制面板及帮助部分
        self.boxLayout = QHBoxLayout()
        self.boxLayout.addWidget(self.Group1("控制面板"))
        self.boxLayout.addWidget(self.Group3("帮助"))
        self.boxLayout.addStretch()
        #全屏显示按钮
        All_Display = QPushButton("全屏\n显示")
        self.boxLayout.addWidget(All_Display)
        All_Display.clicked.connect(self.OnWindowDisplay)
        #主要布局
        self.mainVertLayout.addLayout(self.boxLayout)
        self.mainarea.setLayout(self.mainVertLayout)
        self.setCentralWidget(self.mainarea)
        '''
        #更改风格
        self.changeStyle("Fusion")
        #固定大小
        self.resize(800,480) 
        #设置居中并全屏显示
        self.center()
        #设置显示模式
        #self.showFullScreen()  #全屏幕显示
        #self.showMaximized() #最大化显示        
        self.setWindowTitle(self.WindowsTitle) 
        self.setWindowIcon(QIcon("AXLogo.png")) # 图标显示 
        self.show()
        
    #居中
    def center(self):
        '''屏幕居中函数'''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def OnOK(self): 
        pass
        
    #退出按钮
    def onOkClicked(self):
        self.OnOK()
        self.accept() 
        
    #图片编辑
    def onPictureEidt(self):
        self.PICE_APP_OUT=ImageViewer(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H)
        #self.PICE_APP_OUT.Set_PE_Picture(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H)
        Flag=self.PICE_APP_OUT.exec_()
        #传递当前图片参数
        if Flag :
            self.Get_QGPicture(self.PICE_APP_OUT.getImage(),self.PICE_APP_OUT.getZoom_R(),self.PICE_APP_OUT.getRote_R(),self.PICE_APP_OUT.getOpacity(),self.PICE_APP_OUT.getMove_W(),self.PICE_APP_OUT.getMove_H())#接收返回图片
        self.OnAction()
        
    #字体编辑
    def onFontEidt(self):
        self.FE_APP_OUT=FontViewer(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H,self.name_input,self.font,self.Fort_color_R,self.Font_Opacity,self.Font_Move_W,self.Font_Move_H)
        Flag=self.FE_APP_OUT.exec_()
        #传递当前字体设置参数
        if Flag :
            self.Get_Font_Set(self.FE_APP_OUT.getFont(),self.FE_APP_OUT.getFontOpacity(),self.FE_APP_OUT.getFontMove_W(),self.FE_APP_OUT.getFontMove_H())#接收返回图片
        self.OnAction()
    #编辑文本
    def Set_Name(self):
        self.name_input_set, ok = QInputDialog.getText(self, "请输入文字：", "输入文字：", QLineEdit.Normal, QDir.home().dirName())
        if ok and self.name_input_set:
            self.name_input=self.name_input_set
            self.Name_Input_Lable.setText(self.name_input)
            self.OnAction()           
    #字体对话框 取字体
    def OnsetFont(self):
        self.font, ok = QFontDialog.getFont(QFont(self.font_R0,self.font_R1))
        if ok:
            FontElements=str(self.font.key())
            self.font_R=FontElements.split(',')
            #分离字体属性
            self.font_R0=self.font_R[0]
            self.font_R1=int(self.font_R[1])
            self.font_R2=int(self.font_R[2])
            self.font_R3=int(self.font_R[3])
            self.font_R4=int(self.font_R[4])
            self.font_R5=int(self.font_R[5])
            self.font_R6=int(self.font_R[6])
            self.font_R7=int(self.font_R[7])
            self.font_R8=int(self.font_R[8])
            self.font_R9=int(self.font_R[9])
            self.Fort_Lable.setText("%s %d" %(self.font_R0,self.font_R1))
            self.OnAction()
            
    #设置字体颜色       
    def OnFort_Color(self):
        self.Fort_color = QColorDialog.getColor(self.Fort_color_R, self, "选择字体颜色")
        self.Font_color_Lable.setText(self.Fort_color.name())
        self.Font_color_Lable.setPalette(QPalette(self.Fort_color))
        self.Font_color_Lable.setAutoFillBackground(True)
        self.Fort_color_R=self.Fort_color
        self.OnAction()
    #设置背景颜色
    def OnBG_Color(self):
        self.BG_color = QColorDialog.getColor(self.BG_color_R, self, "选择背景颜色")
        self.BG_color_Lable.setText(self.BG_color.name())
        self.BG_color_Lable.setPalette(QPalette(self.BG_color))
        self.BG_color_Lable.setAutoFillBackground(True)
        self.BG_color_R=self.BG_color
        pass
    
    #执行显示
    def OnAction(self):
        
        if self.name_input != "" :
            #显示文字
            self.QGNAMEDP.setPlainText(self.name_input)
            #字体颜色判断
            if self.Fort_color != None :
                self.QGNAMEDP.setDefaultTextColor(QColor(self.Fort_color))
            #字体属性判断
            if self.font != None:
                self.QGNAMEDP.setFont(self.font)
                self.QGNAMEDP.setOpacity(self.Font_Opacity)
                
            self.QGNAMEDP.setPos(self.Font_Move_W,self.screen.height()/2-self.font_R1/2+self.Font_Move_H)
        else : #若没有显示文字 则显示提示
            self.QGNAMEDP.setPlainText("请完成所有设置！")
    #全屏显示部分
    def OnWindowDisplay(self):
        self.Display_APP_OUT=DisplayWindow()      
        self.Display_APP_OUT.SetFullScreenDisPlay(self.name_input, self.Fort_color, self.BG_color, self.font,self.DisplayPicture,self.MDP_Zoom_R,self.MDP_Rote_R,self.MDP_Opacity_R,self.MDP_Move_W,self.MDP_Move_H,self.Font_Opacity,self.Font_Move_W,self.Font_Move_H)
        self.Display_APP_OUT.exec_()
        
    def Get_QGPicture(self,QGImage,QGImage_Zoom_R,QGImage_Rote_R,QGImage_Opacity_R,QGImage_Move_W,QGImage_Move_H):
        #获得图片相关参数
        self.DisplayPicture=QGImage
        self.MDP_Zoom_R=QGImage_Zoom_R
        self.MDP_Rote_R=QGImage_Rote_R
        self.MDP_Opacity_R=QGImage_Opacity_R
        self.MDP_Move_W=QGImage_Move_W
        self.MDP_Move_H=QGImage_Move_H
        
        #读取图片
        self.QGBGPIC.setPixmap(self.DisplayPicture)
        #设置中心偏移
        self.QGBGPIC.setOffset(-float(self.DisplayPicture.width()/2),-float(self.DisplayPicture.height()/2))
        #设置放大
        self.QGBGPIC.setScale(QGImage_Zoom_R)
        #设置旋转
        self.QGBGPIC.setRotation(QGImage_Rote_R)
        #设置透明度
        self.QGBGPIC.setOpacity(QGImage_Opacity_R)
        #设置位置
        self.QGBGPIC.setPos(self.screen.width()/2+QGImage_Move_W,self.screen.height()/2+QGImage_Move_H)
    
    def Get_Font_Set(self,FE_Font,FE_Font_Opacity,FE_Font_Move_W,FE_Font_Move_H):
        #获得字体相关参数
        self.font=FE_Font
        FontElements=str(self.font.key())
        self.font_R=FontElements.split(',')
        #分离字体属性
        self.font_R0=self.font_R[0]
        self.font_R1=int(self.font_R[1])
        self.font_R2=int(self.font_R[2])
        self.font_R3=int(self.font_R[3])
        self.font_R4=int(self.font_R[4])
        self.font_R5=int(self.font_R[5])
        self.font_R6=int(self.font_R[6])
        self.font_R7=int(self.font_R[7])
        self.font_R8=int(self.font_R[8])
        self.font_R9=int(self.font_R[9])
        #透明度 横向位移 纵向位移
        self.Font_Opacity=float(FE_Font_Opacity)
        self.Font_Move_W=int(FE_Font_Move_W)
        self.Font_Move_H=int(FE_Font_Move_H)
        self.Fort_Lable.setText("%s %d" %(self.font_R0,self.font_R1))
        
    def about(self):
        QMessageBox.about(self, "关于南京安夏电子有限公司",
                "<p><b>南京安夏电子科技有限公司</b>是一家集信息系统软硬件研发、生产、销售和服务为一体的高科技创新企业。  "
                "公司由南京理工大学扶持成立，并获得南京市属金融投资平台紫金投资集团旗下的紫金科创的风险投资。"
                " 安夏科技位于南京理工大学科技园，公司拥有一流的软件开发和产品设计团队，专注于研发具有自主知识产权的软硬件产品。"
                " 公司以年轻的科技研发人员为主体，研发中心拥有专业技术人员20多人，其中包括博士2人，硕士3人，本科以上学历100%。"
                " 公司目前拥有两项国家发明专利与四项国家软件产品著作权。公司以“用心服务，共创价值”为核心理念，"
                "致力于为客户提供技术先进的信息化和电子商务解决方案，同时提供优质的咨询、培训和运维服务。</p>")       
    def UseHelp(self):
        QMessageBox.about(self, "关于安夏电子席卡",
                "<p><b>安夏电子席卡</b>是一款绿色环保，且高效的会议席卡系统。<br>"
                "<b>使用方法：</b><br>"
                "1.先设置录入要显示的名子<br>"
                "2.设置要显示的名子的字体，具体设置字体，透明度，位置要素<br>"
                "3.设置要显示的名子的文字颜色，默认为黑色<br>"
                "4.设置背景图片，可以使用适应窗口快速设置按钮完成设置<br>  另外可以使用魔板进行快速设置</p>"
                "<p>若有疑问请联系<b> 安夏电子科技有限公司 </b><br>"
                "<b>电话：</b> 4008017129<br>"
                "<b>网址：</b><a href='www.anshare.com.cn'>www.anshare.com.cn</a></p>")    
    # 改变显示风格    
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
    def changePalette(self):
            QApplication.setPalette(QApplication.style().standardPalette())
    