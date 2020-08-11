from PyQt5.QtGui import QColor


class SavedValuesConstants:
    ORGANIZATION = "RWU - EI"
    APPLICATION = "Post-it Replacer"

    class LoaderDialog:
        SETTING_NAME = "Load dialog"
        REPLACE_IMAGE_PATH = "replace image path"
        ORIGINAL_PICTURE_PATH = "original picture path"
        ORGINAL_VIDEO_PATH = "original video path"

    class SettingsColorPicker:
        CUSTOMIZED_COLOR_POST_IT = QColor(209, 181, 162)
        CUSTOMIZED_COLOR_POST_IT_UPPER = QColor(189, 161, 144)
        CUSTOMIZED_COLOR_POST_IT_LOWER = QColor(229, 201, 182)
