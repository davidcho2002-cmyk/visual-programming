import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QLineEdit, QInputDialog,
        )

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()

        # UI 구성을 별도의 method로 분리.
        self.init_ui()

        # main window를 화면에 표시.
        self.show()

    def init_ui(self):

        # QInputDialog.getText()를 실행하기 위한 button.
        self.button0 = QPushButton('Test.')

        # button이 clicked signal을 발생시키면 slot00()이 호출됨.
        self.button0.clicked.connect(self.slot00)

        # 사용자가 입력한 text를 표시할 label.
        self.ret_label = QLabel()

        # button과 label을 위에서 아래로 배치하기 위한 layout.
        layout = QVBoxLayout()
        layout.addWidget(self.button0)
        layout.addWidget(self.ret_label)

        # QMainWindow에는 layout을 직접 설정하지 않음.
        # QWidget을 하나 만들고, 해당 widget에 layout을 설정한 뒤
        # QMainWindow의 central widget으로 지정함.
        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        # 현재 slot을 호출한 sender object를 확인.
        print(self.sender())

        sender = self.sender()

        # 여러 widget이 같은 slot에 연결될 수 있으므로,
        # 어떤 widget에서 signal이 발생했는지 확인함.
        if sender == self.button0:

            # 한 줄 text 입력을 위한 dialog를 실행.
            ret_text, is_ok = QInputDialog.getText(
                    self,                         # parent widget
                    "Input Text",                 # dialog title
                    "Enter Your Text!",           # input field 위의 label text
                    QLineEdit.PasswordEchoOnEdit, # echo mode
                    "default text!",              # 기본 text 값
                    )

            # 사용자가 OK를 누른 경우에만 입력값을 사용함.
            if is_ok:
                # 입력받은 text를 label에 표시.
                self.ret_label.setText(f'{ret_text}')

if __name__ == "__main__":
    # Qt application 객체 생성.
    app = QApplication(sys.argv)

    # main window 생성.
    mw = MW()

    # Qt event loop 실행.
    sys.exit(app.exec())
