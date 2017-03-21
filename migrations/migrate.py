from flask_migrate import Migrate, MigrateCommand
from .. import manage

migrate = Migrate(manage.app, manage.db)
manage.manager.add_command('db', MigrateCommand)