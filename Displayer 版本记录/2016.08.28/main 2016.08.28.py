'''
Created on 2016.07.15
@author: Anshare_LY
2016.08.14 完成图像处理部分的全部功能
2016.08.18 完成树莓派 800*480官方屏幕的测试
2016.08.19 重新调整布局 
2016.08.22 完成树莓派上的二次细化完善
2016.08.25 完成图片编辑自动保存功能
2016.08.26 开始设计字体设置高级界面部分功能
2016.08.29 完成字体高级编辑功能[字体设置、字体透明度、字体位置]
2016.08.29 加入帮助板块 Group3 UseHelp & About
2016.08.29 *（可选） 完成图片编辑背景色填充设置
2016.08.29 树莓派测试

暂留问题：
 1.字体编辑界面链接问题  OK
 2.程序代码迭代
 3.功能优化
 4.界面布局
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
        self.WindowsTitle="安夏电子席卡   ——V 1.3"
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
        
        #hbox.addStretch()
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
        
        self.mainarea=QWidget()
        self.mainVertLayout = QVBoxLayout()
        self.vlayout2 = QVBoxLayout()
        self.vlayout2.addWidget(self.Group2("预览"))
        self.mainVertLayout.addLayout(self.vlayout2)

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
        self.PICE_APP_OUT=ImageViewer(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H)
        #self.PICE_APP_OUT.Set_PE_Picture(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H)
        self.PICE_APP_OUT.exec_()
        #传递当前图片参数
        self.Get_QGPicture(self.PICE_APP_OUT.getImage(),self.PICE_APP_OUT.getZoom_R(),self.PICE_APP_OUT.getRote_R(),self.PICE_APP_OUT.getOpacity(),self.PICE_APP_OUT.getMove_W(),self.PICE_APP_OUT.getMove_H())#接收返回图片
        self.OnAction()
        
    #字体编辑
    def onFontEidt(self):
        self.FE_APP_OUT=FontViewer(self.DisplayPicture, self.MDP_Zoom_R, self.MDP_Rote_R, self.MDP_Opacity_R, self.MDP_Move_W, self.MDP_Move_H,self.name_input,self.font,self.Fort_color_R,self.Font_Opacity,self.Font_Move_W,self.Font_Move_H)
        self.FE_APP_OUT.exec_()
        #传递当前图片参数
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
            print("Main 字体透明度 %f 宽度位移 %d 高度位移 %d" %(self.Font_Opacity,self.Font_Move_W,self.Font_Move_H))
            print("Main 屏幕尺寸 %d  %d" %(self.screen.width(),self.screen.height()))
            print("Main 字体位置 %f  %f" %(self.Font_Move_W,self.screen.height()/2-self.font_R1/2+self.Font_Move_H))
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
        print("Main获取FE 字体透明度 %f 宽度位移 %d 高度位移 %d" %(self.Font_Opacity,self.Font_Move_W,self.Font_Move_H))
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
                "<p><b>安夏电子席卡</b>是一款绿色环保，且高效的会议席卡系统。</p>"
                "<p><b>使用方法：</b>"
                "<ul>1.先设置要显示的名子</ul>"
                "<ul>2.设置要显示的名子的字体，具体设置字体，透明度，位置</ul>"
                "<ul>3.设置要显示的名子的文字颜色</ul>"
                "<ul>4.背景若要使用图片请设置背景图片，可以使用适应窗口快速设置按钮完成设置</ul></p>"
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
        self.DP_QGScreen.setSceneRect(0,0,self.DP_FullScreen.width() ,self.DP_FullScreen.height())
        #设置默认背景图片
        self.DP_BGPIC_NameDisPlay=QPixmap("AXlogo.png")#读取图片 AXlogo.png
        self.DP_QGBGPIC=QGraphicsPixmapItem()#定义一个图片项目
        self.DP_QGBGPIC.setPixmap(self.DP_BGPIC_NameDisPlay)#设置图片
        self.DP_QGBGPIC.setOpacity(0.3)#设置透明度   
        self.DP_QGBGPIC.setScale(1)#缩放
        #图片中心定位
        self.DP_QGBGPIC.setPos(self.DP_FullScreen.width()/2-self.DP_BGPIC_NameDisPlay.width()*(self.DP_QGBGPIC.scale())/2,self.DP_FullScreen.height()/2-self.DP_BGPIC_NameDisPlay.height()*(self.DP_QGBGPIC.scale())/2)
        #文字控件
        self.DP_QG_NAMEDP=QGraphicsTextItem()
        self.DP_QG_NAMEDP.setPlainText("安夏电子席卡 ")
        #字体横向居中
        DP_document = self.DP_QG_NAMEDP.document()
        DP_option = DP_document.defaultTextOption()
        DP_option.setAlignment(Qt.AlignCenter)
        DP_document.setDefaultTextOption(DP_option)
        #设置文字初始化
        self.DP_QG_NAMEDP.setFont(QFont("华文新魏",50))#设置字体
        self.DP_QG_NAMEDP.setTextWidth(self.DP_FullScreen.width())#设置文字宽度
        self.DP_QG_NAMEDP.setDefaultTextColor(QColor(Qt.black))#设置颜色
        self.DP_QG_NAMEDP.setPos(0,self.DP_FullScreen.height()/2-25)
        #添加控件
        self.DP_QGScreen.addItem(self.DP_QGBGPIC)
        self.DP_QGScreen.addItem(self.DP_QG_NAMEDP)
        #添加矩形框
        #self.DP_QGScreen.addRect(0,0,self.DP_FullScreen.width(),self.DP_FullScreen.height(), QColor(Qt.red))
        #添加显示
        self.DP_QGView.setScene(self.DP_QGScreen)
        self.DP_QGView.scale(0.96,0.96)
        DP_Main_Layout.addWidget(self.DP_QGView)
        self.setLayout(DP_Main_Layout)
        self.setWindowTitle("DisplayWindow")
        self.showFullScreen()
        
    def SetFullScreenDisPlay(self,name,CFort,CBG,DP_Font,QGImage,DPFS_Zoom_R,DPFS_Rote_R,DPFS_Opacity_R,DPFS_Move_W,DPFS_Move_H,Font_Opacity,Font_Move_W,Font_Move_H):
        
        if name != "" :
            #设置显示的名字
            self.DP_QG_NAMEDP.setPlainText(name)
            if CFort != None :
                #设置字体颜色
                self.DP_QG_NAMEDP.setDefaultTextColor(QColor(CFort))#设置颜色
                
            if CBG != None: 
                pass
            if DP_Font != None:
                self.DP_QG_NAMEDP.setFont(DP_Font)#设置字体
                DP_FortKey=DP_Font.key()
                DP_Fort_Set =DP_FortKey.split(',')
                self.DP_QG_NAMEDP.setOpacity(float(Font_Opacity))
                #设置位置   
                self.DP_QG_NAMEDP.setPos(Font_Move_W,self.DP_FullScreen.height()/2-int(DP_Fort_Set[1])/2+Font_Move_H)
                print("DP 字体透明度 %f 宽度位移 %d 高度位移 %d" %(Font_Opacity,Font_Move_W,Font_Move_H))
                print("DP 屏幕尺寸 %d  %d" %(self.DP_FullScreen.width(),self.DP_FullScreen.height()))
                print("DP 字体位置 %f  %f" %(Font_Move_W,self.DP_FullScreen.height()/2-int(DP_Fort_Set[1])/2+Font_Move_W))
        
                
            if QGImage != None :
                #self.DP_QGScreen.setBackgroundBrush(QColor(Qt.white))# 背景颜色
                self.DP_DisplayPicture=QGImage
                self.DP_QGBGPIC.setPixmap(self.DP_DisplayPicture)
                self.DP_QGBGPIC.setOffset(-float(self.DP_DisplayPicture.width()/2),-float(self.DP_DisplayPicture.height()/2))
                self.DP_QGBGPIC.setScale(float(DPFS_Zoom_R)*1.05)
                self.DP_QGBGPIC.setRotation(float(DPFS_Rote_R))
                self.DP_QGBGPIC.setOpacity(float(DPFS_Opacity_R))
                self.DP_QGBGPIC.setPos((self.DP_FullScreen.width()/2+DPFS_Move_W),(self.DP_FullScreen.height()/2+DPFS_Move_H))
            else:
                self.DP_QGBGPIC.setOpacity(0)
        else :
            self.DP_QG_NAMEDP.setPlainText("请完成设置！")
    
    #双击退出函数            
    def mouseDoubleClickEvent(self,event):  
        self.close()   

class FontViewer(QDialog):
    def __init__(self,QGImage,QGImage_Zoom_R,QGImage_Rote_R,QGImage_Opacity_R,QGImage_Move_W,QGImage_Move_H,Name_Input,Name_Font,Name_Color,Name_Opacity,Name_Move_W,Name_Move_H):
        super(FontViewer, self).__init__()
        #建立共有变量：0.图片 1.放大因数 2.旋转因数 3.透明因数 4.横向移动 5.纵向移动 6.背景颜色
        self.FE_BGPicture=QGImage
        self.FE_Zoom_R=QGImage_Zoom_R
        self.FE_Rote_R=QGImage_Rote_R
        self.FE_Opacity_R=QGImage_Opacity_R
        self.FE_Move_W=QGImage_Move_W
        self.FE_Move_H=QGImage_Move_H
        self.FE_BG_Color="#ece8e4" #设置背景颜色
        #字体设置 [字体、颜色]
        #字体输入初始化
        if Name_Input!= "" :
            self.FE_Name_Input=Name_Input
        else :
            self.FE_Name_Input="安 夏"
        # 字体初始化
        if Name_Font != None:
            self.FE_Name_Font=Name_Font
            FontElements=str(self.FE_Name_Font.key())
            self.font_R=FontElements.split(',')
            #分离字体属性
            self.FE_font_R0=self.font_R[0]
            self.FE_font_R1=int(self.font_R[1])
            self.FE_font_R2=int(self.font_R[2])
            self.FE_font_R3=int(self.font_R[3])
            self.FE_font_R4=int(self.font_R[4])
            self.FE_font_R5=int(self.font_R[5])
            self.FE_font_R6=int(self.font_R[6])
            self.FE_font_R7=int(self.font_R[7])
            self.FE_font_R8=int(self.font_R[8])
            self.FE_font_R9=int(self.font_R[9])
        else :
            #self.FE_Name_Font={"华文新魏",130,-1,5,50,0,0,0,0,0}
            #原始设置
            self.FE_font_R0="华文新魏"
            self.FE_font_R1=130
            self.FE_font_R2=-1
            self.FE_font_R3=5
            self.FE_font_R4=50
            self.FE_font_R5=0
            self.FE_font_R6=0
            self.FE_font_R7=0
            self.FE_font_R8=0
            self.FE_font_R9=0
        #字体颜色初始化
        if Name_Color !=None:
            self.FE_Name_Color=Name_Color
        else :
            self.FE_Name_Color=Qt.black
        
        if Name_Opacity !=None:
            self.FE_Name_Opacity=Name_Opacity
        else :
            self.FE_Name_Opacity=1
        if Name_Move_W !=None:
            self.FE_Name_Move_W=Name_Move_W
        else:
            self.FE_Name_Move_W=0
        if Name_Move_H != None:
            self.FE_Name_Move_H=Name_Move_H
        else:
            self.FE_Name_Move_H=0       
        
        self.LayoutSetUp()
        #设置背景
        self.Set_FE_Picture(self.FE_BGPicture, self.FE_Zoom_R, self.FE_Rote_R, self.FE_Opacity_R, self.FE_Move_W, self.FE_Move_H)
        #设置字体
        self.Set_FE_Font()
        
    def Group_Control(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #控制面板 界面编辑
        FE_HBox = QHBoxLayout()
        #第一列
        #字体编辑
        hBox0_0=QHBoxLayout()
        FE_gridLayout0_0 = QGridLayout()
        row=0
        Font_Set_button = QPushButton("字体设置")
        FE_gridLayout0_0.addWidget(Font_Set_button,row,0)
        Font_Set_button.clicked.connect(self.FontSetFunction)
        row=row+1
        self.FE_Fort_Lable=QLabel(" ")
        FE_gridLayout0_0.addWidget(self.FE_Fort_Lable,row,0)
        self.FE_Fort_Lable.setAlignment(Qt.AlignCenter)
        FE_gridLayout0_0.setAlignment(Qt.AlignCenter)
        hBox0_0.addLayout(FE_gridLayout0_0)
        FE_HBox.addLayout(hBox0_0) 
        
        #第0列 两个按钮
        hBox0=QHBoxLayout()
        FE_gridLayout0 = QGridLayout()
        row=0
        #政府魔板
        ZF_Model_button = QPushButton("政府魔板")
        FE_gridLayout0.addWidget(ZF_Model_button,row,0)
        ZF_Model_button.clicked.connect(self.ZFModelFunction)
        row=row+1
        #重置字体
        Font_Reset_button = QPushButton("重置字体")
        FE_gridLayout0.addWidget(Font_Reset_button,row,0)
        Font_Reset_button.clicked.connect(self.FontResetFunction)
        
        hBox0.addLayout(FE_gridLayout0)  
        FE_HBox.addLayout(hBox0) 
        
        #第一层设置
        hBox1=QHBoxLayout()
        FE_gridLayout1 = QGridLayout()
        row=0
        #透明度设置
        FE_gridLayout1.addWidget(QLabel("透明度:"), row, 0)
        self.FE_Opacity_spinBox = QDoubleSpinBox()
        self.FE_Opacity_spinBox.setValue(1.00)
        self.FE_Opacity_spinBox.setRange(0.00,1.00)
        self.FE_Opacity_spinBox.setSingleStep(0.01)
        self.FE_Opacity_spinBox.valueChanged[float].connect(self.FE_Opacity)
        FE_gridLayout1.addWidget(self.FE_Opacity_spinBox, row, 1)
        row=row+1
        self.FE_Opacity_slider = QSlider(Qt.Horizontal)
        self.FE_Opacity_slider.setValue(1)
        self.FE_Opacity_slider.setRange(0.00,1.00)
        self.FE_Opacity_slider.setSingleStep(1)
        self.FE_Opacity_slider.valueChanged[int].connect(self.FE_Opacity)
        FE_gridLayout1.addWidget(self.FE_Opacity_slider, row, 0,1,3)
        hBox1.addLayout(FE_gridLayout1)  
        FE_HBox.addLayout(hBox1)
         
        #第二层列表
        hBox2=QVBoxLayout()
        FE_gridLayout2 = QGridLayout()
        #横向调整
        row=0
        FE_gridLayout2.addWidget(QLabel("横向调整:"), row, 0)
        self.FE_W_spinBox = QSpinBox()
        self.FE_W_spinBox.setValue(0.0000)
        self.FE_W_spinBox.setRange(-1000,1000)
        self.FE_W_spinBox.setSingleStep(1)
        self.FE_W_spinBox.valueChanged[int].connect(self.FE_Move_W_FX)
        FE_gridLayout2.addWidget(self.FE_W_spinBox, row, 1)
        row=row+1
        self.FE_W_Move_slider = QSlider(Qt.Horizontal)
        self.FE_W_Move_slider.setValue(0)
        self.FE_W_Move_slider.setRange(-1000,1000)
        self.FE_W_Move_slider.valueChanged[int].connect(self.FE_Move_W_FX)
        FE_gridLayout2.addWidget(self.FE_W_Move_slider, row, 0,1,3) 
        #纵向调整
        row=row+1
        FE_gridLayout2.addWidget(QLabel("纵向调整:"), row, 0)
        self.FE_H_spinBox = QSpinBox()
        self.FE_H_spinBox.setValue(0.0000)
        self.FE_H_spinBox.setRange(-1000,1000)
        self.FE_H_spinBox.valueChanged[int].connect(self.FE_Move_H_FX)
        FE_gridLayout2.addWidget(self.FE_H_spinBox, row, 1)
        row=row+1
        self.FE_H_Move_slider = QSlider(Qt.Horizontal)
        self.FE_H_Move_slider.setValue(0)
        self.FE_H_Move_slider.setRange(-1000,1000)
        self.FE_H_Move_slider.valueChanged[int].connect(self.FE_Move_H_FX)
        FE_gridLayout2.addWidget(self.FE_H_Move_slider, row, 0,1,3)
        
        hBox2.addLayout(FE_gridLayout2)  
        FE_HBox.addLayout(hBox2) 
        
        #第三层列表
        hBox3=QVBoxLayout()
        FE_gridLayout3 = QGridLayout()
        row=0
        #应用按钮
        Picture_Apply_button=QPushButton("应用字体")
        FE_gridLayout3.addWidget(Picture_Apply_button,row,0)
        Picture_Apply_button.clicked.connect(self.onOkClicked)
        row=row+1
        #关闭按钮
        Close_button=QPushButton("关闭")
        FE_gridLayout3.addWidget(Close_button,row,0)
        Close_button.clicked.connect(self.onOkClicked)
        
        hBox3.addLayout(FE_gridLayout3)  
        FE_HBox.addLayout(hBox3)
        
        #FE_HBox.addStretch()
        group.setLayout(FE_HBox)
        
        return group
    
    def Group_FE_Show(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        
        hbox = QHBoxLayout()#垂直布局
        FE_QGView=QGraphicsView()#控件
        FE_QGScene=QGraphicsScene()#控件
        FE_QGView.setAlignment(Qt.AlignCenter)#居中
        FE_QGScene.setBackgroundBrush(QColor("#ece8e4"))
        #新的版本
        self.FE_Screen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸 
        FE_QGScene.setSceneRect(0,0,self.FE_Screen.width(),self.FE_Screen.height())
        #加载图片
        self.FE_QGPixmap=QGraphicsPixmapItem()#定义一个图片项目
        self.FE_QGPixmap.setPixmap(self.FE_BGPicture)#设置图片
        #计算出居中
        self.FE_QGPixmap.setPos(self.FE_Screen.width()/2-self.FE_BGPicture.width()*(self.FE_QGPixmap.scale())/2,self.FE_Screen.height()/2-self.FE_BGPicture.height()*(self.FE_QGPixmap.scale())/2)
        #加载文字
        self.FE_QGNAMEDP=QGraphicsTextItem()
        self.FE_QGNAMEDP.setPlainText(self.FE_Name_Input)
        self.FE_QGNAMEDP.setOpacity(self.FE_Name_Opacity)
        #字体横向居中
        document = self.FE_QGNAMEDP.document()
        option = document.defaultTextOption()
        option.setAlignment(Qt.AlignCenter)
        document.setDefaultTextOption(option)
        #设置文字初始化
        self.FE_QGNAMEDP.setFont(QFont(self.FE_font_R0,self.FE_font_R1))#设置字体
        self.FE_QGNAMEDP.setTextWidth(self.FE_Screen.width())#设置文字宽度
        self.FE_QGNAMEDP.setDefaultTextColor(QColor(self.FE_Name_Color))#设置颜色
        self.FE_QGNAMEDP.setPos(self.FE_Name_Move_W,self.FE_Screen.height()/2+self.FE_Name_Move_W-self.FE_font_R1/2)
        
        #添加控件
        FE_QGScene.addItem(self.FE_QGPixmap)
        FE_QGScene.addItem(self.FE_QGNAMEDP)
        FE_QGScene.addRect(0,0,self.FE_Screen.width(),self.FE_Screen.height(), Qt.red)#添加边框
        #添加显示
        FE_QGView.scale(FE_QGView.width()/(1.5*FE_QGScene.width()),FE_QGView.width()/(1.5*FE_QGScene.width()))
        FE_QGView.setScene(FE_QGScene)
        hbox.addWidget(FE_QGView)
        group.setLayout(hbox)

        return group        
    
    def LayoutSetUp(self): 
        #设置主要控件
        self.mainVertLayout = QVBoxLayout()
        self.mainVertLayout.addWidget(self.Group_FE_Show("字体预览"))
        self.mainVertLayout.addWidget(self.Group_Control("控制面板"))
        #显示
        #self.FE_Screen = QDesktopWidget().screenGeometry()  #获取屏幕尺寸
        self.setLayout(self.mainVertLayout)
        self.showFullScreen()
        self.setWindowTitle("字体编辑器")
    
    #功能部分
    def FontSetFunction(self):
        self.FE_Name_Font, ok = QFontDialog.getFont(QFont(self.FE_font_R0,self.FE_font_R1))
        if ok:
            FontElements=str(self.FE_Name_Font.key())
            self.font_R=FontElements.split(',')
            #分离字体属性
            self.FE_font_R0=self.font_R[0]
            self.FE_font_R1=int(self.font_R[1])
            self.FE_font_R2=int(self.font_R[2])
            self.FE_font_R3=int(self.font_R[3])
            self.FE_font_R4=int(self.font_R[4])
            self.FE_font_R5=int(self.font_R[5])
            self.FE_font_R6=int(self.font_R[6])
            self.FE_font_R7=int(self.font_R[7])
            self.FE_font_R8=int(self.font_R[8])
            self.FE_font_R9=int(self.font_R[9])
            self.FE_Fort_Lable.setText("%s %d" %(self.FE_font_R0,self.FE_font_R1))
            self.OnAction()
        
    def ZFModelFunction(self):
        pass
    
    def FontResetFunction(self):
        pass
    #执行显示
    def OnAction(self):
        
        if self.FE_Name_Input != "" :
            #显示文字
            self.FE_QGNAMEDP.setPlainText(self.FE_Name_Input)
            #字体颜色判断
            if self.FE_Name_Color != None :
                self.FE_QGNAMEDP.setDefaultTextColor(QColor(self.FE_Name_Color))
            #字体属性判断
            if self.FE_Name_Font != None:
                self.FE_QGNAMEDP.setFont(self.FE_Name_Font)
                self.FE_QGNAMEDP.setOpacity(self.FE_Name_Opacity)
                
            self.FE_QGNAMEDP.setPos(self.FE_Name_Move_W,self.FE_Screen.height()/2-self.FE_font_R1/2+self.FE_Name_Move_H)
            print("FE 屏幕尺寸 %d  %d" %(self.FE_Screen.width(),self.FE_Screen.height()))
            print("Main获取FE 字体透明度 %f 宽度位移 %d 高度位移 %d" %(self.FE_Name_Opacity,self.FE_Name_Move_W,self.FE_Name_Move_H))
            print("FE 字体位置 %f  %f" %(self.FE_Name_Move_W,self.FE_Screen.height()/2-self.FE_font_R1/2+self.FE_Name_Move_H))
        else : #若没有显示文字 则显示提示
            self.QGNAMEDP.setPlainText("安 夏")
    
    def FE_Opacity(self,FE_Opacity_Rate):
        #设置透明
        self.FE_Name_Opacity=FE_Opacity_Rate
        self.FE_QGNAMEDP.setOpacity(float(FE_Opacity_Rate))
        self.FE_Opacity_slider.setValue(int(FE_Opacity_Rate))
        self.FE_Opacity_spinBox.setValue(float(FE_Opacity_Rate))
        
    def FE_Move_W_FX(self,FE_Move_W_Value):
        self.FE_Name_Move_W=FE_Move_W_Value
        #设置位置
        self.FE_QGNAMEDP.setPos(self.FE_Name_Move_W,self.FE_Screen.height()/2-self.FE_font_R1/2+self.FE_Name_Move_H)
        self.FE_W_spinBox.setValue(FE_Move_W_Value)
        self.FE_W_Move_slider.setValue(FE_Move_W_Value)
        
    def FE_Move_H_FX(self,FE_Move_H_Value):
        self.FE_Name_Move_H=FE_Move_H_Value
        #设置位置
        self.FE_QGNAMEDP.setPos(self.FE_Name_Move_W,self.FE_Screen.height()/2-self.FE_font_R1/2+self.FE_Name_Move_H)
        self.FE_H_spinBox.setValue(FE_Move_H_Value)
        self.FE_H_Move_slider.setValue(FE_Move_H_Value)
    def Set_FE_Font(self):
        #字体
        self.FE_Fort_Lable.setText("%s %d" %(self.FE_font_R0,self.FE_font_R1))
        #透明度
        self.FE_Opacity_spinBox.setValue(float(self.FE_Name_Opacity))
        #横向位置
        self.FE_W_spinBox.setValue(self.FE_Name_Move_W)
        self.FE_W_Move_slider.setValue(self.FE_Name_Move_W)
        #纵向位置
        self.FE_H_spinBox.setValue(self.FE_Name_Move_H)
        self.FE_H_Move_slider.setValue(self.FE_Name_Move_H)

    #参数返回    
    def getFont(self):
        return self.FE_Name_Font
    def getFontOpacity(self):
        return self.FE_Name_Opacity
    def getFontMove_W(self):
        return self.FE_Name_Move_W
    def getFontMove_H(self):
        return self.FE_Name_Move_H
    
    
    def Set_FE_Picture(self,QGImage,QGImage_Zoom_R,QGImage_Rote_R,QGImage_Opacity_R,QGImage_Move_W,QGImage_Move_H):
        #获得图片相关参数
        self.FE_BGPicture=QGImage
        self.FE_Zoom_R=QGImage_Zoom_R
        self.FE_Rote_R=QGImage_Rote_R
        self.FE_Opacity_R=QGImage_Opacity_R
        self.FE_Move_W=QGImage_Move_W
        self.FE_Move_H=QGImage_Move_H
        
        #读取图片
        self.FE_QGPixmap.setPixmap(self.FE_BGPicture)
        #设置中心偏移
        self.FE_QGPixmap.setOffset(-float(self.FE_BGPicture.width()/2),-float(self.FE_BGPicture.height()/2))
        #设置放大
        self.FE_QGPixmap.setScale(QGImage_Zoom_R)
        #设置旋转
        self.FE_QGPixmap.setRotation(QGImage_Rote_R)
        #设置透明度
        self.FE_QGPixmap.setOpacity(QGImage_Opacity_R)
        #设置位置
        self.FE_QGPixmap.setPos(self.FE_Screen.width()/2+QGImage_Move_W,self.FE_Screen.height()/2+QGImage_Move_H)
    
    def OnOK(self):
        print("FE 屏幕尺寸 %d  %d" %(self.FE_Screen.width(),self.FE_Screen.height()))
        print("FE 字体透明度 %f 宽度位移 %d 高度位移 %d" %(self.FE_Name_Opacity,self.FE_Name_Move_W,self.FE_Name_Move_H))
        print("FE 字体位置 %f  %f" %(self.FE_Name_Move_W,self.FE_Screen.height()/2-self.FE_font_R1/2+self.FE_Name_Move_H))
        pass
    #退出按钮
    def onOkClicked(self):
        self.OnOK()
        self.accept()    


class ImageViewer(QDialog):
    def __init__(self,QGImage,QGImage_Zoom_R,QGImage_Rote_R,QGImage_Opacity_R,QGImage_Move_W,QGImage_Move_H):
        super(ImageViewer, self).__init__()
        #建立共有变量：0.图片 1.放大因数 2.旋转因数 3.透明因数 4.横向移动 5.纵向移动 6.背景颜色
        self.PE_BGPicture=QGImage
        self.PE_Zoom_R=QGImage_Zoom_R
        self.PE_Rote_R=QGImage_Rote_R
        self.PE_Opacity_R=QGImage_Opacity_R
        self.PE_Move_W=QGImage_Move_W
        self.PE_Move_H=QGImage_Move_H
        self.PE_BG_Color="#ece8e4" #设置背景颜色
        self.LayoutSetUp()
        self.Set_PE_Picture(self.PE_BGPicture, self.PE_Zoom_R, self.PE_Rote_R, self.PE_Opacity_R, self.PE_Move_W, self.PE_Move_H)

    def Group_Control(self, grpname):
        group = QGroupBox(grpname)
        group.setCheckable(False)
        #控制面板 界面编辑
        PE_HBox = QHBoxLayout()
        #打开图片
        openPicture_button = QPushButton("打开图片")
        PE_HBox.addWidget(openPicture_button)
        openPicture_button.clicked.connect(self.open)
        #第0列 两个按钮
        hBox0=QHBoxLayout()
        PE_gridLayout0 = QGridLayout()
        row=0
        #适应全屏
        Picture_Fit_button = QPushButton("适应窗口")
        PE_gridLayout0.addWidget(Picture_Fit_button,row,0)
        Picture_Fit_button.clicked.connect(self.fitToWindow)
        row=row+1
        #重置按钮
        Picture_Reset_button = QPushButton("重置图片")
        PE_gridLayout0.addWidget(Picture_Reset_button,row,0)
        Picture_Reset_button.clicked.connect(self.normalSize)
        
        hBox0.addLayout(PE_gridLayout0)  
        PE_HBox.addLayout(hBox0) 
        
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
        hBox1.addLayout(PE_gridLayout1)  
        PE_HBox.addLayout(hBox1)
        
        hBox1_5=QHBoxLayout()
        PE_gridLayout1_5 = QGridLayout()
        row=0
        #透明度设置
        PE_gridLayout1_5.addWidget(QLabel("透明度:"), row, 0)
        self.PE_Opacity_spinBox = QDoubleSpinBox()
        self.PE_Opacity_spinBox.setValue(1.00)
        self.PE_Opacity_spinBox.setRange(0.00,1.00)
        self.PE_Opacity_spinBox.setSingleStep(0.01)
        self.PE_Opacity_spinBox.valueChanged[float].connect(self.PE_Opacity)
        PE_gridLayout1_5.addWidget(self.PE_Opacity_spinBox, row, 1)
        row=row+1
        self.PE_Opacity_slider = QSlider(Qt.Horizontal)
        self.PE_Opacity_slider.setValue(1)
        self.PE_Opacity_slider.setRange(0.00,1.00)
        self.PE_Opacity_slider.setSingleStep(1)
        self.PE_Opacity_slider.valueChanged[int].connect(self.PE_Opacity)
        PE_gridLayout1_5.addWidget(self.PE_Opacity_slider, row, 0,1,3)
        hBox1_5.addLayout(PE_gridLayout1_5)  
        PE_HBox.addLayout(hBox1_5)
         
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
        
        #第三层列表
        hBox3=QVBoxLayout()
        PE_gridLayout3 = QGridLayout()
        row=0
        #应用按钮
        Picture_Apply_button=QPushButton("应用图片")
        PE_gridLayout3.addWidget(Picture_Apply_button,row,0)
        Picture_Apply_button.clicked.connect(self.onOkClicked)
        row=row+1
        #关闭按钮
        Close_button=QPushButton("关闭")
        PE_gridLayout3.addWidget(Close_button,row,0)
        Close_button.clicked.connect(self.onOkClicked)
        
        hBox3.addLayout(PE_gridLayout3)  
        PE_HBox.addLayout(hBox3)
        
        #PE_HBox.addStretch()
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
        #图片加载
        self.PE_QGPixmap=QGraphicsPixmapItem()#定义一个图片项目
        self.PE_QGPixmap.setPixmap(self.PE_BGPicture)#设置图片
        #计算出居中
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2-self.PE_BGPicture.width()*(self.PE_QGPixmap.scale())/2,self.PE_Screen.height()/2-self.PE_BGPicture.height()*(self.PE_QGPixmap.scale())/2)
        #添加控件
        PE_QGScene.addItem(self.PE_QGPixmap)
        PE_QGScene.addRect(0,0,self.PE_Screen.width(),self.PE_Screen.height(), Qt.red)#添加边框
        #添加显示
        PE_QGView.scale(PE_QGView.width()/(1.5*PE_QGScene.width()),PE_QGView.width()/(1.5*PE_QGScene.width()))
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
    def getBGColor(self):
        return self.PE_BG_Color
    
    def Set_PE_Picture(self,QGImage,QGImage_Zoom_R,QGImage_Rote_R,QGImage_Opacity_R,QGImage_Move_W,QGImage_Move_H):
        #获得图片相关参数
        self.PE_BGPicture=QGImage
        self.PE_Zoom_R=QGImage_Zoom_R
        self.PE_Rote_R=QGImage_Rote_R
        self.PE_Opacity_R=QGImage_Opacity_R
        self.PE_Move_W=QGImage_Move_W
        self.PE_Move_H=QGImage_Move_H
        
        #读取图片
        self.PE_QGPixmap.setPixmap(self.PE_BGPicture)
        #设置中心偏移
        self.PE_QGPixmap.setOffset(-float(self.PE_BGPicture.width()/2),-float(self.PE_BGPicture.height()/2))
        #设置放大
        self.PE_QGPixmap.setScale(QGImage_Zoom_R)
        #设置旋转
        self.PE_QGPixmap.setRotation(QGImage_Rote_R)
        #设置透明度
        self.PE_QGPixmap.setOpacity(QGImage_Opacity_R)
        #设置位置
        self.PE_QGPixmap.setPos(self.PE_Screen.width()/2+QGImage_Move_W,self.PE_Screen.height()/2+QGImage_Move_H)
        
        #设置参数
        self.PE_Zoom(QGImage_Zoom_R)
        self.PE_Rote(QGImage_Rote_R)
        self.PE_Opacity(QGImage_Opacity_R)
        self.PE_Move_H_FX(QGImage_Move_H)
        self.PE_Move_W_FX(QGImage_Move_W)
        
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
