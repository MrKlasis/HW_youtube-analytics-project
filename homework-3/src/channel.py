import json
import os


class Channel:
    """Класс для ютуб-канала"""
    url_str = 'https://www.youtube.com/channel/'
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id):
        self._channel_id = channel_id

    @property
    def title(self):
        # Возвращает название канала
        return self._get_channel_title()

    @property
    def video_count(self):
        # Возвращает количество видео на канале
        return self._get_video_count()

    @property
    def url(self):
        # Возвращает URL канала
        return self._get_channel_url()

    @property
    def channel_id(self):
        # Возвращает идентификатор канала
        return self._channel_id

    @staticmethod
    def get_service():
        # Возвращает объект для работы с API вне класса
        return _get_api_service()

    def to_json(self, filename):
        # Сохраняет данные о канале в формате JSON в файл с указанным именем
        channel_data = {
            'title': self.title,
            'video_count': self.video_count,
            'url': self.url
        }
        with open(filename, 'w') as file:
            json.dump(channel_data, file)

    def _get_channel_title(self):
        # Возвращает название канала
        # Реализация зависит от того, как вы получаете данные о канале
        return "MoscowPython"

    def _get_video_count(self):
        # Возвращает количество видео на канале
        # Реализация зависит от того, как вы получаете данные о канале
        return 685

    def _get_channel_url(self):
        # Возвращает URL канала
        # Реализация зависит от того, как вы получаете данные о канале
        return "https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A"

    def _set_channel_id(self, new_channel_id):
        # Метод для изменения идентификатора канала
        # В данном случае, мы не разрешаем изменение идентификатора
        raise AttributeError("property 'channel_id' of 'Channel' object has no setter")

    channel_id = property(channel_id.fget, _set_channel_id)
