from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in chris/__init__.py
from chris import __version__ as version

setup(
	name="chris",
	version=version,
	description="Ecom App",
	author="khan",
	author_email="khanmomodou101@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
