from setuptools import setup

setup(
    name='Internet Connection Recorder',
    version='1.0',
    py_modules=['yourscript'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        record=main:set_params
    ''',
)