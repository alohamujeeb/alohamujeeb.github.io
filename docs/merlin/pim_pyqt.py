import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QListWidget, QListWidgetItem
from PyQt5.QtCore import QTimer

class NetworkMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Physical Interface Monitor")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        layout.addWidget(QLabel("Interface Status"))
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_status)
        self.timer.start(1000)  # refresh every 1 seconds

        self.update_status()

    def update_status(self):
        self.list_widget.clear()
        stats = psutil.net_if_stats()
        addrs = psutil.net_if_addrs()

        # Filter only physical interfaces
        for iface, stat in stats.items():
            if iface.startswith(("lo", "docker", "veth", "br", "virbr", "vmnet")):
                continue

            connected = "Connected" if stat.isup else "Disconnected"
            item_text = f"{iface}: {connected}"
            QListWidgetItem(item_text, self.list_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NetworkMonitor()
    window.show()
    sys.exit(app.exec_())
