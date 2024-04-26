from Registration_Page import registration
from Registration_Page import render as r_render
import flask
from .settings import shop
from Home_page import render, home
from Authorization_page import render_autho, authorization

registration.add_url_rule(rule= '/Registration/', view_func= r_render, methods = ['GET', 'POST'])

home.add_url_rule(rule = "/", view_func= render)

authorization.add_url_rule(rule = "/Authorization/", view_func = render_autho)

shop.register_blueprint(blueprint = authorization)
shop.register_blueprint(blueprint = home)
shop.register_blueprint(blueprint= registration)
