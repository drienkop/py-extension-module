from setuptools import setup, Extension, find_packages
from subprocess import check_output, CalledProcessError
from platform import system
from setuptools.dist import Distribution, DistutilsPlatformError, DistutilsOptionError, DistutilsSetupError

REQUIREMENTS = ['setuptools', 'altgraph',]

STATIC_LIBS = ['libcrypto',]

DYNAMIC_LIBS = ['']
DYNAMIC_LIBS_DIR = ['']


def get_setup_option(category_name, option):
    """Get value of option within [category_name] in setup.cfg"""
    dist = Distribution()
    dist.parse_config_files()
    return dist.get_option_dict(category_name).get(option, None)
    

def find_library_path(library_name):
    try:
        found_path = check_output(['pkg-config', '--variable=libdir', library_name]).decode().strip()
    except CalledProcessError:
        raise DistutilsSetupError('Could not find {}. Please specify the full path in setup.cfg.'.format(library_name))
    return found_path


extra_objects = []
# If static libraries are not defined in setup.cfg, try to find them automatically
if not get_setup_option('build_ext', 'link_objects'):
    extra_objects = [find_library_path(lib) + '/' + lib + '.a' for lib in STATIC_LIBS]

module1 = Extension(name = '_hashmodule',
                    sources = ['hashmodule.c', 'hashmodule.i'],
                    libraries=DYNAMIC_LIBS,
                    library_dirs=DYNAMIC_LIBS_DIR,
                    extra_objects=extra_objects
                    )

setup (name = 'hashmodule',
       version = '1.0',
       description = 'This is is an extension module which does XYZ.',
       ext_modules = [module1],
       py_modules = ["hashmodule"],
       packages=find_packages(),
       python_requires='>=3.6',
       install_requires=REQUIREMENTS,
       license='MIT',
       )
