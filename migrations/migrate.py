from flask_migrate import Migrate, MigrateCommand
from .. import web

migrate = Migrate(web.app, web.db)
web.manager.add_command('db', MigrateCommand)