from setuptools import setup, find_packages
from typing import List


def get_requirements()-> list[str]:
    """
    This Function will return list of requirements

    """
    requirement_list: List [str]=[]

    try:
        #open and read the requirements.txt file
        with open('requirements.txt','r') as file:
            # read list from file
            lines=file.readlines()
            #process each line
            for line in lines:
                #strip whitespace and newline characters
                requirement=line.strip()
                #ignore empty lines and -e .

                if requirement and requirement!='-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print('requirements.txt file not found.')

    return requirement_list


print(get_requirements())

setup(
    name="AI_Trip_Planner",
    version="0.0.1",
    author="Meet P Bhatt",
    author_email= "meetbhatt96.mb@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)