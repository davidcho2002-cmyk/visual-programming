import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MW(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("QFileDialog.getExistingDirectory Example")

        # button을 누르면 directory 선택 dialog가 표시됨.
        button = QPushButton("Open Directory", self)
        button.clicked.connect(self.open_directory)

        self.setCentralWidget(button)
        self.show()

    def open_directory(self):
        # directory를 선택하는 dialog.
        directory_path = QFileDialog.getExistingDirectory(
            self,
            "Select a Directory",
            "",
            QFileDialog.Option.ShowDirsOnly,
        )

        # 사용자가 directory를 선택한 경우 directory_path는 빈 문자열이 아님.
        if directory_path:
            QMessageBox.information(
                self,
                "Selected Directory",
                f"Directory: {directory_path}",
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MW()

    sys.exit(app.exec())
