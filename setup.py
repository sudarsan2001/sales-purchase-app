from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in purchase_and_sales_management/__init__.py
from purchase_and_sales_management import __version__ as version

setup(
	name="purchase_and_sales_management",
	version=version,
	description="An app that manages the stock purchases and stock sales",
	author="Sudarshan",
	author_email="frankel9675@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
