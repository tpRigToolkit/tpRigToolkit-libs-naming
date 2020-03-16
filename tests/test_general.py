#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains general tests for tpRigToolkit-libs-naming
"""

import pytest

from tpRigToolkit.libs.naming import __version__


def test_version():
    assert __version__.__version__
