from PyQt5.QtCore import Qt, QItemSelectionModel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QColorDialog
import os
import cv2
import numpy as np
from PIL import Image

from ui_py.ui_mainwindow import Ui_MainWindow
from dialogs.open_load_dialog import OpenLoadDialog
from dialogs.saved_values_paths import SavedValuesConstants
from dialogs.loader import LoadingThread

REPLACED_FILE_NAME = "savedImage.jpg"
COLOR_RANGE = 20


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # setup ui layout
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # register event handlers
        self.ui.radioButton_camera.toggled.connect(self.__refresh_ui)
        self.ui.radioButton_picture.toggled.connect(self.__refresh_ui)
        self.ui.radioButton_video.toggled.connect(self.__refresh_ui)
        self.ui.actionLoader.triggered.connect(self.on_action_loader_triggered)
        self.ui.pushButton_replace.pressed.connect(self.show_replace_result)
        self.ui.post_it_color_pushButton.pressed.connect(self.on_action_settings_color_picker_triggered)

        self.post_it_color_rgb_value = np.array([])

        self.replace_image_path = None
        self.original_picture_path = None
        self.original_video_path = None

        self.__refresh_post_it_color_line_edit()

    def on_action_loader_triggered(self):
        dialog = OpenLoadDialog()
        if not dialog.exec_():
            return

        self.replace_image_path = dialog.replace_image_file_path()
        self.original_picture_path = dialog.original_picture_file_path()
        self.original_video_path = dialog.original_video_file_path()

        self.load_labelled_sequence_thread = LoadingThread(
            replace_image_path=self.replace_image_path,
            original_picture_path=self.original_picture_path,
            original_video_path=self.original_video_path,
        )

        self.load_labelled_sequence_thread.start()
        self.__refresh_ui()

        # self.loading_progress_dialog = QProgressDialog("loading...", None, 0, 100, parent=self)
        # self.loading_progress_dialog.exec_()

    def on_action_settings_color_picker_triggered(self):
        title = "Choose the color of post-it"
        color = self.post_it_color()
        color_pick = QColorDialog.getColor(color, self, title, QColorDialog.ShowAlphaChannel)

        SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT = color_pick

        self.__update_post_it_color()
        self.__refresh_post_it_color_line_edit()

    def show_replace_result(self):
        replace_img = Image.open(self.replace_image_path)
        dir_path = os.path.dirname(os.path.realpath(self.replace_image_path))
        pic_path = self.original_picture_path
        video_path = self.original_video_path
        result_path = dir_path + "/" + REPLACED_FILE_NAME

        if self.ui.radioButton_picture.isChecked:
            self.show_replaced_picture(pic_path, replace_img)

        elif self.ui.radioButton_video.isChecked:
            self.show_replaced_video(video_path, replace_img)

        elif self.ui.radioButton_camera.isChecked:
            self.show_replace_camera_stream(replace_img)

        else:
            print("Unexpected Value of Mode")

        self.__refresh_replaced_result(result_path)

    def show_replaced_picture(self, pic_path, replace_img):
        # Picture, change the post-it part in pic
        cap = cv2.VideoCapture(pic_path)
        ret, frame = cap.read()
        replace_result = self.detect_and_replace(frame.copy(), replace_img)
        cv2.imwrite(REPLACED_FILE_NAME, replace_result)
        # cv2.imshow('original', frame)
        # cv2.imshow('mask', replace_result)
        cap.release()

    def show_replaced_video(self, video_path, replace_img):
        # Video, change the post-it part in video
        cap = cv2.VideoCapture(video_path)
        while True:
            ret, frame = cap.read()
            if frame is not None:
                replace_result = self.detect_and_replace(frame.copy(), replace_img)

                cv2.imshow("original", frame)
                cv2.imshow("mask", replace_result)

                # press 'ESC' to quit
                if cv2.waitKey(100) & 0xFF == 0x1B:
                    break
            else:
                break
        cap.release()

    def show_replace_camera_stream(self, replace_img):
        # Camera, change the post-it part in the camera stream
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            replace_result = self.detect_and_replace(frame.copy(), replace_img)

            cv2.imshow("original", frame)
            cv2.imshow("mask", replace_result)

            # press 'ESC' to quit
            if cv2.waitKey(100) & 0xFF == 0x1B:
                break
        cap.release()

    def detect_and_replace(self, frame, replace_img):
        # lower = self.post_it_color_rgb_value - COLOR_RANGE
        # upper = self.post_it_color_rgb_value + COLOR_RANGE
        lower = np.array([189, 161, 142])
        upper = np.array([229, 201, 184])

        mask = cv2.inRange(frame, lowerb=lower, upperb=upper)

        # find contours
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        try:
            # find biggest bounding box
            biggest, index = 0, 0
            rect = list()
            for i in range(len(contours)):
                x, y, w, h = cv2.boundingRect(contours[i])
                rect.append(((x, y), (x + w, y + h), (w, h)))
                if w * h > biggest:
                    biggest = w * h
                    index = i

            # draw bounding box in captured image
            frame = cv2.rectangle(frame, rect[index][0], rect[index][1], (0, 0, 255), 2)
            temp_replace = np.array(replace_img.resize(rect[index][2]))
            frame[rect[index][0][1] : rect[index][1][1], rect[index][0][0] : rect[index][1][0], :,] = temp_replace
        except:
            pass
        return frame

    @staticmethod
    def post_it_color():
        return SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT

    def __update_post_it_color(self):
        rgb_value = SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT
        self.post_it_color_rgb_value = np.array([rgb_value.red(), rgb_value.green(), rgb_value.blue()])

    def __refresh_ui(self):
        self.__update_post_it_color()
        self.__refresh_replace_image(self.replace_image_path)
        self.__refresh_original_picture(self.original_picture_path)
        # self.__refresh_original_video(self.original_video_path)

    def __refresh_replace_image(self, replace_image_path):
        pix_map = QPixmap(replace_image_path)
        self.ui.replace_image_label.setPixmap(pix_map)

    def __refresh_original_picture(self, original_picture_path):
        pix_map = QPixmap(original_picture_path)
        self.ui.original_source_label.setPixmap(pix_map)

    def __refresh_original_video(self, original_video_path):
        pix_map = QPixmap(original_video_path)
        self.ui.original_source_label.setPixmap(pix_map)

    def __refresh_replaced_result(self, replaced_result_path):
        pix_map = QPixmap(replaced_result_path)
        self.ui.replacement_result_label.setPixmap(pix_map)

    def __refresh_post_it_color_line_edit(self):
        self.ui.post_it_lineEdit.setStyleSheet(
            "QLineEdit { background-color: %s}"
            % SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT.name()
        )


# if __name__ == '__main__':
#     # replace image
#     replace_img = './replace_img.jpg'
#     img_name = './img.png'
#     show_replace_result(replace_img=replace_img, mode=0, img_name=img_name)

#     # 视频模式 ： 待替换的视频
#     # video_name = './video.mp4'
#     # show_replace_result(replace_img=replace_img, mode=1, video_name=video_name)

#     # 摄像头模式 ：
#     # show_replace_result(replace_img=replace_img, mode=2)
