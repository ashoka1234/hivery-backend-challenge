from configparser import ConfigParser
from pathlib import Path, PosixPath
from pymongo import MongoClient


class LocalConfig:
    def __init__(self, cfg: dict = None, cfg_file_path=None):
        if cfg:
            self.cfg = cfg
        else:
            cfg_ = ConfigParser()
            if cfg_file_path:
                cfg_.read(cfg_file_path)
            elif (Path().absolute() / 'challenge.conf').exists():
                cfg_.read(Path().absolute() / 'challenge.conf')
            elif (PosixPath('~').expanduser() / 'challenge.conf').exists():
                cfg_.read(PosixPath('~') / 'challenge.conf')
            elif Path(__file__).parent.parent.parent.with_suffix('challenge.conf').exists():
                cfg_.read(Path(__file__).parent.parent.parent.with_name('challenge.conf'))
            else:
                cfg_.read_dict({'default': {'host': '127.0.0.1',
                                            'port': 27017,
                                            'database': 'ashoka_challenge'}})
            self.cfg = cfg_['default']

    def set_database_name(self, database_name):
        self.cfg['database'] = database_name


def connect(cfg: dict = None, cfg_file_path=None):
    if not cfg:
        cfg = LocalConfig(cfg_file_path=cfg_file_path).cfg
    return MongoClient(host=cfg.get('host', '127.0.0.1'),
                       port=cfg.getint('port', 27017),
                       username=cfg.get('user'),
                       password=cfg.get('password'))[cfg.get('database') or 'ashoka_challenge']
