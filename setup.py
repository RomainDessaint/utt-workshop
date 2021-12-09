from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding="utf-8") as f:
    install_requires = f.read().split('\n')
    
setup(
    name='uttworkshop',
    install_requires=install_requires,
    packages=find_packages("src"),
    package_dir={"": "src"},
    version='0.1.0',
    description=long_description,
    long_description_content_type="text/markdown",
    author='Best groupe',
    license='',
    url="https://github.com/RomainDessaint/utt-workshop",
    python_requires=">=3.6"
)
