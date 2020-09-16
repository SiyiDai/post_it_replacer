from dialogs.saved_values_paths import SavedValuesConstants
from PyQt5.QtCore import QSettings

SPECIAL_SAVER_SEPARATOR = " - "


class SettingsLoaderAndSaver:
    def __init__(
        self, name, organization=SavedValuesConstants.ORGANIZATION, application=SavedValuesConstants.APPLICATION,
    ):
        self.organization = organization
        self.application = application
        self.name = name

    def read(self, path):
        settings_reader = QSettings(self.organization, self.application)
        return settings_reader.value(self.name + SPECIAL_SAVER_SEPARATOR + path)

    def write(self, path, value):
        settings_writer = QSettings(self.organization, self.application)
        settings_writer.setValue(self.name + SPECIAL_SAVER_SEPARATOR + path, value)
