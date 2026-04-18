# labels.py
import sys
import os

try:
    from PySide6.QtWidgets import QApplication, QWidget, QLabel
    from PySide6.QtGui import QFont, QPixmap
    from PySide6.QtCore import Qt
    qt_modules = 'PySide6'
except ImportError:
    try:
        from PyQt6.QtWidgets import QApplication, QWidget, QLabel
        from PyQt6.QtGui import QFont, QPixmap
        from PyQt6.QtCore import Qt
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
        self.setGeometry(100, 100, 250, 200)  # 위치 (100, 100), 크기 250x200
        self.setFixedSize(250, 200)            # 창 크기 고정 - absolute positioning 사용 시 권장
        self.setWindowTitle('QLabel Example')
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        # text label 생성
        # 아래 한 줄로도 동일하게 생성 가능
        # hello_label = QLabel('Hello, World and Qt!', self)
        hello_label = QLabel(self)
        hello_label.setText('Hello, World and Qt!')
        hello_label.setFont(QFont('Arial', 15))
        hello_label.move(10, 10)

        # 아래 두 줄을 주석 해제하여 동작 확인 가능
        # hello_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # hello_label.setStyleSheet("background-color: yellow")

        # image label 생성
        # 스크립트 파일 위치를 기준으로 image 경로를 계산함
        path_py_file = os.path.dirname(os.path.realpath(__file__))
        img_path = os.path.join(path_py_file, 'img/world.png')

        if os.path.exists(img_path):
            world_label = QLabel(self)
            pixmap = QPixmap(img_path)
            # scaled()는 새로운 QPixmap을 반환함 - in-place 변환이 아님
            pixmap = pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio)
            world_label.setPixmap(pixmap)
            world_label.move(25, 40)
        else:
            print(f'Image not found: {img_path}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
