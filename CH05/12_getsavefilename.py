import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,                                #시작이요 
    QPushButton,
)


class MW(QMainWindow):                          #메인윈도우 기본 설정이요 

    def __init__(self): 
        super().__init__()

        self.setWindowTitle("QFileDialog.getSaveFileName Example")

        # button을 누르면 저장할 file path를 선택하는 dialog가 표시됨.
        button = QPushButton("Save File", self)
        button.clicked.connect(self.save_file)

        self.setCentralWidget(button)
        self.show()

    def save_file(self):
        # 저장할 file path를 선택하는 dialog.
        # 이 method는 실제 저장을 수행하지 않고, 저장할 path만 반환함.
        file_name, selected_filter = QFileDialog.getSaveFileName(
            self,
            "Save file",
            "",
            "Text files (*.txt);;Python files (*.py);;All files (*.*)",
        )

        # 사용자가 Cancel을 누르면 file_name은 빈 문자열임.
        if file_name:                                                   #파일을 열었다면 
            # 실제 file 저장은 반환된 path를 이용하여 직접 수행해야 함.          #파일을 열고, 파일을 이후에 자동으로 닫아주는
            with open(file_name, "w", encoding="utf-8") as f:           #파일을 가져와서 열고, 새로운 글 쓸거야, 문자인코딩   
                f.write("Hello QFileDialog\n")                          #파일 내부 이하로 바꾸기 
                f.write(f"Selected filter: {selected_filter}\n")        #파일 내부 그 다음줄 에 이하 작성 

            QMessageBox.information(                                    #메시지 박스에다가 이하 내용 작성, 그리고 작성한 것 저장하기 
                self,
                "Saved",
                f"File saved to:\n{file_name}",
            )


if __name__ == "__main__":                  #종료 
    app = QApplication(sys.argv)

    window = MW()

    sys.exit(app.exec())
