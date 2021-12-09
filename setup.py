from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
setup(
    name='utt-workshop',
    packages=find_packages(),
    version='0.1.0',
    description=long_description,
    long_description_content_type="text/markdown",
    author='Best groupe',
    license='',
    url="https://github.com/RomainDessaint/utt-workshop",
    python_requires=">=3.6"
)
