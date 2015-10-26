# Copyright (c) 2014 Per Unneberg
import logging
import logging.config
import yaml
import os
import sys

# NB: _logger level cannot be modified by user
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.DEBUG)

# See http://stackoverflow.com/questions/15727420/using-python-logging-in-multiple-modules
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances.keys():
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class LoggerManager(object):
    __metaclass__ = Singleton

    _loggers = {}
    _fmt = "%(asctime)s (%(levelname)s) %(name)s :  %(message)s"
    _ch = logging.StreamHandler()
    _formatter = logging.Formatter(_fmt)
    _ch.setFormatter(_formatter)
    _has_loaded_config = False

    def __init__(self, *args, **kwargs):
        if not LoggerManager._has_loaded_config:
            # Add snakemakelib root handler
            LoggerManager._loggers['snakemakelib'] = logging.getLogger('snakemakelib')
            LoggerManager._loggers['snakemakelib'].setLevel(logging.WARNING)
            LoggerManager._loggers['snakemakelib'].addHandler(LoggerManager._ch)
            self._set_config()
            LoggerManager._has_loaded_config = True

    def _set_config(self):
        cfg = self._load_config()
        if cfg:
            logging.config.dictConfig(cfg)

    def _load_config(self):
        try:
            import snakemake.workflow as wf
            if "logging" in wf.config:
                return wf.config['logging']
        except Exception as e:
            _logger.warn("snakemakelib logging setup failed!")
            _logger.warn(e)
        return None

    @staticmethod
    def getLogger(name=None):
        if not name:
            smllogger = logging.getLogger()
            return logging.getLogger()
        elif name not in LoggerManager._loggers.keys():
            LoggerManager._loggers[name] = logging.getLogger(str(name))
            LoggerManager._loggers[name].addHandler(LoggerManager._ch)
            return LoggerManager._loggers[name]
        else:
            logging.warn("Trying to get already existing logger")
