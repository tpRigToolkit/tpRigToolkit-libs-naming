#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Initialization module for tpRigToolkit-libs-naming
"""

from __future__ import print_function, division, absolute_import

import os
import inspect
import logging.config


def init(do_reload=False, dev=False):
    """
    Initializes module
    :param do_reload: bool, Whether to reload modules or not
    :param dev: bool, Whether is initialized in dev mode or not
    """

    from tpDcc.libs.nameit import register
    from tpDcc.libs.python import importer

    logger = create_logger()

    class tpNameIt(importer.Importer, object):
        def __init__(self, *args, **kwargs):
            super(tpNameIt, self).__init__(module_name='tpRigToolkit.libs.naming', *args, **kwargs)

        def get_module_path(self):
            """
            Returns path where tpNameIt module is stored
            :return: str
            """

            try:
                mod_dir = os.path.dirname(inspect.getframeinfo(inspect.currentframe()).filename)
            except Exception:
                try:
                    mod_dir = os.path.dirname(__file__)
                except Exception:
                    try:
                        import tpRigToolkit.libs.naming
                        mod_dir = tpRigToolkit.libs.naming.__path__[0]
                    except Exception:
                        return None

            return mod_dir

    naming_importer = importer.init_importer(importer_class=tpNameIt, do_reload=False)

    register.register_class('logger', logger)

    naming_importer.import_modules()
    naming_importer.import_packages(only_packages=True)
    if do_reload:
        naming_importer.reload_all()


def create_logger():
    """
    Returns logger of current module
    """

    logging.config.fileConfig(get_logging_config(), disable_existing_loggers=False)
    logger = logging.getLogger('tpRigToolkit-libs-naming')

    return logger


def create_logger_directory():
    """
    Creates artellapipe logger directory
    """

    nameit_importer = os.path.normpath(os.path.join(os.path.expanduser('~'), 'tpRigToolkit-libs-naming', 'logs'))
    if not os.path.isdir(nameit_importer):
        os.makedirs(nameit_importer)


def get_logging_config():
    """
    Returns logging configuration file path
    :return: str
    """

    create_logger_directory()

    return os.path.normpath(os.path.join(os.path.dirname(__file__), '__logging__.ini'))
