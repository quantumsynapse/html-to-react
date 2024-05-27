from setuptools import setup, find_packages

setup(
    name="html-to-react",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Lista de dependências
    ],
    entry_points={
        'console_scripts': [
            'html-to-react=src.converter:main',
        ],
    },
)

