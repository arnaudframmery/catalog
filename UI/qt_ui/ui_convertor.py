import subprocess


qt_ui_mapping = {
    'main_window.ui': 'main_window_UI.py',
    'catalog_frame.ui': 'catalog_frame_UI.py',
    'article_frame.ui': 'article_frame_UI.py',
    'detail_frame.ui': 'detail_frame_UI.py',
    'catalog_creation_dialog.ui': 'catalog_creation_UI.py',
    'component_setting_dialog.ui': 'component_setting_UI.py',
    'component_frame.ui': 'component_frame_UI.py',
}


if __name__ == "__main__":
    for key, value in qt_ui_mapping.items():
        command = ['pyuic5', key, '-o', value]
        subprocess.run(command, stdout=subprocess.DEVNULL)
