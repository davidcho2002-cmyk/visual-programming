import sys

from PySide6.QtWidgets import (
        QApplication, QMainWindow,
        QWidget, QPushButton, QLabel, QVBoxLayout,
        QInputDialog)

class MW (QMainWindow):

    def __init__(self):
        super(MW, self).__init__()

        # UI 구성을 별도의 method로 분리.
        self.init_ui()

        # main window를 화면에 표시.
        self.show()

    def init_ui(self):

        # QInputDialog.getInt()를 실행하기 위한 button.
        self.button0 = QPushButton('Test.')

        # button이 clicked signal을 발생시키면 slot00()이 호출됨.
        self.button0.clicked.connect(self.slot00)

        # 사용자가 입력한 정숫값을 표시할 label.
        self.ret_label = QLabel()

        # button과 label을 위에서 아래로 배치하기 위한 layout.
        layout = QVBoxLayout()
        layout.addWidget(self.button0)
        layout.addWidget(self.ret_label)

        # layout을 담을 QWidget을 만들고,
        # 이를 QMainWindow의 central widget으로 사용함.
        tmp = QWidget()
        tmp.setLayout(layout)

        self.setCentralWidget(tmp)

    def slot00(self):
        # 현재 slot을 호출한 sender object를 확인.
        print(self.sender())

        sender = self.sender()

        if sender == self.button0:

            # 정수 입력을 위한 dialog를 실행.
            ret_int, is_ok = QInputDialog.getInt(
                    self,                    # parent widget
                    "Input Integer",         # dialog title
                    "Enter Your Int Value!", # input field 위의 label text
                    0,                       # 기본값
                    0, 100,                  # 입력 가능한 최솟값, 최댓값
                    3,                       # 증가/감소 단위
                    )

            # 사용자가 OK를 누른 경우에만 입력값을 사용함.
            if is_ok:
                # 입력받은 integer를 label에 표시.
                self.ret_label.setText(f'{ret_int}')

if __name__ == "__main__":
    # Qt application 객체 생성.
    app = QApplication(sys.argv)

    # main window 생성.
    mw = MW()

    # Qt event loop 실행.
    sys.exit(app.exec())
