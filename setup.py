import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='tgju_crawl',                           # should match the package folder
    packages=['tgju_crawl'],                     # should match the package folder
    version='1.0.1.1.5',                                # important for updates
    license='BSD (3-clause)',                                  # should match your chosen license
    description='A Python Module to Access tgju.org Historical Price',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='HOSSEIN AHMADI',
    author_email='hosein.ahmadi1997@yahoo.com',
    install_requires=['requests','jdatetime','pandas','bs4','datetime','lxml'],                  # list all packages that your package uses
   
)