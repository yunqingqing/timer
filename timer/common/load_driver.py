import importlib


def load_driver(driver_name):
    module_name, obj_name = driver_name.rsplit('.', 1)
    return getattr(importlib.import_module(module_name), obj_name)()
