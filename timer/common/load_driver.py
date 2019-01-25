import stevedore


def load_driver(namespace, driver_name, *args):
    try:
        driver_manager = stevedore.DriverManager(namespace,
                                                 driver_name,
                                                 invoke_on_load=True,
                                                 invoke_args=args)
        return driver_manager.driver
    except stevedore.exception.NoMatches:
        msg = 'Unable to find %(name)r driver in %(namespace)r.'
        raise ImportError(msg % {'name': driver_name, 'namespace': namespace})
