import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-yarmp",
    version="0.5.0",
    author="Thomas Jurk",
    author_email="yarmp@breaknoise.com",
    description="This package provides the python backend for the yarmp-project",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/tjay/python-yarmp",
    packages=setuptools.find_packages(),
    install_requires=['python-mpd2','evdev','serial','select'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        'Intended Audience :: Developers',
        "Operating System :: POSIX :: Linux",
    ],
)