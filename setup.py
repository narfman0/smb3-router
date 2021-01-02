from setuptools import setup, find_packages


setup(
    name="smb3-router",
    version="0.1.0",
    description=("Create a DAG for smb3 for use with routing"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="smb3-router",
    author="Jon Robison",
    author_email="narfman0@gmail.com",
    license="LICENSE",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True,
    install_requires=["openpyxl"],
    test_suite="tests",
)
