# Copyright (C) 2015 by Per Unneberg
# pylint: disable=R0904
import pytest
import logging

@pytest.fixture()
def lm(request):
    from snakemakelib.log import LoggerManager
    LoggerManager._loggers = {}
    LoggerManager._has_loaded_config = False
    return LoggerManager

# Mock LoggerManager._load_config
def test_log(lm, monkeypatch):
    def mockreturn(cls):
        return {'version':1, 'disable_existing_loggers': True, 'loggers' : {__name__: {'level': 'INFO'}}}
    monkeypatch.setattr(lm, '_load_config', mockreturn)
    logger =  lm().getLogger(__name__)
    assert logging.getLevelName(logger.level) == "INFO"
    
def test_log_debug(lm, monkeypatch):
    def my_mockreturn(cls):
        return {'version':1, 'disable_existing_loggers': True, 'loggers' : {__name__: {'level': 'DEBUG'}}}
    monkeypatch.setattr(lm, '_load_config', my_mockreturn)
    logger = lm().getLogger(__name__)
    assert logging.getLevelName(logger.level) == "DEBUG"

def test_failed_log(lm, monkeypatch):
    def mockreturn(cls):
        return {'version':1, 'disable_existing_loggers':True, 'loggers' : {__name__: {'level': 'FOO'}}}
    monkeypatch.setattr(lm, '_load_config', mockreturn)
    with pytest.raises(ValueError):
        logger = lm().getLogger(__name__)
