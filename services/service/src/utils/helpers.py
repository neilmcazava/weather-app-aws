import logging
import os
from typing import Any
from distutils.util import strtobool


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_env(env_var: str, var_type: Any, default: Any) -> Any:
    try:
        if var_type == bool:
            result = strtobool(os.getenv(env_var, str(default)))
        else:
            result = var_type(os.getenv(env_var, default))
    except Exception as e:
        logger.error(e, exc_info=True)
        result = default

    return result


def get_logger() -> logging.Logger:
    log = logging.getLogger(__name__)
    level = get_env("LOG_LEVEL", str, "INFO")
    log.setLevel(level)

    return log
