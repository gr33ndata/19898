#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of 19898.
# https://github.com/gr33ndata/19898

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2014 Tarek Amr gr33ndata@yahoo.com

from preggy import expect

from 19898 import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal("0.1.0")
