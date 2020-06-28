import os


class FileUtil:
    RESOURCES_PATH = 'resources\\word.json'

    @classmethod
    def get_json_from_file(cls, file_path):
        pass

    @classmethod
    def get_file_path(cls):
        # This Side project used hard coded path
        project_path = \
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.abspath(__file__))))
        file_path = os.path.join(project_path, cls.RESOURCES_PATH)
        return file_path
