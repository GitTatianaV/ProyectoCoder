from setuptools import setup, find_packages

setup(
    name='mipaquete',
    version='1.0',
    description='modelamiento de Clientes en una página de compras',
    author='Tatiana Velehorski',
    author_email='tati.velehorski@gmail.com',
    packages=['mipaquete'],  # Especifica el paquete principal
    py_modules=['mipaquete.modulo1', 'mipaquete.modulo2'],  # Especifica los módulos
)