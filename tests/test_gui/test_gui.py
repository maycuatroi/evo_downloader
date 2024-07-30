import unittest

from PyQt5.QtCore import Qt
from evo_downloader.gui import DownloaderGUI


def test_start_download(qtbot):
    gui = DownloaderGUI()
    qtbot.addWidget(gui)
    gui.url_input.setPlainText(
        "http://images.cocodataset.org/annotations/image_info_test2014.zip\nhttps://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip"
    )

    gui.folder_input.setText("./test/download_folder")
    qtbot.mouseClick(gui.download_button, Qt.MouseButton.LeftButton)
    gui.download_thread.wait()


if __name__ == "__main__":
    unittest.main()
