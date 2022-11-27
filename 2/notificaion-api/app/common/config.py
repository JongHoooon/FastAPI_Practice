from dataclasses import dataclass, asdict
from os import path, environ

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    '''
    기본 Configuration
    '''
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    # environ(환경 변수) 에서 첫번째 찾고 없으면 두번째 사용한다.(switch case 처럼 사용한다.)
    return config.get(environ.get("API_ENV", "local"))


# 딕셔너리 형태로 사용하기위해서 dataclass 사용한다.