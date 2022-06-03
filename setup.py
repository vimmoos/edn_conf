#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="Edn Configs",
    version="0.0.1",
    description="Edn enhanced config parser",
    long_description="",
    author="Massimiliano Falzari",
    author_email="m.falzari@student.rug.nl",
    url="https://github.com/vimmoos/edn_conf",
    download_url="https://github.com/vimmoos/edn_conf",
    license="LGPLv3",
    install_requires=["edn_format"],
    include_package_data=True,
    packages=find_packages(),
)
