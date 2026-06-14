import sys
import time

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class WorkerThread(QThread):
    # worker thread에서 GUI thread로 문자열 message를 전달하기 위한 signal.
    update_signal = Signal(str)             #업데이트 시그널을 가지고 받겠다 

    def run(self):                      #런에 대한 함수 서술하게요 
        # 이 method는 start() 호출 후 새 thread 안에서 실행됨.
        # 직접 run()을 호출하면 새 thread가 생성되지 않으므로 주의해야 함.
        for i in range(5):                      #0,1,2,3,4, 차례로 i에 넣겠다 
            time.sleep(1)                       #1초동안 멈추겠다       화면을 멈추는거지 일하는 쓰레드가 멈추는 것은 아니다 
            self.update_signal.emit(f"Working {i + 1}")  # 진행 상태를 GUI thread로 전달./ 스레드가 한번씩 멈추는 거에 대해서 한번멈추면 워킹 1, 두번멈추면 워킹 2, ... 이런식으로 움직이게 된다. 

        # 작업 완료 message를 GUI thread로 전달.
        self.update_signal.emit("Task completed!")          #신호 방출 시 task completed라고 보내주기 


class MW(QWidget):                      #메인 윈도우 서술 
    def __init__(self):                 
        super().__init__()          #기본값 설정 

        self.setWindowTitle("QThread Example")      #제목 

        self.init_ui()                  #이거 할거요 
        self.show()

    def init_ui(self):                  
        # GUI widget 생성.
        self.label = QLabel("Thread Example", self)     #라벨에 대해서 스레드 이그젬플 서술 
        self.button = QPushButton("Start Thread", self)    #버튼에 이거 써 주겠다 

        # button click 시 worker thread 시작.
        self.button.clicked.connect(self.start_thread)      #버튼 눌리면 이 함수 실행시키겠다 

        # layout 설정.
        layout = QVBoxLayout(self)              #도장꽝 
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # QThread를 상속한 worker thread 객체 생성.
        self.worker = WorkerThread()                #이 클래스를 변수에 지정 

        # worker thread에서 발생한 signal을 GUI thread의 slot에 연결.
        # update_label()은 GUI thread에서 호출되므로 QLabel을 안전하게 update할 수 있음.
        self.worker.update_signal.connect(self.update_label)    #업데이트 라벨 이랑 연결시키기 

    def start_thread(self):                         #업데이트 라벨이라는 함수에 연결할 것 
        # 이미 thread가 실행 중이면 다시 시작하지 않음.
        # QThread를 중복 실행하는 것을 방지하기 위한 처리임.
        if not self.worker.isRunning():            #스레드가 작동 안하면 작동 시키겠다. 
            self.worker.start()                     

    def update_label(self, message):                #위에서 업무 완료 이런 메시지들 받아서 라벨에서 보여주겠다
        # GUI widget은 GUI thread에서 update해야 함.
        # worker thread는 직접 QLabel을 수정하지 않고 signal만 emit함.
        self.label.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)            #종료 

    wnd = MW()

    sys.exit(app.exec())
