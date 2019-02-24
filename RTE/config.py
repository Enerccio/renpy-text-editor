import RTE.constants as const
import json
from collections import defaultdict
from RTE.models.theme import Theme


class Config:
    def __init__(self):
        with open(const.config_file_path) as conf:
            data = json.load(conf)
        self._attrs = defaultdict()
        for k, v in data.items():
            self._attrs[k] = v
        self.current_theme = self.get_theme()

    def __getattr__(self, attr):
        return self._attrs[attr]

    def __setattr__(self, attr, value):
        if attr == '_attrs':
            return super(Config, self).__setattr__(attr, value)
        self._attrs[attr] = value

    @property
    def geometry(self):
        return f"{self.wm_width}x{self.wm_height}"

    def get_theme(self):
        return Theme(self.theme_name)

    def set_theme(self, theme_name):
        self.theme_name = theme_name
        self.current_theme = self.get_theme()

    def save(self):
        to_save = dict(self._attrs)
        with open(const.config_file_path, "w") as conf:
            json.dump(to_save, conf, indent=4)

config = Config()