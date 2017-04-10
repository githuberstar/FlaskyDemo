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

    # def test_password_setter(self):
      # u = User(password = 'cat')
      # self.assertTrue(u.password_hash is not None)
      #
      # def test_no_password_getter(self):
      # u = User(password = 'cat')
      # with self.assertRaises(ArithmeticError):
      # u.password
      #
      # def test_password_verification(self):
      # u = User(password = 'cat')
      # self.assertTrue(u.verify_password('cat'))
      # self.assertFalse(u.verify_password('dog'))
      #
      # def test_password_salts_are_random(self):
      # u = User(password = 'cat')
      # u2 = User(password = 'cat')
      # self.assertNotEqual(u.password_hash, u2.password_hash)

    # if __name__ == '__main__':
    #     -  # app = Flask(__name__)
    #     -  # ####SMTP server config
    #     -  # app.config['MAIL_SERVER'] = 'smtp.163.com'  # 电子邮件服务器的地址
    #     -  # app.config['MAIL_PORT'] = 25  # 邮箱服务器的端口
    #     -  # app.config['MAIL_USE_TLS'] = True  # 启用安全传输
    #     -  # app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')  # 邮件账户用户名,已定义环境变量
    #     -  # app.config['MAIL_PASSWORD'] = os.environ.get(('MAIL_PASSWORD'))  # 邮件账密码,已定义环境变量
    #     -  # app.config['FLASKY_ADMIN'] = 'aa'
    #     -  # app.run()
    #     -    unittest.main()



    def test_roles_and_permissions(self):
        # Role.insert_roles()
        u = User(email='flasky@example.com', password='123456')
        self.assertTrue(u.can(Permission.WRITE_ARTICLES))
        self.assertFalse(u.can(Permission.MODERATE_COMMENTS))

    def test_anonymous_user(self):
        u = AnonymousUser()
        self.assertFalse(u.can(Permission.FOLLOW))
