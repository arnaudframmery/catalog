import os

from value_type.value_type_float import ValueTypeFloat
from value_type.value_type_image import ValueTypeImage
from value_type.value_type_int import ValueTypeInt
from value_type.value_type_text import ValueTypeText


def test_value_type_get_all(controller):
    # Test the recovery of all the possible value types
    assert controller.get_all_value_types() == [
        {'code': 'text', 'id': 1},
        {'code': 'int', 'id': 2},
        {'code': 'float', 'id': 3},
        {'code': 'image', 'id': 4},
    ], 'failed'


# Text
def test_value_type_text_check_consistency():
    assert ValueTypeText.check_consistency('this is a text')
    assert ValueTypeText.check_consistency('-98')
    assert not ValueTypeText.check_consistency({'abc': 50})


def test_value_type_text_recovery_process():
    assert ValueTypeText.recovery_process('this is a text') == 'this is a text'
    assert ValueTypeText.recovery_process('-98') == '-98'
    assert ValueTypeText.recovery_process({'abc': 50}) is None


# Int
def test_value_type_int_check_consistency():
    assert ValueTypeInt.check_consistency(53)
    assert ValueTypeInt.check_consistency(-7)
    assert ValueTypeInt.check_consistency('-098')
    assert ValueTypeInt.check_consistency(64.7)
    assert not ValueTypeInt.check_consistency('123abc')
    assert not ValueTypeInt.check_consistency('50.0')


def test_value_type_int_recovery_process():
    assert ValueTypeInt.recovery_process(53) == '53'
    assert ValueTypeInt.recovery_process(-7) == '-7'
    assert ValueTypeInt.recovery_process('-098') == '-98'
    assert ValueTypeInt.recovery_process(64.7) == '64'
    assert ValueTypeInt.recovery_process('123abc') is None
    assert ValueTypeInt.recovery_process('50.0') is None


# Float
def test_value_type_float_check_consistency():
    assert ValueTypeFloat.check_consistency(53)
    assert ValueTypeFloat.check_consistency(-7.2)
    assert ValueTypeFloat.check_consistency('-98')
    assert ValueTypeFloat.check_consistency('64.7')
    assert not ValueTypeFloat.check_consistency('100,01')
    assert not ValueTypeFloat.check_consistency('hell0')


def test_value_type_float_recovery_process():
    assert ValueTypeFloat.recovery_process(53) == '53.0'
    assert ValueTypeFloat.recovery_process(-7.2) == '-7.2'
    assert ValueTypeFloat.recovery_process('-98') == '-98.0'
    assert ValueTypeFloat.recovery_process('64.7') == '64.7'
    assert ValueTypeFloat.recovery_process('100,01') is None
    assert ValueTypeFloat.recovery_process('hell0') is None


# Image
def test_value_type_image_check_consistency():
    resource_path = os.path.join(os.getcwd(), 'resource')

    assert ValueTypeImage.check_consistency(os.path.join(resource_path, 'hagrid.jpg'))
    assert not ValueTypeImage.check_consistency(None)
    assert not ValueTypeImage.check_consistency(resource_path)
    assert not ValueTypeImage.check_consistency('this/is/a/fake/path.jpg')


def test_value_type_image_recovery_process():
    resource_path = os.path.join(os.getcwd(), 'resource')
    test_path = os.path.join(os.getcwd(), 'test')

    image_path = os.path.join(resource_path, 'hagrid.jpg')
    assert ValueTypeImage.recovery_process(image_path) == image_path
    image_origin_path = os.path.join(test_path, 'test_hagrid.jpg')
    assert resource_path in ValueTypeImage.recovery_process(image_origin_path)
    assert ValueTypeImage.recovery_process('this/is/a/fake/path.jpg') is None
