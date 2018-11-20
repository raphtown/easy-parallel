from setuptools import setup

setup(
    name='parallel',
    py_modules=['parallel'],
    version='0.1.0',
    description='Parallel wrapper for easy multi-threading.',
    author='Raphael Townshend',
    license='MIT',
    install_requires=['pathos'],
)
