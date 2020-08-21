from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap, QColor, QImage
from PyQt5.QtWidgets import QMainWindow, QColorDialog
import os
import cv2
import numpy as np
from PIL import Image

from ui_py.ui_mainwindow import Ui_MainWindow
from dialogs.open_load_dialog import OpenLoadDialog
from dialogs.saved_values_paths import SavedValuesConstants

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
        print(self.__dict__)

    def on_action_loader_triggered(self):
        dialog = OpenLoadDialog()
        if not dialog.exec_():
            return

        self.replace_image_path = dialog.replace_image_file_path()
        self.original_picture_path = dialog.original_picture_file_path()
        self.original_video_path = dialog.original_video_file_path()

        self.__refresh_ui()

    def on_action_settings_color_picker_triggered(self):
        title = "Choose the color of post-it"
        color = SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT
        color_pick = QColorDialog.getColor(color, self, title, QColorDialog.ShowAlphaChannel)

        self.__store_post_it_color(color_pick)
        self.__update_post_it_color()
        self.__refresh_post_it_color_line_edit()

    def show_replace_result(self):
        dir_path = os.path.dirname(os.path.realpath(self.replace_image_path))
        result_path = dir_path + "/" + REPLACED_FILE_NAME

        self.select_mode()
        self.__refresh_replaced_result(result_path)

    def select_mode(self):
        assert self.replace_image_path is not None
        replace_img = self.__convert_rgb_to_bgr(self.replace_image_path)
        replace_img = Image.fromarray(replace_img)

        # check which radiobutton has been selected
        if self.ui.radioButton_picture.isChecked():
            assert self.original_picture_path is not None
            self.show_result_picture(self.original_picture_path, replace_img)

        if self.ui.radioButton_video.isChecked():
            assert self.original_video_path is not None
            self.cap = cv2.VideoCapture(self.original_video_path)
            self.replace_img = replace_img
            self.timer_video = QTimer(self)
            self.timer_video.timeout.connect(self.show_result_video)
            self.timer_video.start(50)

        if self.ui.radioButton_camera.isChecked():
            # self.show_result_camera_stream(replace_img)
            self.cap = cv2.VideoCapture(0)
            self.replace_img = replace_img
            self.timer_camera = QTimer(self)
            self.timer_camera.timeout.connect(self.show_result_camera_stream)
            self.timer_camera.start(5)

    def show_result_picture(self, pic_path, replace_img):
        # Picture, change the post-it part in pic
        frame = self.__convert_rgb_to_bgr(pic_path)

        replace_result = self.detect_and_replace(frame.copy(), replace_img)
        cv2.imwrite(REPLACED_FILE_NAME, replace_result)

    def show_result_video(self):
        replace_img = self.replace_img
        # video_path = self.original_video_path
        # Video, change the post-it part in video
        # while True:
        ret, frame = self.cap.read()
        if frame is not None:
            replace_result = self.detect_and_replace(frame.copy(), replace_img)

            replace_result = cv2.cvtColor(replace_result, cv2.COLOR_BGR2RGB)  # 将OpenCV图像流转为pyqt可以显示的图像流
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            show_image = QImage(
                replace_result.data, replace_result.shape[1], replace_result.shape[0], QImage.Format_RGB888
            )
            source_image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.ui.replacement_result_label.setPixmap(QPixmap.fromImage(show_image))
            self.ui.original_source_label.setPixmap(QPixmap.fromImage(source_image))
            # cv2.imshow("original", frame)
            # cv2.imshow("mask", replace_result)

            # press 'ESC' to quit
            if cv2.waitKey(100) & 0xFF == 0x1B:
                return
        else:
            self.timer_video.stop()
            return

        # cap.release()

    def show_result_camera_stream(self):
        # Camera, change the post-it part in the camera stream
        # cap = cv2.VideoCapture(0)
        # while True:
        #     ret, frame = cap.read()
        #     replace_result = self.detect_and_replace(frame.copy(), replace_img)

        #     cv2.imshow("original", frame)
        #     cv2.imshow("mask", replace_result)

        #     # press 'ESC' to quit
        #     if cv2.waitKey(100) & 0xFF == 0x1B:
        #         break
        # cap.release()

        replace_img = self.replace_img
        ret, frame = self.cap.read()
        if frame is not None:
            replace_result = self.detect_and_replace(frame.copy(), replace_img)

            replace_result = cv2.cvtColor(replace_result, cv2.COLOR_BGR2RGB)  # 将OpenCV图像流转为pyqt可以显示的图像流
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            show_image = QImage(
                replace_result.data, replace_result.shape[1], replace_result.shape[0], QImage.Format_RGB888
            )
            source_image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
            self.ui.replacement_result_label.setPixmap(QPixmap.fromImage(show_image))
            self.ui.original_source_label.setPixmap(QPixmap.fromImage(source_image))
            if cv2.waitKey(100) & 0xFF == 0x1B:
                return
        else:
            self.timer_camera.stop()
            return

    def detect_and_replace(self, frame, replace_img):
        contours, hierarchy = self.find_contours(frame)
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

    def set_mask(self, frame):
        lower = self.post_it_color_rgb_value - COLOR_RANGE
        upper = self.post_it_color_rgb_value + COLOR_RANGE
        return cv2.inRange(frame, lowerb=lower, upperb=upper)

    def find_contours(self, frame):
        mask = self.set_mask(frame)
        return cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    @staticmethod
    def __convert_rgb_to_bgr(rgb_img_path):
        # open image with Image.open to avoid error from opencv
        # convert rgb image to bgr for opencv
        bgr_img = np.array(Image.open(rgb_img_path).convert("RGB"))
        bgr_img = cv2.cvtColor(bgr_img, cv2.COLOR_RGB2BGR)
        return bgr_img

    @staticmethod
    def __store_post_it_color(color_pick):
        SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT = color_pick

    def __update_post_it_color(self):
        rgb_value = SavedValuesConstants.SettingsColorPicker.CUSTOMIZED_COLOR_POST_IT
        self.post_it_color_rgb_value = np.array([rgb_value.blue(), rgb_value.green(), rgb_value.red()])

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
