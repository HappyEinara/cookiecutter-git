import os
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(HERE, "README.md")) as handle:
    LONG_DESCRIPTION = handle.read()

with open(os.path.join(HERE, "cookiecutter_git", "VERSION")) as handle:
    VERSION = handle.read().strip()

setuptools.setup(
    name="cookiecutter-git",
    version=VERSION,
    author="Dave Lowrey",
    author_email="dave.lowrey@einara.com",
    description="A wrapper around cookie-cutter to provide metadata from the template repo.",
    entry_points={
        'console_scripts': [
            'cookiecutter-git=cookiecutter_git.cli:cli'],
    },
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/HappyEinara/cookiecutter-git",
    packages=setuptools.find_packages(include=['cookiecutter_git']),
    package_data={"cookiecutter_git": ["VERSION"]},
    classifiers=[
        "Programming Language :: Python :: 3",
	"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.8',
    install_requires=[
        'click',
        'logzero',
        'requests',
    ],
    extras_require={
        'dev': [
            'black',
            'tox'],
        'ci': [
            'tox'],
    }
)
