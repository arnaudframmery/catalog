import shutil
import os
import uuid

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout

from UI.widget.button import Button
from constant import VALUE_TYPE_CODE
from value_type.value_type import ValueType


class ValueTypeImage(ValueType):
    """
    an image
    """

    @staticmethod
    def get_code():
        return VALUE_TYPE_CODE.IMAGE

    @staticmethod
    def check_consistency(value):
        if value is not None and os.path.isfile(value):
            return True
        else:
            return False

    @staticmethod
    def recovery_process(value):
        if ValueTypeImage.check_consistency(value):
            resource_dir = os.path.join(os.getcwd(), 'resource')
            assumed_path = os.path.join(resource_dir, os.path.basename(value))

            # if the image is already in resource folder
            if os.path.isfile(assumed_path):
                return assumed_path
            # else, the image is moved into the resource folder and rename
            else:
                image_extension = value.split('.')[-1]
                path = shutil.copy(value, resource_dir)
                new_path = os.path.join(resource_dir, f'{str(uuid.uuid4())}.{image_extension}')
                os.rename(path, new_path)
                return new_path
        else:
            return None

    @staticmethod
    def create_edit_widget(value, style=None):
        widget = ImageEditWidget(style)
        if ValueTypeImage.check_consistency(value):
            widget.set_image_path(value)
        return widget

    @staticmethod
    def create_view_widget(value):
        widget = ImageViewWidget()
        if ValueTypeImage.check_consistency(value):
            widget.set_image_path(value)
        return widget

    @staticmethod
    def is_filled(widget):
        return os.path.isfile(widget.get_image_path())

    @staticmethod
    def get_edit_widget_data(widget):
        image_path = widget.get_image_path()
        return image_path

    @staticmethod
    def is_sortable():
        return False

    @staticmethod
    def is_filterable():
        return False

    @staticmethod
    def is_recovery_accepted(code):
        if code in [VALUE_TYPE_CODE.INT, VALUE_TYPE_CODE.FLOAT]:
            return False
        else:
            return True


class ImageEditWidget(QtWidgets.QWidget):
    """
    manage the selection and the display of an image
    """

    def __init__(self, style, *args, **kwargs):
        super(ImageEditWidget, self).__init__(*args, **kwargs)

        self.image_path = ''
        self.image = None
        self.style = style

        self.select_button = Button(self)
        self.select_button.setText('Select an image')
        self.select_button.released.connect(self.choose_default_image)

        self.image_label = QLabel(self)
        self.image_label.setText('')

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.select_button)
        self.layout.addWidget(self.image_label)
        self.layout.setContentsMargins(0, 0, 0, 0)

    def choose_default_image(self):
        """manage the dialog window for selecting an image"""
        dialog = QFileDialog()
        dialog.setFileMode(1)
        image_path, image_type = QFileDialog.getOpenFileName(
            dialog,
            "Default image selection",
            filter="Images (*.png *.jpg)"
        )
        if image_path != '':
            self.image_path = image_path
            self.display_image()
            self.resizeEvent(None)

    def display_image(self):
        """manage the display of the selected image"""
        self.image = QPixmap(self.image_path)
        self.image = self.image.scaled(240, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.image_label.setPixmap(self.image)

    def set_image_path(self, path):
        """set the image path"""
        self.image_path = path
        self.display_image()

    def get_image_path(self):
        """get the image path"""
        return self.image_path

    def setAlignment(self, alignment):
        """set the alignment of the image and the button"""
        self.image_label.setAlignment(alignment)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """Adjust the size of the image"""
        if self.style is not None and self.image is not None:
            self.image_label.setPixmap(self.image.scaled(self.image_label.rect().width(),
                                                         self.image_label.rect().height(),
                                                         Qt.KeepAspectRatio,
                                                         Qt.FastTransformation))


class ImageViewWidget(QtWidgets.QLabel):
    """
    manage the display of an image
    """

    def __init__(self, *args, **kwargs):
        super(ImageViewWidget, self).__init__(*args, **kwargs)
        self.image = None
        self.setText('')

    def set_image_path(self, path):
        """set the image path"""
        self.image = QPixmap(path)
        self.setPixmap(self.image)

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        """Adjust the size of the image"""
        self.setPixmap(self.image.scaled(a0.size(), Qt.KeepAspectRatio, Qt.FastTransformation))
