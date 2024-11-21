from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='Biblioteca',
    version='0.0.1',
    license='MIT License',
    author='MarvinTL24',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='escorpiano18@bol.com.br',
    keywords='Marvin',
    description=u'Estudos',
    packages=['Testando'],
    install_requires=['requests'],)