from setuptools import find_packages,setup
from typing import List 

def get_requirements()->list[str]:
    requirements_list:List[str]=[]
    # with open("requirements.txt")as file:
    #     requirements_list=file.read().splitlines()
    
    
    return requirements_list
    

setup(
    
    name="APS Fault Prediction",
    version="0.0.1",
    author="siri",
    author_email="sridharsahu51@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),#["pymongo"]
    )