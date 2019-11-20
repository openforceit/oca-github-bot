import io
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="orco-bot",
    use_scm_version=True,
    long_description=long_description,
    author="Openforce",
    author_email="devops@openforce.it",
    url="https://github.com/openforceit/orco-bot",
    python_requires=">=3.6",
    setup_requires=["setuptools_scm"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        # aiohttp ang gitgethub for the webhook app
        "aiohttp",
        "gidgethub",
        "appdirs",
        # GitHub client
        "github3.py>=1.3.0",
        # celery and celery monitoring for the task queue
        "flower",
        "celery[redis]",
        # Odoo
        "odoorpc",
        # Sentry
        "raven",
        # setuptools and twine to build, check and upload wheels
        "setuptools",
        "twine",
        "wheel",
    ],
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
)
