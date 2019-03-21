import os
import re
import importlib
import inspect

from abstract.abstract_plugin import AbstractPlugin


class PluginManager:

    @property
    def load_dynamically(self):
        py_search_re = re.compile('.py$', re.IGNORECASE)
        plugin_files = list(filter(py_search_re.search, os.listdir('plugins')))
        form_module = lambda fp: '.' + os.path.splitext(fp)[0]
        plugins = list(map(form_module, plugin_files))

        modules = []
        for plugin in plugins:
            if not plugin.startswith('__'):
                modules.append(importlib.import_module(plugin, package="plugins"))

        class_instances = []
        for module in modules:
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, AbstractPlugin):
                    class_instances.append(getattr(module, name)())

        return class_instances
