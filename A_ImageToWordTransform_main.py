from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PIL import Image
from QssLoader import *
import sys
import math
import os
#pyinstaller -F -w -i Images/faviconA.ico A_ImageToWordTransform_main.py
class QFileDialogEXPForm(QWidget):
    def __init__(self):
        super(QFileDialogEXPForm, self).__init__()

        self.fileName=""
        self.fileNameSaved=""
        self.stateText="Welcome!\nVersion 1.1.1 By VezzzingQAQ I.D.S\n"
        self.customArea=120000

        self.charList=[]#上色字符串集

        self.loadQss("support/QssFile/QssBright.qss")
        self.loadCharList()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("●I.T.W.V1.0.2!!!∑(ﾟДﾟノ)ノ")
        self.setWindowIcon(QIcon("support/Images/vezzzinge.png"))
        formlayout=QHBoxLayout()

        self.text=QTextEdit("最后会在这里显示")
        self.text.setFont(QFont("微软雅黑",1))
        # 右侧面板##########################################
        self.buttonLoad = QPushButton("导入图片")
        self.buttonLoad.clicked.connect(self.loadImage)

        self.cb=QComboBox()
        self.cb.addItems(self.charList)
        #如果已经选择了图片，自动切换：

        self.customeButton=QPushButton("自定义字符串")
        self.customeButton.clicked.connect(self.showCT)

        self.labelcb=QLabel("指定上色字符串")
        self.cb.currentIndexChanged.connect(lambda :self.changepictures(self.fileName))

        self.labelwidth=QLabel("调节图像宽度:125")

        self.sliderw = QSlider(Qt.Horizontal)  # 水平滑块
        self.sliderw.setMinimum(1)
        self.sliderw.setMaximum(1000)
        self.sliderw.setSingleStep(1)
        self.sliderw.setValue(125)
        self.sliderw.valueChanged.connect(lambda :self.changepictures(self.fileName))

        self.labelheight = QLabel("调节图像高度:125")

        self.sliderh = QSlider(Qt.Horizontal)  # 水平滑块
        self.sliderh.setMinimum(1)
        self.sliderh.setMaximum(1000)
        self.sliderh.setSingleStep(1)
        self.sliderh.setValue(125)
        self.sliderh.valueChanged.connect(lambda :self.changepictures(self.fileName))

        self.checkNewline=QCheckBox("插入换行符[For Python:\\n]")
        self.checkNewline.setObjectName("check1")
        self.checkNewline.stateChanged.connect(lambda :self.changepictures(self.fileName))
        self.checkAnnotation1=QCheckBox("插入段首单引号[For VB:']")
        self.checkAnnotation1.stateChanged.connect(lambda: self.changepictures(self.fileName))
        self.checkAnnotation2 = QCheckBox("插入段首双斜杠[For Java://]")
        self.checkAnnotation2.stateChanged.connect(lambda: self.changepictures(self.fileName))
        self.checkAnnotation3 = QCheckBox("插入段首井号[For Python:#]")
        self.checkAnnotation3.stateChanged.connect(lambda: self.changepictures(self.fileName))
        self.checkAnnotation4 = QCheckBox("插入注记[For HTML:<!---->]")
        self.checkAnnotation4.stateChanged.connect(lambda: self.changepictures(self.fileName))

        self.line=QLabel("  ")
        #SCMB部分
        self.labelsld=QLabel("快速字号调节:1")

        self.slider1 = QSlider(Qt.Horizontal)#水平滑块
        self.slider1.setMinimum(1)
        self.slider1.setMaximum(100)
        self.slider1.setSingleStep(2)
        self.slider1.setValue(1)
        self.slider1.valueChanged.connect(self.valueChange)

        self.copybutton=QPushButton("复制全部文本")
        self.copybutton.clicked.connect(self.copyword)
        #状态栏
        self.textStateE=QTextEdit()
        self.textStateE.setText(self.stateText)
        self.textStateE.setObjectName("texte")

        self.fmbutton=QPushButton("点击投喂作者")
        self.fmbutton.clicked.connect(self.lath)

        self.csbutton=QPushButton("点击切换风格")
        self.csbutton.clicked.connect(self.ccss)
        #面板规划###########################################
        self.panel=QFrame()
        self.panel.setFrameShape(QFrame.StyledPanel)
        self.panelLayout = QVBoxLayout(self.panel)
        #布局控件添加组
        self.panelLayout.addWidget(self.buttonLoad)
        self.panelLayout.addWidget(self.labelcb)
        self.panelLayout.addWidget(self.cb)
        self.panelLayout.addWidget(self.customeButton)
        self.panelLayout.addWidget(self.labelwidth)
        self.panelLayout.addWidget(self.sliderw)
        self.panelLayout.addWidget(self.labelheight)
        self.panelLayout.addWidget(self.sliderh)
        self.panelLayout.addWidget(self.checkNewline)
        self.panelLayout.addWidget(self.checkAnnotation1)
        self.panelLayout.addWidget(self.checkAnnotation2)
        self.panelLayout.addWidget(self.checkAnnotation3)
        self.panelLayout.addWidget(self.checkAnnotation4)

        self.panelLayout.addWidget(self.line)

        self.panelLayout.addWidget(self.labelsld)
        self.panelLayout.addWidget(self.slider1)
        self.panelLayout.addWidget(self.copybutton)
        self.panelLayout.addWidget(self.textStateE)
        self.panelLayout.addWidget(self.fmbutton)
        self.panelLayout.addWidget(self.csbutton)

        self.spt = QSplitter(Qt.Horizontal)
        self.spt.addWidget(self.text)
        self.spt.addWidget(self.panel)
        self.spt.setStretchFactor(0, 6)
        self.spt.setStretchFactor(1, 1)

        formlayout.addWidget(self.spt)
        self.setLayout(formlayout)
        self.showMaximized()

    def loadCharList(self):
        #读取txt文件中的上色字符串,放到comboBox cb里面
        with open("support/charList.txt","r",encoding='utf-8')as f:
            temp=f.read()
            self.charList=temp.split(",")
    
    def loadQss(self,stname):
        try:
            styleFile=stname
            qssStyle= CommonQssLoader.readCss(styleFile)
            self.setStyleSheet(qssStyle)
        except:
            pass

    def loadImage(self):
        self.fileNameSaved=self.fileName
        self.fileName,_=QFileDialog.getOpenFileName(self,"打开文件","support/Images","图像文件(*.jpg *.png *bmp)")
        self.changepictures(self.fileName)
        if self.fileName=="":#防止已经有图片载入后打开导入框但是又没有选择导致filename清空
            self.fileName=self.fileNameSaved

    def changepictures(self,path):
        try:
            img = Image.open(path)
            out = img.convert("L")
            owidth, oheight = out.size
            proportion=math.sqrt(self.customArea)/math.sqrt((owidth*oheight))
            width=owidth*proportion
            height=oheight*proportion
            out = out.resize((int(width*(self.sliderw.value()/1000)*8+2), int(height*(self.sliderh.value()/1000)*8+2)))
            width, height = out.size
            ascii = self.cb.currentText()
            textout = ""
            for row in range(height):
                if self.checkAnnotation1.isChecked():
                    textout+="'"
                if self.checkAnnotation2.isChecked():
                    textout+="//"
                if self.checkAnnotation3.isChecked():
                    textout+="#"
                if self.checkAnnotation4.isChecked():
                    textout+="<!--"
                #BODY-PART
                for col in range(width):
                    gray = out.getpixel((col, row))
                    textout += ascii[int(gray / 255 * 7)]
                if self.checkNewline.isChecked():
                    textout+="\\n"
                if self.checkAnnotation4.isChecked():
                    textout+="-->"
                textout += "\n"
            self.text.setText(textout)
            textOutput="\n"+path+"\n宽度="+str(width)+";高度="+str(height)+\
                        "\n原始宽度="+str(owidth)+";原始高度="+str(oheight)+"\n上色字符串="+ascii+"\n"
            self.stateText+=textOutput
            self.textStateE.setText(self.stateText)
            self.textStateE.moveCursor(QTextCursor.End)
        except:
            pass
        finally:
            self.labelwidth.setText("调节图像宽度:" + str(self.sliderw.value()) )
            self.labelheight.setText("调节图像高度:" + str(self.sliderh.value()) )

    def valueChange(self):
        size =self.slider1.value()
        self.text.setFont(QFont("微软雅黑",size))
        self.labelsld.setText("快速字号调节:" + str(self.slider1.value()))

    def copyword(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text.toPlainText())
        self.stateText += "\n文本已复制\n"
        self.textStateE.setText(self.stateText)
        self.textStateE.moveCursor(QTextCursor.End)

    def ccss(self):
        changeStyle()

    def lath(self):
        showChild()

    def showCT(self):
        showCustomText()

    def closeEvent(self, event):
        app = QApplication.instance()  # 退出应用程序
        app.quit()

