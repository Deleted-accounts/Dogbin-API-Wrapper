import setuptools


with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt") as f:
    dependencies = [_.strip() for _ in f]


setuptools.setup(
    name="dogbin",
    version=0.1,
    description="Dogbin API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNU Lesser General Public License v3 (LGPLv3)",
    author="DeletedAccounts",
    author_email="deletedaccuonts@hi2.in",
    url="https://github.com/Deleted-accounts/Dogbin-API-Wrapper",
    packages=setuptools.find_packages(exclude="example.py"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.9",
    ],
    install_requires=dependencies,
    python_requires=">=3.7",
)