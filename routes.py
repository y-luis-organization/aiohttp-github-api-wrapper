from organizations.views import organizations


def setup_routes(app):
    app.router.add_get('/', organizations)
    app.router.add_get('/{organization}', organizations)