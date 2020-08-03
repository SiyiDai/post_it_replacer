from PyQt5.QtCore import QThread, pyqtSignal

from dialogs.open_load_dialog import OpenLoadDialog
import os

class LoadingThread(QThread):
    done_signal = pyqtSignal()
    progress_signal = pyqtSignal(str, int)

    def __init__(
        self,
        replace_image_path,
        original_picture_path,
        original_video_path,
        **kwargs
    ):
        QThread.__init__(self)
        # input data
        self.replace_image_path = replace_image_path
        self.original_picture_path = original_picture_path
        self.original_video_path = original_video_path

    def run(self):
        if self.is_path_valid(self.replace_image_path):
            self.progress_signal.emit("loading replace image ... ", 10)

            if self.is_path_valid(self.original_picture_path):
                self.progress_signal.emit("loading original picture ... ", 50)

            if self.is_path_valid(self.original_video_path):
                self.progress_signal.emit("loading original video ...", 60)

        self.progress_signal.emit("finished ... ", 100)
        self.done_signal.emit()

    @staticmethod
    def is_path_valid(file_path: str):
        return file_path is not None and os.path.exists(file_path)
