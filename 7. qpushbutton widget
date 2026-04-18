# ds_button.py
import sys
import os

try:
    from PySide6.QtWidgets import (
        QApplication, QWidget,
        QLabel, QPushButton,
    )
    from PySide6.QtGui import QFont, QIcon
    from PySide6.QtCore import Qt, QSize
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import (
            QApplication, QWidget,
            QLabel, QPushButton,
        )
        from PyQt6.QtGui import QFont, QIcon
        from PyQt6.QtCore import Qt, QSize
        qt_modules = 'PyQt6'
    except ImportError:
        print("PySide6 또는 PyQt6가 설치되어 있지 않습니다.")
        sys.exit(1)

print(f"Using {qt_modules} binding.")


class MW(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QPushButton Example')
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        # text label - slot에서 접근하므로 instance attribute로 생성
        self.hello_label = QLabel(self)
        self.hello_label.setText('Hello, World and Qt!')
        self.hello_label.setFont(QFont('Arial', 15))
        self.hello_label.resize(230, 40)
        self.hello_label.move(10, 20)

        # 아래 줄을 주석 해제하여 정렬 / 배경색 동작 확인 가능
        # self.hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # PySide6 / PyQt6 모두 동작
        # self.hello_label.setAlignment(Qt.AlignCenter)                # PySide6 전용 (하위 호환)
        # self.hello_label.setStyleSheet("background-color: yellow")

        # 스크립트 위치 기준으로 image 경로 계산
        base_dir = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(base_dir, 'img/world.png')

        # icon + text 버튼
        it_button = QPushButton("icon and text button", self)
        it_button.setIcon(QIcon(img_path))
        it_button.clicked.connect(self.it_btn_clicked)
        it_button.resize(150, 50)
        it_button.move(50, 70)

        # icon 전용 버튼 (text 없음)
        icon_button = QPushButton(self)
        icon_button.setIcon(QIcon(img_path))
        icon_button.setIconSize(QSize(120, 30))  # icon 크기 명시적으로 고정
        icon_button.clicked.connect(self.icon_btn_clicked)
        icon_button.resize(150, 50)
        icon_button.move(50, 130)

        # text 전용 버튼 (icon 없음)
        text_button = QPushButton("text button", self)
        text_button.clicked.connect(self.text_btn_clicked)
        text_button.resize(150, 50)
        text_button.move(50, 190)

    def it_btn_clicked(self):
        """icon + text 버튼 클릭 시 호출됨."""
        self.hello_label.setText("Icon and text Button")

    def icon_btn_clicked(self):
        """icon 전용 버튼 클릭 시 호출됨."""
        self.hello_label.setText("Icon Button")

    def text_btn_clicked(self):
        """text 전용 버튼 클릭 시 호출됨."""
        self.hello_label.setText("text Button")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
