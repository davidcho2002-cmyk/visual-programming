import sys

from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QMainWindow,
    QMessageBox,
    QPushButton,
)


class MW(QMainWindow):

    def __init__(self):                         #오픈파일이라는 버튼을 가운데 만들고 탐색창 하나 만들기 
        super().__init__()

        self.setWindowTitle("QFileDialog.getOpenFileName Example")

        # button을 central widget으로 설정함.
        # button을 누르면 단일 file 선택 dialog가 표시됨.
        button = QPushButton("Open File", self)
        button.clicked.connect(self.open_file)

        self.setCentralWidget(button)                                   #버튼 중앙에 둘거야 
        self.show()                                                 #보여줘 

    def open_file(self):                                        #오픈파일함수 새로 명명 
        # 단일 file을 선택하는 dialog.
        # 반환값은 file path 문자열과 선택된 filter 문자열임.
        file_name, selected_filter = QFileDialog.getOpenFileName(                       #파일찾는 클래스 가져오기 
            self,                              # parent widget                          #자식창 탐색기, 부모창 푸쉬버튼 
            "Open file",                       # dialog title
            "",                                # start directory            #이 코드가 있는 현 위치에서 탐색기 시작 
            "Text files (*.txt *.html *.py);;All files (*.*)",              #탐색기에서 제한하는 보여지는 파일들 
        )

        # 사용자가 Cancel을 누르면 file_name은 빈 문자열임.
        if file_name:                                                   #파일 이름이 선택되었다면 
            QMessageBox.information(                                    #이하 함수에 올린다 
                self,   
                "Selected File",                                            #파일 선택하면 경로랑, 확장자명 알려주기 
                f"File: {file_name}\nFilter: {selected_filter}",
            )


if __name__ == "__main__":                                  #종료 
    app = QApplication(sys.argv)

    window = MW()

    sys.exit(app.exec())
