from setuptools import setup

setup(
    name='easy-parallel',
    py_modules=['parallel'],
    url='https://github.com/raphtown/easy-parallel',
    version='0.1.1',
    description='Parallel wrapper for easy multi-threading.',
    long_description='Parallel wrapper for easy multi-threading.',
    author='Raphael Townshend',
    license='MIT',
    install_requires=['pathos'],
)
