from setuptools import find_packages,setup
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

REQUIREMENT_FILE_NAME="requirements.txt"

setup(
      
    name='mlproject',
    version='0.0.1',
    author='Sai Kiran Thota',
    author_email='saikirant375@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(REQUIREMENT_FILE_NAME)
)