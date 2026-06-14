import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMessageBox,
)


class MW(QMainWindow):
    def __init__(self):
        super().__init__()

        # main window의 title 설정.
        self.setWindowTitle("QMessageBox.question Example")

        # dialog를 띄우기 위한 button 생성.
        button = QPushButton("Press me for a dialog!", self)

        # button 클릭 시 button_clicked method가 호출되도록 signal-slot 연결.
        button.clicked.connect(self.button_clicked)

        # button을 main window의 central widget으로 지정.
        self.setCentralWidget(button)

        # main window 표시.
        self.show()

    def button_clicked(self, checked):
        # button click signal에서 전달된 checked 상태 출력.
        print("click", checked)

        # question dialog 표시.
        # Yes와 No button을 제공하고, 기본 선택 button은 Yes로 지정함.
        response = QMessageBox.question(
            self,
            "Question Message",
            "Do you like PySide6?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.Yes,
        )

        # 사용자가 선택한 button에 따라 분기.
        if response == QMessageBox.StandardButton.Yes:
            print("User likes PySide6!")
        else:
            print("User does not like PySide6!")

        # 사용자가 누른 button 값 출력.
        print("Dialog result:", response)


if __name__ == "__main__":
    # Qt application instance 생성.
    app = QApplication(sys.argv)

    # main window instance 생성.
    wnd = MW()

    # Qt event loop 실행.
    app.exec()
