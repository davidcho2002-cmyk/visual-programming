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
        self.setWindowTitle("QMessageBox.information Example")

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

        # information dialog 표시.
        # Ok와 Cancel button을 표시하고, 기본 선택 button은 Ok로 지정함.
        result = QMessageBox.information(
            self,
            "Message",
            "This is an information message.",
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel,
            QMessageBox.StandardButton.Ok,
        )

        # 사용자가 누른 button 값 출력.
        print("Dialog result:", result)


if __name__ == "__main__":
    # Qt application instance 생성.
    app = QApplication(sys.argv)

    # main window instance 생성.
    wnd = MW()

    # Qt event loop 실행.
    app.exec()
