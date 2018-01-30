# Load all modules in folder: https://stackoverflow.com/a/1057534

from os.path import dirname, basename, isfile
import glob
import importlib
modules = glob.glob(dirname(__file__)+"/*/*.py")

__all__ = [
    basename(dirname(f)) for f in modules
    if isfile(f) and f.endswith('__init__.py')
]

for m in __all__:
    importlib.import_module('.{}'.format(m), __name__)
