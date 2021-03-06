import os
import json


class FileUtil:
    RESOURCES_PATH = 'resources\\word.json'
    OS_PROPERTY_KEY_PATH = 'resources\\os_property_key.json'

    @classmethod
    def get_json_from_file(cls, file_path=None):
        if not file_path:
            file_path = cls.get_file_path()

        with open(file_path, 'rt', encoding='UTF8') as json_file:
            json_data = json.load(json_file)

        return json_data

    @classmethod
    def get_file_path(cls):
        # This Side project used hard coded path
        file_path = os.path.join(cls.get_root_dir_path(), cls.RESOURCES_PATH)
        return file_path

    @classmethod
    def get_root_dir_path(cls):
        project_path = \
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__))))
        
        return project_path

    @classmethod
    def get_os_property_key_json(cls):
        file_path = os.path.join(cls.get_root_dir_path(), cls.OS_PROPERTY_KEY_PATH)
        with open(file_path) as json_file:
            os_property_key_json = json.load(json_file)

        return os_property_key_json
