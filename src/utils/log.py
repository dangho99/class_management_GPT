from src.utils.load_config import get_log_config
import logging
import logging.config

conf = get_log_config()
logging.config.dictConfig(get_log_config())


def get_logger(class_name='root') -> logging.Logger:
    """

    :param class_name:
    :return:
    """
    return logging.getLogger(class_name)
    pass
