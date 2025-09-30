import sys

from PyQt5 import QtWidgets

from app.config import ConfigManager
from app.db import Database
from app.webhook_server import WebhookServerThread
from app.whatsapp_api import WhatsAppClient
from app.gui import MainWindow


def main() -> int:
    config = ConfigManager("config.json")
    db = Database("data.db")

    webhook = WebhookServerThread(config, db)
    webhook.start()

    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName("WhatsApp Sender")

    client = WhatsAppClient(config, db)
    window = MainWindow(config=config, db=db, client=client)
    window.show()

    return app.exec_()


if __name__ == "__main__":
    raise SystemExit(main())


