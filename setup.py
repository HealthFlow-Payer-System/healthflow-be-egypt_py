from pathlib import Path
from setuptools import find_packages, setup

README = Path(__file__).with_name("README.md").read_text(encoding="utf-8")

setup(
    name="healthflow-be-egypt",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    license="GNU AGPL v3",
    description="Egypt-specific localization and validation helpers for HealthFlow Payer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/HealthFlowEgy/healthflow-be-egypt_py",
    install_requires=["django"],
    classifiers=[
        "Framework :: Django",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
    ],
)
