#!/bin/env python
# -*- coding:utf-8 -*-
import os

import sys

# 加这一段就好了
from app import create_app

#修改系统路径名称
file_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.dirname(file_folder))
sys.path.append(os.getcwd())
# sys.path.append(os.path.join(os.path.dirname(os.path.dirname(file_folder)),"app"))

import app.auth.views
import unittest
from app.models import User, Permission, AnonymousUser

if __name__ == '__main__':
    unittest.main()


class UserModuleTest(unittest.TestCase):
    def setUp(self):
        create_app('default').run()

    def test_roles_and_permissions(self):
        u = User(email='flasky@example.com', password='123456')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
