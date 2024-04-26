import flask
import flask_migrate
import flask_sqlalchemy
import os 

shop = flask.Flask(
    import_name= 'settings',
    template_folder= 'Shop/templates',
    instance_path= os.path.abspath(__file__ + '/..') 
)

shop.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = flask_sqlalchemy.SQLAlchemy(app = shop)
migrate = flask_migrate.Migrate(app = shop, db = db)