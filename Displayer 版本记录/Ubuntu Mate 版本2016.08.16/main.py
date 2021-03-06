'''
Created on 2016.07.15
@author: Anshare_LY
'''
import sys  
from PyQt5 import *
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWidgets import *

NULL=0;

class MainWindow(QMainWindow):
     
    def __init__(self, parent = None):
        super().__init__(parent)
        #显示暂存量
        self.name_input=""
        self.Fort_color_R=Qt.black
        self.BG_color_R=Qt.white
        self.font_R0="Noto Sans Mono CJK SC"
        self.font_R1=130
        self.font_R2=-1
        self.font_R3=5
        self.font_R4=50
        self.font_R5=0
        self.font_R6=0
        self.font_R7=0
        self.font_R8=0
        self.font_R9=0
        #关于图片
        self.DisplayPicture=None
        self.MDP_Zoom_R=1
        self.MDP_Rote_R=0
        self.MDP_Opacity_R=1
        self.MDP_Move_W=0
        self.MDP_Move_H=0
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
        Fort_Set_Button.clicked.connect(self.OnsetFont)
        
        Font_ColorSet_Button = QPushButton("颜色设置")
        gridLayout.addWidget(Font_ColorSet_Button, row, 4)
        Font_ColorSet_Button.clicked.connect(self.OnFort_Color)
        
        BGPicture_Set_Button = QPushButton("背景设置")
        gridLayout.addWidget(BGPicture_Set_Button, row, 5)
        BGPicture_Set_Button.clicked.connect(self.onPictureEidt)
        
        row = row + 1
        self.Name_Input_Lable=QLabel("请设置名字")
        gridLayout.addWidget(self.Name_Input_Lable, row, 1)
        
        self.Fort_Lable=QLabel(" ")
        gridLayout.addWidget(self.Fort_Lable, row, 3)
        
        self.Fort_color_Lable=QLabel(" ")
        gridLayout.addWidget(self.Fort_color_Lable, row, 4)
        
        self.PIC_Lable=QLabel("剪裁需要的图片")
        gridLayout.addWidget(self.PIC_Lable, row, 5)           
        hbox.addLayout(gridLayout)
        
        hbox.addStretch()
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
        self.BGPIC_NameDisPlay=QPixmap("/home/anshare/下载/Display/AXLogo.png")#读取图片 AXLogo.png
        self.QGBGPIC=QGraphicsPixmapItem()#定义一个图片项目
        self.QGBGPIC.setPixmap(self.BGPIC_NameDisPlay)#设置图片
        self.QGBGPIC.setOpacity(0)#设置透明度
        #缩放控制
        BGPICScale_H=float(self.screen.height()/self.BGPIC_NameDisPlay.height())
        BGPICScale_W=float(self.screen.width()/self.BGPIC_NameDisPlay.width())
        if BGPICScale_H>BGPICScale_W : BGPICScale=BGPICScale_H
        else : BGPICScale=BGPICScale_W
        if BGPICScale > 1 : BGPICScale=1
        self.QGBGPIC.setScale(BGPICScale)#缩放
        self.QGBGPIC.setPos(self.screen.width()/2-self.BGPIC_NameDisPlay.width()*(self.QGBGPIC.scale())/2,self.screen.height()/2-self.BGPIC_NameDisPlay.height()*(self.QGBGPIC.scale())/2)
        #加载文字
        self.QGNAMEDP=QGraphicsTextItem()
        self.QGNAMEDP.setPlainText("电子席卡 内容预览显示区域")
        #字体横向居中
        document = self.QGNAMEDP.document()
        option = document.defaultTextOption()
        option.setAlignment(Qt.AlignCenter)
        document.setDefaultTextOption(option)
        #设置文字初始化
        self.QGNAMEDP.setFont(QFont(self.font_R0,30))#设置字体
        self.QGNAMEDP.setTextWidth(self.screen.width())#设置文字宽度
        self.QGNAMEDP.setDefaultTextColor(QColor(self.Fort_color_R))#设置颜色
        self.QGNAMEDP.setPos(0,self.screen.height()/2-15)

        #添加控件
        QGP.addItem(self.QGBGPIC)
        QGP.addItem(self.QGNAMEDP)
        QGP.addRect(0,0,self.screen.width(),self.screen.height(), Qt.red)#添加边框
        #添加显示
        QGW.scale(QGW.width()/(2.3*QGP.width()),QGW.width()/(2.3*QGP.width()))
        QGW.setScene(QGP)
        hbox.addWidget(QGW)
        group.setLayout(hbox)
        
        return group    
    #初始化界面
    def initUI(self):              
        
        self.mainarea=QWidget()
        self.mainVertLayout = QVBoxLayout()
        self.vlayout1 = QVBoxLayout()
        self.vlayout1.addWidget(self.Group1("控制面板"))
        self.mainVertLayout.addLayout(self.vlayout1)
        self.vlayout2 = QVBoxLayout()
        self.vlayout2.addWidget(self.Group2("预览"))
        self.mainVertLayout.addLayout(self.vlayout2)

        self.boxLayout = QHBoxLayout()
        self.boxLayout.addStretch()
        #初始化显示暂存状态
        self.font=NULL;
        self.Fort_color=NULL;
        self.BG_color=NULL;
        #全屏显示按钮
        All_Display = QPushButton("全屏显示")
        self.boxLayout.addWidget(All_Display)
        All_Display.clicked.connect(self.OnWindowDisplay)
        #关闭按钮       
        close = QPushButton("关闭")
        #self.boxLayout.addWidget(close)
        close.clicked.connect(QCoreApplication.quit)
        #主要布局
        self.mainVertLayout.addLayout(self.boxLayout)
        self.mainarea.setLayout(self.mainVertLayout)
        self.setCentralWidget(self.mainarea)
        #更改风格
        self.changeStyle("Fusion")
        #设置居中并全屏显示
        self.center() 
        #self.showFullScreen()  #全屏幕显示
        self.showMaximized() #最大化显示
        self.setWindowTitle("安夏电子席卡    ——安夏出品 必出精品") 
        self.setWindowIcon(QIcon("/home/anshare/下载/Display/AXLogo.png")) # 图标显示 
        self.show()
           
    def center(self):
         
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
        self.PICE_APP_OUT=ImageViewer()
        self.PICE_APP_OUT.exec_()
        self.Get_QGPicture(self.PICE_APP_OUT.getImage(),self.PICE_APP_OUT.getZoom_R(),self.PICE_APP_OUT.getRote_R(),self.PICE_APP_OUT.getOpacity(),self.PICE_APP_OUT.getMove_W(),self.PICE_APP_OUT.getMove_H())#接收返回图片
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
            self.Fort_Lable.setText(self.font.key())
            self.font_R=self.Fort_Lable.text().split(',')
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
            self.OnAction()
    
    #设置字体颜色       
    def OnFort_Color(self):
        self.Fort_color = QColorDialog.getColor(self.Fort_color_R, self, "选择字体颜色")
        self.Fort_color_Lable.setText(self.Fort_color.name())
        self.Fort_color_Lable.setPalette(QPalette(self.Fort_color))
        self.Fort_color_Lable.setAutoFillBackground(True)
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
            if self.Fort_color != 0 :
                self.QGNAMEDP.setDefaultTextColor(QColor(self.Fort_color))
            #背景颜色判断    
            if self.BG_color != 0: 
                pass
            #字体属性判断
            if self.font != 0:
                self.QGNAMEDP.setFont(self.font)
            self.QGNAMEDP.setPos(0,self.screen.height()/3-self.font_R1/2)
        else : #若没有显示文字 则显示提示
            self.name_display.setText("请完成所有设置！")
            self.QGNAMEDP.setPlainText("请完成所有设置！")
        pass
    #全屏显示部分
    def OnWindowDisplay(self):
        self.Display_APP_OUT=DisplayWindow()      
        self.Display_APP_OUT.SetFullScreenDisPlay(self.name_input, self.Fort_color, self.BG_color, self.font,self.DisplayPicture,self.MDP_Zoom_R,self.MDP_Rote_R,self.MDP_Opacity_R,self.MDP_Move_W,self.MDP_Move_H)
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
    
    def about(self):
        QMessageBox.about(self, "关于南京安夏电子有限公司",
                "<p><b>南京安夏电子科技有限公司</b>是一家集信息系统软硬件研发、生产、销售和服务为一体的高科技创新企业。  "
                "公司由南京理工大学扶持成立，并获得南京市属金融投资平台紫金投资集团旗下的紫金科创的风险投资。"
                " 安夏科技位于南京理工大学科技园，公司拥有一流的软件开发和产品设计团队，专注于研发具有自主知识产权的软硬件产品。"
                " 公司以年轻的科技研发人员为主体，研发中心拥有专业技术人员20多人，其中包括博士2人，硕士3人，本科以上学历100%。"
                " 公司目前拥有两项国家发明专利与四项国家软件产品著作权。公司以“用心服务，共创价值”为核心理念，"
                "致力于为客户提供技术先进的信息化和电子商务解决方案，同时提供优质的咨询、培训和运维服务。</p>")       
    def aboutuse(self):
        QMessageBox.about(self, "关于安夏电子席卡",
                "<p><b>安夏电子席卡</b>是一款绿色环保，且高效的会议席卡系统。</p>"
                "<p><b>使用方法：</b>"
                "<ul>1.先设置要显示的名子</ul>"
                "<ul>2.设置要显示的名子的字体颜色</ul>"
                "<ul>3.设置要显示的名子的背景颜色</ul>"
                "<ul>4.背景若要使用图片请设置背景图片</ul></p>"
                "<p>若有疑问请联系 安夏电子科技有限公司 </p>"
                "<li>电话： 4008017129</li>"
                "<li>网址： www.anshare.com.cn<li></p>")    
    # 改变显示风格    
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
    def changePalette(self):
            QApplication.setPalette(QApplication.style().standardPalette())
    
