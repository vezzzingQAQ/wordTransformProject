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
        self.stateText="Welcome!\nVersion 1.0.1 By Vezzzing I.D.S\n"
        self.customArea=120000

        self.allFile=os.listdir("QssFile")
        self.totalState= len(self.allFile)
        self.state=1

        self.loadQss("QssFile/QssBright.qss")
        self.initUI()

    def initUI(self):
        self.setWindowTitle("●I.T.W.V1.0.2!!!∑(ﾟДﾟノ)ノ")
        self.setWindowIcon(QIcon("Images/vezzzinge.png"))
        formlayout=QHBoxLayout()

        self.text=QTextEdit("最后会在这里显示")
        self.text.setFont(QFont("微软雅黑",1))
        # 右侧面板##########################################
        self.buttonLoad = QPushButton("导入图片")
        self.buttonLoad.clicked.connect(self.loadImage)

        self.cb=QComboBox()
        self.cb.addItems(["█▉▊▋▌▍▎▏",
                          "█▇▆▅▄▃▂▁",
                          "■■■■□□□□",
                          "◆◆◆◆◇◇◇◇",
                          "●●●●○○○○",
                          "♥♥♥♥♡♡♡♡",
                          "++++----",
                          "☀☀☀☀☼☼☼☼",
                          "▩▩▦▥▧▨▤▤",
                          "██▓▓▒▒░░",
                          "灏巰离水大三二一",
                          "䭨得我水火人二一",
                          "■■■■    "])
        #如果已经选择了图片，自动切换：

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

        self.csbutton=QPushButton("点击切换界面")
        self.csbutton.clicked.connect(self.ccss)
        #面板规划###########################################
        self.panel=QFrame()
        self.panel.setFrameShape(QFrame.StyledPanel)
        self.panelLayout = QVBoxLayout(self.panel)
        #布局控件添加组
        self.panelLayout.addWidget(self.buttonLoad)
        self.panelLayout.addWidget(self.labelcb)
        self.panelLayout.addWidget(self.cb)
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

    def loadQss(self,stname):
        try:
            styleFile=stname
            qssStyle= CommonQssLoader.readCss(styleFile)
            self.setStyleSheet(qssStyle)
        except:
            pass

    def loadImage(self):
        self.fileNameSaved=self.fileName
        self.fileName,_=QFileDialog.getOpenFileName(self,"打开文件","Images","图像文件(*.jpg *.png *bmp)")
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
        try:
            if self.state==self.totalState:
                self.state=1
            else:
                self.state+=1
            self.loadQss("QssFile/"+self.allFile[self.state-1])
        except:
            pass

    def lath(self):
        showChild()

    def closeEvent(self, event):
        app = QApplication.instance()  # 退出应用程序
        app.quit()

class ShowEXP(QWidget):
    def __init__(self):
        super(ShowEXP, self).__init__()
        self.setWindowOpacity(0.9)

        self.setWindowIcon(QIcon("Images/vezzzinge.png"))
        self.setWindowTitle("微信扫一扫投喂作者")
        self.resize(290,260)
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowStaysOnTopHint)

        formlayout = QVBoxLayout()

        self.label=QLabel()
        img = QImage("FDA/1.png")
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

if __name__=="__main__":
    app=QApplication(sys.argv)
    main=QFileDialogEXPForm()
    child=ShowEXP()
    main.show()

    def showChild():
        child.show()
        child.center()

    sys.exit(app.exec_())