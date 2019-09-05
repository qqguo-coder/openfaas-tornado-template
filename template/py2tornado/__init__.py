import glob
import importlib
import os


def import_modules(pathname):

    modules_dict = {}
    module_paths = glob.glob(pathname)
    for path in module_paths:
        module_name = path.replace(os.sep, '.')[:-3]
        print(module_name)
        module = importlib.import_module(module_name)
        for element in dir(module):
            if not element.startswith('__'):
                modules_dict[element] = eval('module.{}'.format(element))

    return modules_dict


module_info = import_modules('../function/**.py')
print(module_info)