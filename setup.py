from setuptools import find_packages,setup
from pathlib import Path
import os

requirements_dir = os.path.join(Path(__file__).resolve().parent,"requirements.txt")

def get_requirements(file_path:str):
    Hyphen_e_dot = "-e ."
    with open(file_path) as file_obj:
        packages = file_obj.read().splitlines()
        if Hyphen_e_dot in packages:
            packages.remove(Hyphen_e_dot)
        
    return packages


setup (
    name = "wine_quality"
    version = "0.0.1"
    author = "abhinav"
    packages = find_packages()
    install_requires = get_requirements(file_path = requirements_dir)
)