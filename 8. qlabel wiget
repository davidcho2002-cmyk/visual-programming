import sys

try:
    from PySide6.QtWidgets import (
        QApplication, QWidget, QLineEdit,
        QPushButton, QVBoxLayout, QHBoxLayout, QLabel,
    )
    from PySide6.QtCore import Qt
except ImportError:
    from PyQt6.QtWidgets import (
        QApplication, QWidget, QLineEdit,
        QPushButton, QVBoxLayout, QHBoxLayout, QLabel,
    )
    from PyQt6.QtCore import Qt


class MW(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QLineEdit - Edit Operations Test")
        self.setup_main_wnd()
        self.show()

    def setup_main_wnd(self):
        lm = QVBoxLayout()

        lm.addWidget(QLabel("Input:"))
        self.le = QLineEdit()
        self.le.setPlaceholderText("텍스트를 입력하고 드래그로 선택 후 버튼을 눌러보세요.")
        lm.addWidget(self.le)

        # 각 버튼 → 해당 method 직접 연결
        btn_layout = QHBoxLayout()
        for label, slot in [
            ("cut",   self.le.cut),
            ("copy",  self.le.copy),
            ("paste", self.le.paste),
            ("undo",  self.le.undo),
            ("redo",  self.le.redo),
        ]:
            btn = QPushButton(label)
            # button에 포커스를 뺏기면 선택영역이 사라지므로 다음 처리 필요.
            btn.setFocusPolicy(Qt.FocusPolicy.NoFocus) #windows and linux
            btn.clicked.connect(slot)
            btn_layout.addWidget(btn)

        lm.addLayout(btn_layout)

        # undo / redo 가능 여부를 실시간으로 표시
        self.status_label = QLabel("undo: -, redo: -")
        lm.addWidget(self.status_label)
        self.le.textChanged.connect(self.update_status)

        self.setLayout(lm)

    def update_status(self):
        undo_ok = self.le.isUndoAvailable()
        redo_ok = self.le.isRedoAvailable()
        self.status_label.setText(
            f"undo available: {undo_ok}  |  redo available: {redo_ok}"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = MW()
    sys.exit(app.exec())
