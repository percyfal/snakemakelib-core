# Copyright (C) 2015 by Per Unneberg

class SnakemakelibException(Exception):
    """Base exception class

    Args:
      msg (str): String described by exception
      code (int, optional): Error code, defaults to 2.

    """
    def __init__(self, msg, code=2):
        self.msg = msg
        self.code = code

class NotInstalledError(SnakemakelibException):
    """Error thrown if program/command/application cannot be found in path"""

class SamplesException(SnakemakelibException):
    """Error thrown if samples missing or wrong number."""

class OutputFilesException(SnakemakelibException):
    """Error thrown if outputfiles missing or wrong number."""

class DeprecatedException(SnakemakelibException):
    """Error thrown for deprecated functions."""
