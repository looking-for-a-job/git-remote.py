import setuptools

setuptools.setup(
    name='git-remote',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
