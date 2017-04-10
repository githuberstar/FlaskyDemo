run /tests/test_user_model.py 错误栈：

`E:\workplace\python\FlaskyDemo\tests\test_user_model.py:3: RuntimeWarning: Parent module 'tests' not found while handling absolute import
  import os
E:\workplace\python\FlaskyDemo\tests\test_user_model.py:5: RuntimeWarning: Parent module 'tests' not found while handling absolute import
  import sys
E:\workplace\python\FlaskyDemo\tests\test_user_model.py:13: RuntimeWarning: Parent module 'tests' not found while handling absolute import
  import unittest
E:\workplace\python\FlaskyDemo\tests\test_user_model.py:14: RuntimeWarning: Parent module 'tests' not found while handling absolute import
  from models import User, Permission, AnonymousUser
Traceback (most recent call last):
  File "D:\softwares\pycharm\helpers\pydev\pydevd.py", line 1556, in <module>
    globals = debugger.run(setup['file'], None, None, is_module)
  File "D:\softwares\pycharm\helpers\pydev\pydevd.py", line 940, in run
    pydev_imports.execfile(file, globals, locals)  # execute the script
  File "D:\softwares\pycharm\helpers\pycharm\utrunner.py", line 153, in <module>
    modules = [loadSource(a[0])]
  File "D:\softwares\pycharm\helpers\pycharm\utrunner.py", line 65, in loadSource
    module = imp.load_source(moduleName, fileName)
  File "E:\workplace\python\FlaskyDemo\tests\test_user_model.py", line 14, in <module>
    from models import User, Permission, AnonymousUser
  File "E:\workplace\python\FlaskyDemo\app\models.py", line 2, in <module>
    from . import login_manager, db
ValueError: Attempted relative import in non-package`

也就是回到了之前说的问题，app/models.py里的from . 和from __init__ 的问题，这里怎么改