class ShowEXP(QWidget):
    def __init__(self):
        super(ShowEXP, self).__init__()
        self.setWindowOpacity(0.9)

        self.setWindowIcon(QIcon("support/Images/vezzzinge.png"))
        self.setWindowTitle("微信扫一扫投喂作者")
        self.resize(290,260)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)

        formlayout = QVBoxLayout()

        self.label=QLabel()
        img = QImage("support/FDA/1.png")
        result = img.scaled(260, 260,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.label.setPixmap(QPixmap.fromImage(result))

        formlayout.addWidget(self.label)
        self.setLayout(formlayout)

    def center(self):#窗口居中函数
        screen=QDesktopWidget().screenGeometry()#得到屏幕坐标
        size=self.geometry()#得到窗口坐标系
        newLeft=int((screen.width()-size.width())/2)
        newTop=int((screen.height()-size.height())/2)
        self.move(newLeft,newTop)

class CustomText(QWidget):
    def __init__(self):
        super(CustomText, self).__init__()

        self.setWindowIcon(QIcon("support/Images/vezzzinge.png"))
        self.setWindowTitle("自定义上色字符串")
        self.resize(490,60)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)

        formlayout = QHBoxLayout()

        self.label=QLabel("自定义上色字符串")
        self.char1=QLineEdit()
        self.char2=QLineEdit()
        self.char3=QLineEdit()
        self.char4=QLineEdit()
        self.char5=QLineEdit()
        self.char6=QLineEdit()
        self.char7=QLineEdit()
        self.char8=QLineEdit()
        self.confirmButton=QPushButton("确定")
        self.confirmButton.clicked.connect(self.processChar)

        formlayout.addWidget(self.label)
        formlayout.addWidget(self.char1)
        formlayout.addWidget(self.char2)
        formlayout.addWidget(self.char3)
        formlayout.addWidget(self.char4)
        formlayout.addWidget(self.char5)
        formlayout.addWidget(self.char6)
        formlayout.addWidget(self.char7)
        formlayout.addWidget(self.char8)
        formlayout.addWidget(self.confirmButton)

        self.setLayout(formlayout)

    def processChar(self):
        if len(self.char1.text())*len(self.char2.text())*len(self.char3.text())*len(self.char4.text())*len(self.char5.text())*len(self.char6.text())*len(self.char7.text())*len(self.char8.text())==1:
            currentChar=self.char1.text()+self.char2.text()+self.char3.text()+self.char4.text()+self.char5.text()+self.char6.text()+self.char7.text()+self.char8.text()
            addChar(currentChar)
            self.char1.setText("")
            self.char2.setText("")
            self.char3.setText("")
            self.char4.setText("")
            self.char5.setText("")
            self.char6.setText("")
            self.char7.setText("")
            self.char8.setText("")
            self.hide()
        else:
            self.setWindowTitle("有字符不为一位!!")

    def center(self):#窗口居中函数
        screen=QDesktopWidget().screenGeometry()#得到屏幕坐标
        size=self.geometry()#得到窗口坐标系
        newLeft=int((screen.width()-size.width())/2)
        newTop=int((screen.height()-size.height())/2)
        self.move(newLeft,newTop)

if __name__=="__main__":    
    app=QApplication(sys.argv)
    main=QFileDialogEXPForm()
    child=ShowEXP()
    customText=CustomText()

    allFile=os.listdir("support/QssFile")
    totalState= len(allFile)
    state=1

    main.show()

    def showChild():
        child.show()
        child.center()

    def showCustomText():
        customText.show()
        customText.center()

    def changeStyle():
        global state#这是个坑
        if state==totalState:
            state=1
        else:
            state+=1
        loadQss("support/QssFile/"+allFile[state-1])

    def loadQss(stname):
        try:
            styleFile=stname
            qssStyle= CommonQssLoader.readCss(styleFile)
            main.setStyleSheet(qssStyle)
            child.setStyleSheet(qssStyle)
            customText.setStyleSheet(qssStyle)
        except:
            pass

    def addChar(charAdded):
        main.cb.clear()
        main.cb.addItem(charAdded)
        main.cb.addItems(main.charList)

    sys.exit(app.exec_())