class DisplayWindow(QDialog):
        
    def __init__(self, parent = None):
        super(DisplayWindow,self).__init__(parent)
        
        self.LayoutSetUp()
    
    def LayoutSetUp(self):        
        #创建图像层
        DP_Main_Layout=QVBoxLayout()
        self.DP_QGView=QGraphicsView()
        self.DP_QGView.setAlignment(Qt.AlignCenter)
        self.DP_QGScreen=QGraphicsScene()#控件
        self.DP_QGScreen.setBackgroundBrush(QColor("#ece8e4"))# 背景颜色
        self.DP_FullScreen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸       
        self.DP_QGScreen.setSceneRect(0,0,self.DP_FullScreen.width()*0.95 ,self.DP_FullScreen.height()*0.95)
        #设置默认背景图片
        self.DP_BGPIC_NameDisPlay=QPixmap("/home/anshare/下载/Display/AXlogo.png")#读取图片 AXlogo.png
        self.DP_QGBGPIC=QGraphicsPixmapItem()#定义一个图片项目
        self.DP_QGBGPIC.setPixmap(self.DP_BGPIC_NameDisPlay)#设置图片
        self.DP_QGBGPIC.setOpacity(0.3)#设置透明度   
        self.DP_QGBGPIC.setScale(1)#缩放
        #图片中心定位
        self.DP_QGBGPIC.setPos(self.DP_FullScreen.width()*0.95/2-self.DP_BGPIC_NameDisPlay.width()*(self.DP_QGBGPIC.scale())/2,self.DP_FullScreen.height()*0.95/2-self.DP_BGPIC_NameDisPlay.height()*(self.DP_QGBGPIC.scale())/2)
        #文字控件
        self.DP_QG_NAMEDP=QGraphicsTextItem()
        self.DP_QG_NAMEDP.setPlainText("安夏电子席卡 ")
        #字体横向居中
        DP_document = self.DP_QG_NAMEDP.document()
        DP_option = DP_document.defaultTextOption()
        DP_option.setAlignment(Qt.AlignCenter)
        DP_document.setDefaultTextOption(DP_option)
        #设置文字初始化
        self.DP_QG_NAMEDP.setFont(QFont("Noto Sans Mono CJK SC",50))#设置字体
        self.DP_QG_NAMEDP.setTextWidth(self.DP_FullScreen.width()*0.95)#设置文字宽度
        self.DP_QG_NAMEDP.setDefaultTextColor(QColor(Qt.black))#设置颜色
        self.DP_QG_NAMEDP.setPos(0,self.DP_FullScreen.height()*0.95/2-25)
        #添加控件
        self.DP_QGScreen.addItem(self.DP_QGBGPIC)
        self.DP_QGScreen.addItem(self.DP_QG_NAMEDP)
        #添加矩形框
        #self.DP_QGScreen.addRect(0,0,self.DP_FullScreen.width()*0.95,self.DP_FullScreen.height()*0.95, QColor(Qt.red))
        #添加显示
        self.DP_QGView.setScene(self.DP_QGScreen)
        DP_Main_Layout.addWidget(self.DP_QGView)
        self.setLayout(DP_Main_Layout)
        self.setWindowTitle("DisplayWindow")
        self.showFullScreen()
        
    def SetFullScreenDisPlay(self,name,CFort,CBG,DP_Font,QGImage,DPFS_Zoom_R,DPFS_Rote_R,DPFS_Opacity_R,DPFS_Move_W,DPFS_Move_H):
        
        if name != "" :
            #设置显示的名字
            self.DP_QG_NAMEDP.setPlainText(name)
            if CFort != 0 :
                #设置字体颜色
                self.DP_QG_NAMEDP.setDefaultTextColor(QColor(CFort))#设置颜色
                
            if CBG != 0: 
                pass
            if DP_Font != 0:
                self.DP_QG_NAMEDP.setFont(DP_Font)#设置字体
                DP_FortKey=DP_Font.key()
                DP_Fort_Set =DP_FortKey.split(',')
                #设置位置   
                self.DP_QG_NAMEDP.setPos(0,self.DP_FullScreen.height()*0.95/3-int(DP_Fort_Set[1])/2)   
            if QGImage != None :
                self.DP_QGScreen.setBackgroundBrush(QColor(Qt.white))# 背景颜色
                self.DP_DisplayPicture=QGImage
                self.DP_QGBGPIC.setPixmap(self.DP_DisplayPicture)
                self.DP_QGBGPIC.setOffset(-float(self.DP_DisplayPicture.width()/2),-float(self.DP_DisplayPicture.height()/2))
                self.DP_QGBGPIC.setScale(float(DPFS_Zoom_R))
                self.DP_QGBGPIC.setRotation(float(DPFS_Rote_R))
                self.DP_QGBGPIC.setOpacity(float(DPFS_Opacity_R))
                self.DP_QGBGPIC.setPos(0.95*(self.DP_FullScreen.width()/2+DPFS_Move_W),0.95*(self.DP_FullScreen.height()/2+DPFS_Move_H))
        else :
            self.DP_QG_NAMEDP.setPlainText("请完成设置！")
    
    #双击退出函数            
    def mouseDoubleClickEvent(self,event):  
        self.close()   

