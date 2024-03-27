from setuptools import setup, find_packages

setup(
    name='lrpc_python',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        'grpcio-tools'
    ],
    author='u1ug',
    author_email='maxim2006722@gmail.com',
    description='Landmark-Search gRPC client for Python',
    keywords=['landmark-search'],
    url='https://github.com/oppositemc/lprc-python'
)