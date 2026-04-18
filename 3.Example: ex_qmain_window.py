# -*- coding: utf-8 -*-
#
# ex_qmain_window.py
#
# Description: QMainWindow를 상속받아 메인 윈도우를 생성하고,
#              여러 위젯을 담은 컨테이너를 Central Widget으로 설정하는
#              표준적인 방법을 보여주는 예제.
# Author: dsaint31
# Date: 2024-04-23
#

# 1. 필요한 library 및 module을 import 하기
import sys                                                                            #시스템이랑 연동 
import os                                                                             #os건드릴거 

# PySide6/PyQt6 사용을 확인하기 위한 flag
PYSIDE = False                                                                        #변수지정하고 false 초기 설정 
PYQT = False                                                                          #

# PySide6를 우선적으로 import 하도록 시도
try:                                                                                 #try 예외처리 
    from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,               #시도하기 파이사이드6의 큐티 위젯안에서 큐어플, 큐메인, 큐윈동, 큐라벨, qb박스레이아웃 가져오기  
                                   QLabel, QVBoxLayout)
    from PySide6.QtGui import QIcon                                                  #파이사이드 6.큐티 지유아이에서 qicon가져오기 
    PYSIDE = True                                                                    #파이사이드를 flase 에서 true로 바꾸기 
except ImportError:                                                                  #불러오기가 실패 시 넘기자 
    pass

# PySide6 import에 실패했을 경우, PyQt6를 import 하도록 시도
if not PYSIDE:                                                                      #파이사이드가 아닌경우 
    try:
        from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,          #파이큐티 불러오고 큐티 위젯안에서 큐어플, 큐메인, 큐윈동, 큐라벨, qb박스레이아웃 가져오기  
        from PySide6.QtGui import QIcon                                             #파이사이드 qtgui에서 qicon가져오기 
        PYQT = True
    except ImportError:
        pass

# QMainWindow를 상속받아 메인 윈도우 class를 정의.
# QMainWindow는 메뉴바, 툴바, 상태바 등을 포함할 수 있는 표준적인 메인 윈도우용 클래스.
class MW(QMainWindow):                                                              # 아래 코드에 대해서 클래스 MW라고 생각해보자 그 토대를 '큐메인윈도우'로 사용   
    def __init__(self):
        """ 생성자(Constructor) """
        # 부모 class인 QMainWindow의 생성자를 호출
        super().__init__()
        # UI 초기화를 위해 user-defined method 호출
        self.initialize_ui()

    def initialize_ui(self):
        """Application의 UI 설정을 담당"""

        # 윈도우의 최소 크기를 400x500으로 설정
        self.setMinimumSize(400, 500) #width, height
        # 윈도우의 title bar에 보일 text를 설정
        self.setWindowTitle("Title of Main Window")

        # 아이콘 이미지 경로 설정
        # __file__은 현재 스크립트의 경로임
        # (pyinstaller로 실행파일 만들시 동작X).
        # os.path.abspath 로 절대경로를 만들고,
        # os.path.dirname 으로 디렉토리 경로를 추출하여
        # 'img/pyqt_logo.png' 경로를 조합.
        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'img/pyqt_logo.png'
        )
        # 아이콘 파일이 실제로 존재하는지 확인하여,
        # 있을 경우에만 아이콘을 설정(에러 방지).
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))

        # 메인 윈도우의 central widget을 설정하는 method 호출
        self.setup_main_wnd()

        # 설정된 윈도우를 화면에 표시
        self.show()

    def setup_main_wnd(self):
        """메인 윈도우의 Central Widget을 생성 및 설정"""

        # 1번 과정: Central Widget에 포함될 자식 widget들을 생성
        label0 = QLabel("test0")
        label1 = QLabel("test1")

        # 2번 과정: 자식 widget들을 배치할 Layout Manager를 생성 (QVBoxLayout: 수직 정렬)
        vbox = QVBoxLayout()

        # 3번 과정: Layout Manager에 자식 widget들을 추가
        vbox.addWidget(label0)
        vbox.addWidget(label1)

        # 4번 과정: 자식 widget들과 layout을 담을 container widget(QWidget)을 생성.
        # QMainWindow는 단 하나의 위젯만 Central Widget으로 가질 수 있음.
        # 따라서 여러 위젯을 배치하려면, 이들을 담을 '컨테이너' 위젯이 필요.
        container = QWidget()

        # 5번 과정: 컨테이너 위젯의 내부 레이아웃을 위에서 설정한 수직 박스 레이아웃(vbox)으로 지정
        container.setLayout(vbox)

        # 6번 과정: 메인 윈도우의 Central Widget으로 이 컨테이너 위젯을 설정.
        # 이로써 두 개의 라벨이 윈도우 중앙에 표시.
        self.setCentralWidget(container)

# 3. Main script로 동작하는 루틴 구현
if __name__ == '__main__':
    # PySide6나 PyQt6 모두 사용 불가능할 경우 메시지 출력 후 종료
    if not PYSIDE and not PYQT:
        print("Neither PySide6 nor PyQt6 is available. Please install one.")
        sys.exit(1)

    # 모든 GUI app은 하나의 QApplication instance를 필요로 함
    app = QApplication(sys.argv)
    # Main window(MW)의 instance를 생성
    window = MW()
    # application의 event loop를 시작
    sys.exit(app.exec())
