import logging
import logging.config
from pathlib import Path

from utils import read_json


def setup_logging(
    save_dir, log_config="logger/logger_config.json", default_level=logging.INFO
):
    """
    Setup logging configuration
    """
    log_config = Path(log_config)
    if log_config.is_file():
        config = read_json(log_config)
        # modify logging paths based on run config
        for _, handler in config["handlers"].items():
            if "filename" in handler:
                handler["filename"] = str(save_dir / handler["filename"])

        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level, format="%(levelname)s-%(message)s")
        logging.warning(
            "Logging configuration file is not found in {}.".format(log_config)
        )
