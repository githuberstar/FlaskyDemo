# #!/bin/env python
# # -*- coding:utf-8 -*-
# import os, sys, unittest
# from app.models import User, Permission, AnonymousUser, Role
# from app import create_app, db
# import app.auth.views
#
#
# #修改系统路径名称, chdir改变当前工作目录到指定路径，getcwd返回当前进程的工作目录
# file_folder = os.path.dirname(os.path.abspath(__file__))
# os.chdir(os.path.dirname(file_folder))
# sys.path.append(os.getcwd())
# # sys.path.append(os.path.join(os.path.dirname(os.path.dirname(file_folder)),"app"))
#
#
# class UserModuleTest(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         # db.create_all()
#         # Role.insert_roles()
#
#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()
#         create_app('default').run()
#
#     # def test_password_setter(self):
#     #     u = User(password = 'cat')
#     #     self.assertTrue(u.password_hash is not None)
#     #
#     # def test_no_password_getter(self):
#     #     u = User(password = 'cat')
#     #     with self.assertRaises(ArithmeticError):
#     #         u.password
#     #
#     # def test_password_verification(self):
#     #     u = User(password = 'cat')
#     #     self.assertTrue(u.verify_password('cat'))
#     #     self.assertFalse(u.verify_password('dog'))
#     #
#     # def test_password_salts_are_random(self):
#     #     u = User(password = 'cat')
#     #     u2 = User(password = 'cat')
#     #     self.assertNotEqual(u.password_hash, u2.password_hash)
#
#     def test_roles_and_permissions(self):
#         # Role.insert_roles()
#         u = User(email='flasky@example.com', password='123456')
#         self.assertTrue(u.can(Permission.WRITE_ARTICLES))
#         self.assertTrue(u.can(Permission.MODERATE_COMMENTS))
#
#     def test_anonymous_user(self):
#         u = AnonymousUser()
#         self.assertFalse(u.can(Permission.FOLLOW))
#
# #
# # if __name__ == '__main__':
# #     unittest.main()
#
# if __name__ == '__main__':
#     unittest.main()
