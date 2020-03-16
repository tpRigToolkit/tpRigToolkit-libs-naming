#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Library to manage nomenclature of project files, folders and DCC nodes
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import tpDcc
from tpDcc.libs.python import decorators
from tpDcc.libs.nameit.core import namelib


@decorators.Singleton
class RigToolkitNameLib(namelib.NameLib, object):
    def __init__(self):
        namelib.NameLib.__init__(self)
        self.naming_file = tpDcc.ConfigsMgr().get_config('tpRigToolkit-naming').get_path()

        self.init_naming_data()