class ImageViewer(QDialog):
    def __init__(self, parent = None):
        super(ImageViewer, self).__init__(parent)
        #建立共有变量：0.图片 1.放大因数 2.旋转因数 3.透明因数 4.横向移动 5.纵向移动
        self.PE_BGPicture=None
        self.PE_Zoom_R=1
        self.PE_Rote_R=0
        self.PE_Opacity_R=1
        self.PE_Move_W=0
        self.PE_Move_H=0
        self.LayoutSetUp()

    def Group_Control(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #控制面板 界面编辑
        PE_HBox = QHBoxLayout()
        #打开图片
        openPicture_button = QPushButton("打开图片")
        PE_HBox.addWidget(openPicture_button)
        openPicture_button.clicked.connect(self.open)
        #重置按钮
        Picture_Reset_button = QPushButton("重置图片")
        PE_HBox.addWidget(Picture_Reset_button)
        Picture_Reset_button.clicked.connect(self.normalSize)
        #适应全屏
        Picture_Fit_button = QPushButton("适应窗口")
        PE_HBox.addWidget(Picture_Fit_button)
        Picture_Fit_button.clicked.connect(self.fitToWindow)
        #第一层列表
        hBox1=QHBoxLayout()
        
        PE_gridLayout1 = QGridLayout()
        #缩放控制
        row=0
        PE_gridLayout1.addWidget(QLabel("缩放:"), row, 0)
        self.PE_Zoom_spinBox = QDoubleSpinBox()
        self.PE_Zoom_spinBox.setValue(1.0000)
        self.PE_Zoom_spinBox.setRange(0.00,20.00)
        self.PE_Zoom_spinBox.setSingleStep(0.01)
        PE_gridLayout1.addWidget(self.PE_Zoom_spinBox, row, 1)
        self.PE_Zoom_spinBox.valueChanged[float].connect(self.PE_Zoom)
        
        row=row+1
        self.PE_Zoom_slider = QSlider(Qt.Horizontal)
        self.PE_Zoom_slider.setValue(1)
        self.PE_Zoom_slider.setRange(0,20)
        self.PE_Zoom_slider.setSingleStep(1)
        PE_gridLayout1.addWidget(self.PE_Zoom_slider, row, 0,1,3)
        self.PE_Zoom_slider.valueChanged[int].connect(self.PE_Zoom)
        #旋转控制
        row=row+1
        PE_gridLayout1.addWidget(QLabel("旋转:"), row, 0)
        self.PE_Rote_spinBox = QDoubleSpinBox()
        self.PE_Rote_spinBox.setValue(0.0000)
        self.PE_Rote_spinBox.setRange(-180.00,180.00)
        self.PE_Rote_spinBox.setSingleStep(0.1)
        self.PE_Rote_spinBox.valueChanged[float].connect(self.PE_Rote)
        PE_gridLayout1.addWidget(self.PE_Rote_spinBox, row, 1)
        row=row+1
        self.PE_Rote_slider = QSlider(Qt.Horizontal)
        self.PE_Rote_slider.setValue(0)
        self.PE_Rote_slider.setRange(-180.00,180.00)
        self.PE_Rote_slider.setSingleStep(1)
        self.PE_Rote_slider.valueChanged[int].connect(self.PE_Rote)
        PE_gridLayout1.addWidget(self.PE_Rote_slider, row, 0,1,3)
        row=row+1
        #透明度设置
        PE_gridLayout1.addWidget(QLabel("透明度:"), row, 0)
        self.PE_Opacity_spinBox = QDoubleSpinBox()
        self.PE_Opacity_spinBox.setValue(1.00)
        self.PE_Opacity_spinBox.setRange(0.00,1.00)
        self.PE_Opacity_spinBox.setSingleStep(0.01)
        self.PE_Opacity_spinBox.valueChanged[float].connect(self.PE_Opacity)
        PE_gridLayout1.addWidget(self.PE_Opacity_spinBox, row, 1)
        row=row+1
        self.PE_Opacity_slider = QSlider(Qt.Horizontal)
        self.PE_Opacity_slider.setValue(1)
        self.PE_Opacity_slider.setRange(0.00,1.00)
        self.PE_Opacity_slider.setSingleStep(1)
        self.PE_Opacity_slider.valueChanged[int].connect(self.PE_Opacity)
        PE_gridLayout1.addWidget(self.PE_Opacity_slider, row, 0,1,3)
        
        hBox1.addLayout(PE_gridLayout1)  
        PE_HBox.addLayout(hBox1) 
        #第二层列表
        hBox2=QVBoxLayout()
        PE_gridLayout2 = QGridLayout()
        #横向调整
        row=0
        PE_gridLayout2.addWidget(QLabel("横向调整:"), row, 0)
        self.PE_W_spinBox = QSpinBox()
        self.PE_W_spinBox.setValue(0.0000)
        self.PE_W_spinBox.setRange(-1000,1000)
        self.PE_W_spinBox.setSingleStep(1)
        self.PE_W_spinBox.valueChanged[int].connect(self.PE_Move_W_FX)
        PE_gridLayout2.addWidget(self.PE_W_spinBox, row, 1)
        row=row+1
        self.PE_W_Move_slider = QSlider(Qt.Horizontal)
        self.PE_W_Move_slider.setValue(0)
        self.PE_W_Move_slider.setRange(-1000,1000)
        self.PE_W_Move_slider.valueChanged[int].connect(self.PE_Move_W_FX)
        PE_gridLayout2.addWidget(self.PE_W_Move_slider, row, 0,1,3) 
        #纵向调整
        row=row+1
        PE_gridLayout2.addWidget(QLabel("纵向调整:"), row, 0)
        self.PE_H_spinBox = QSpinBox()
        self.PE_H_spinBox.setValue(0.0000)
        self.PE_H_spinBox.setRange(-1000,1000)
        self.PE_H_spinBox.valueChanged[int].connect(self.PE_Move_H_FX)
        PE_gridLayout2.addWidget(self.PE_H_spinBox, row, 1)
        row=row+1
        self.PE_H_Move_slider = QSlider(Qt.Horizontal)
        self.PE_H_Move_slider.setValue(0)
        self.PE_H_Move_slider.setRange(-1000,1000)
        self.PE_H_Move_slider.valueChanged[int].connect(self.PE_Move_H_FX)
        PE_gridLayout2.addWidget(self.PE_H_Move_slider, row, 0,1,3)
        
        hBox2.addLayout(PE_gridLayout2)  
        PE_HBox.addLayout(hBox2) 
        
        #应用按钮
        Picture_Apply_button=QPushButton("应用图片")
        PE_HBox.addWidget(Picture_Apply_button)
        Picture_Apply_button.clicked.connect(self.onOkClicked)
        #关闭按钮
        Close_button=QPushButton("关闭")
        PE_HBox.addWidget(Close_button)
        Close_button.clicked.connect(self.onOkClicked)
        
        PE_HBox.addStretch()
        group.setLayout(PE_HBox)
        
        return group
    
    def Group_Picture_Show(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        
        hbox = QHBoxLayout()#垂直布局
        PE_QGView=QGraphicsView()#控件
        PE_QGScene=QGraphicsScene()#控件
        PE_QGView.setAlignment(Qt.AlignCenter)#居中
        PE_QGScene.setBackgroundBrush(QColor("#ece8e4"))
        #新的版本
        self.PE_Screen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸 
        PE_QGScene.setSceneRect(0,0,self.PE_Screen.width(),self.PE_Screen.height())
        #加载图片
        self.PE_BGPicture=QPixmap("/home/anshare/下载/Display/AXLogo.png")#读取图片 AXLogo.png
        self.PE_QGPixmap=QGraphicsPixmapItem()#定义一个图片项目
        self.PE_QGPixmap.setPixmap(self.PE_BGPicture)#设置图片
        self.PE_QGPixmap.setOpacity(0.3)#设置透明度
        self.PE_QGPixmap.setScale(1)#缩放
        #计算出居中
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2-self.PE_BGPicture.width()*(self.PE_QGPixmap.scale())/2,self.PE_Screen.height()/2-self.PE_BGPicture.height()*(self.PE_QGPixmap.scale())/2)
        #添加控件
        PE_QGScene.addItem(self.PE_QGPixmap)
        PE_QGScene.addRect(0,0,self.PE_Screen.width(),self.PE_Screen.height(), Qt.red)#添加边框
        #添加显示
        PE_QGView.scale(PE_QGView.width()/(2.5*PE_QGScene.width()),PE_QGView.width()/(2.5*PE_QGScene.width()))
        PE_QGView.setScene(PE_QGScene)
        hbox.addWidget(PE_QGView)
        group.setLayout(hbox)

        return group        
    
    def LayoutSetUp(self): 
        #放大因子
        self.scaleFactor = 0.0
        #设置主要控件
        self.mainVertLayout = QVBoxLayout()
        self.mainVertLayout.addWidget(self.Group_Picture_Show("图片显示"))
        self.mainVertLayout.addWidget(self.Group_Control("控制面板"))
               
        #显示
        self.PE_Screen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸
        self.setLayout(self.mainVertLayout)
        self.showFullScreen()
        self.setWindowTitle("图片编辑器")
   
    def open(self):
        #获得文件地址及名称
        fileName, _ = QFileDialog.getOpenFileName(self, "打开图片",
                QDir.currentPath())
        if fileName:
            self.image = QImage(fileName)
            if self.image.isNull():
                QMessageBox.information(self, "图片编辑器",
                        "不能载入 %s." % fileName)
                return

            self.PE_BGPicture=QPixmap(self.image)
            self.PE_QGPixmap.setPixmap(self.PE_BGPicture)#设置图片
            self.scaleFactor = 1.0
            self.PE_QGPixmap.setOpacity(1)#设置透明度
            self.PE_QGPixmap.setScale(self.scaleFactor)#缩放
            self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
            #设置位置
            self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
            
    def PE_Zoom(self,PE_ZoomScale):
        #传递 放大系数
        self.PE_Zoom_R=PE_ZoomScale
        self.PE_QGPixmap.setScale(float(PE_ZoomScale))
        #设置中心点
        self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        self.PE_Zoom_slider.setValue(int(PE_ZoomScale))
        self.PE_Zoom_spinBox.setValue(float(PE_ZoomScale))
        
    def PE_Rote(self,PE_RoteRate):
        self.PE_Rote_R=PE_RoteRate
        self.PE_QGPixmap.setRotation(float(PE_RoteRate))
        #设置中心点
        self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        self.PE_Rote_spinBox.setValue(float(PE_RoteRate))
        self.PE_Rote_slider.setValue(int(PE_RoteRate))
           
    def PE_Opacity(self,PE_Opacity_Rate):
        #设置透明
        self.PE_Opacity_R=PE_Opacity_Rate
        self.PE_QGPixmap.setOpacity(float(PE_Opacity_Rate))
        self.PE_Opacity_slider.setValue(int(PE_Opacity_Rate))
        self.PE_Opacity_spinBox.setValue(float(PE_Opacity_Rate))
        
    def PE_Move_W_FX(self,PE_Move_W_Value):
        self.PE_Move_W=PE_Move_W_Value
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        self.PE_W_spinBox.setValue(PE_Move_W_Value)
        self.PE_W_Move_slider.setValue(PE_Move_W_Value)
        
    def PE_Move_H_FX(self,PE_Move_H_Value):
        self.PE_Move_H=PE_Move_H_Value
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        self.PE_H_spinBox.setValue(PE_Move_H_Value)
        self.PE_H_Move_slider.setValue(PE_Move_H_Value)
        
    def normalSize(self):
        self.scaleFactor = 1.0
        self.PE_QGPixmap.setOpacity(1.0)
        self.PE_QGPixmap.setRotation(0)
        self.PE_Move_W=0
        self.PE_Move_H=0
        
        self.PE_QGPixmap.setScale(self.scaleFactor)
        #设置中心点
        self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        #重置所有参数
        self.PE_Zoom_spinBox.setValue(1)
        self.PE_Zoom_slider.setValue(1)
        self.PE_Rote_spinBox.setValue(0)
        self.PE_Rote_slider.setValue(0)
        self.PE_Opacity_spinBox.setValue(1)
        self.PE_Opacity_slider.setValue(1)
        self.PE_W_spinBox.setValue(0)
        self.PE_W_Move_slider.setValue(0)
        self.PE_H_spinBox.setValue(0)
        self.PE_H_Move_slider.setValue(0)
        
    def fitToWindow(self):
        self.PE_QGPixmap.setRotation(0)
        self.PE_Move_W=0
        self.PE_Move_H=0
        #缩放控制
        BGPICScale_H=float(self.PE_Screen.height()/self.PE_BGPicture.height())
        BGPICScale_W=float(self.PE_Screen.width()/self.PE_BGPicture.width())
        if BGPICScale_H>BGPICScale_W : BGPICScale=BGPICScale_H
        else : BGPICScale=BGPICScale_W
        self.PE_QGPixmap.setScale(BGPICScale)#缩放
        #设置中心点
        self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+self.PE_Move_W,self.PE_Screen.height()/2+self.PE_Move_H)
        #重置所有参数
        self.PE_Zoom_slider.setValue(int(BGPICScale))
        self.PE_Zoom_spinBox.setValue(float(BGPICScale))
        self.PE_Rote_spinBox.setValue(0)
        self.PE_Rote_slider.setValue(0)
        self.PE_Opacity_spinBox.setValue(1)
        self.PE_Opacity_slider.setValue(1)
        self.PE_W_spinBox.setValue(0)
        self.PE_W_Move_slider.setValue(0)
        self.PE_H_spinBox.setValue(0)
        self.PE_H_Move_slider.setValue(0)
        
    def getImage(self):
        return self.PE_BGPicture
    def getZoom_R(self):
        return self.PE_Zoom_R
    def getRote_R(self):
        return self.PE_Rote_R
    def getOpacity(self):
        return self.PE_Opacity_R
    def getMove_W(self):
        return self.PE_Move_W
    def getMove_H(self):
        return self.PE_Move_H
    
    def SetImage(self,PicImage):
        self.image=PicImage
        
    def OnOK(self):
        pass
    #退出按钮
    def onOkClicked(self):
        self.OnOK()
        self.accept()

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())
