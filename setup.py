from setuptools import setup

setup(
    name="codexium",
    version="0.1",
    py_modules=["codexium"],
    install_requires=[
        "click",
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'codexium=codexium:codexium',
        ],
    },
)
