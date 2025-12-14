from setuptools import setup, find_packages


setup(
    name="oneheart",
    version="0.1.0",
    description="ONEHEART — small scaffold for helping others",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.10",
    include_package_data=True,
)
