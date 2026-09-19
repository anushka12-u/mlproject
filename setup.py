from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->list:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements
setup(
    name="mlproject",
    version="0.0.1",
    author="Anushka",
    author_email="anushkaawasthi902@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)