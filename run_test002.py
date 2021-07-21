import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
import test002  # 导入添加的资源（根据实际情况填写文件名）

app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = test002.Ui_MainWindow()
ui.setupUi(MainWindow)




MainWindow.show()

sys.exit(app.exec_())
