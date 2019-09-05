#coding:utf-8

import os


def _import_function_submodules():
    function_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    for root, dirs, files in os.walk(os.path.abspath(os.path.join(os.path.dirname(__file__))), topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == ".py":
                filename = os.path.join(root, name)
                module_name = filename[len(function_path):]
                module_name = module_name.replace(os.sep, '.')[:-3]
                if module_name.split(".")[-1] != "__init__":
                    __import__("function{}".format(module_name), fromlist=True)

_import_function_submodules()