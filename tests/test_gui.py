import sys
import unittest
from PyQt6.QtWidgets import QApplication
from evo_downloader.gui import DownloaderGUI


class TestDownloaderGUI(unittest.TestCase):
    def setUp(self):
        self.app = QApplication(sys.argv)
        self.gui = DownloaderGUI()

    def test_initial_ui_state(self):
        self.assertEqual(self.gui.url_input.toPlainText(), "")
        self.assertEqual(self.gui.folder_input.text(), "")
        self.assertEqual(self.gui.progress_bar.value(), 0)

    def test_select_folder(self):
        self.gui.folder_input.setText("/test/download_folder")
        self.assertEqual(self.gui.folder_input.text(), "/test/download_folder")

    def test_start_download(self):
        self.gui.url_input.setPlainText("http://images.cocodataset.org/annotations/image_info_test2014.zip\nhttps://github.com/maycuatroi/evo_downloader/archive/refs/heads/main.zip")
        self.gui.folder_input.setText("/test/download_folder")
        self.gui.start_download()
        self.assertEqual(self.gui.progress_bar.value(), 0)  # Initial progress should be 0

    def tearDown(self):
        self.app.quit()


if __name__ == "__main__":
    unittest.main()
