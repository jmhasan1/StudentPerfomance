# find packages - automatically find out all the poackages in the Machine Learning application (directory)that we have created
from setuptools import find_packages , setup
from typing import List

HYPHEN_E_DOT = '-e .'

# function will take input parameter as file path in form of string and will return a List
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requiremenmts
    '''
    requirements = []
    # opening requirements as a temporary file
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() 
        # list comprehension below to replace \n with blanks at the end of each line
        requirements=[req.replace("\n"," ")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# metadata about the project 
# doing the setup
setup(
    name='StudentPerfomance',
    version='0.0.1',
    author='Jahid Hasan',
    author_email='jmhasan17@gmail.com',
    packages=find_packages(),
    install_requires =get_requirements('requirements.txt')
)
# whenever find packages is running it will look for folders with __init__ as package as build this  (will directly cosider src as a package itself ; then builds this)
# entire project development will happen inside src folder
# install_requires will automatically install all the required libraries

# -e . in requirements.txt automatically triggers setup.py file whenever we try to install requirements