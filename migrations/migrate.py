from flask_migrate import Migrate, MigrateCommand
from .. import DemoManage

migrate = Migrate(DemoManage.app, DemoManage.db)
DemoManage.manager.add_command('db', MigrateCommand)