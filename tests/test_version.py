# -*- coding: utf-8 -*-
# @Time    : 2021/3/17 12:59
# @Author  : sunxuan
# @Site    : 
# @File    : test_version.py
import os
import  sys
def test_vesion():
	from interface_test import  __version__
	assert isinstance(__version__,str)