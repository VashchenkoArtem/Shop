import flask

authorization = flask.Blueprint(
    name = "authorization",
    import_name = "app",
    template_folder = "Authorization_page/templates",
    static_folder = "Authorization_page/static",
    static_url_path = "/authorization/"
)