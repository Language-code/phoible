from clld.web.app import get_configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = get_configurator('phoible', settings=settings)
    return config.make_wsgi_app()
