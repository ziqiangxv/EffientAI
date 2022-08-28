# -*- coding: utf-8 -*-

''''''

import os

from distutils.command.register import register

from distutils.command.upload import upload

from setuptools import find_packages, setup

from setuptools.command.build_py import build_py

file_dir = os.path.relpath(os.path.dirname(os.path.abspath(__file__)), os.getcwd())

version_file = os.path.join(file_dir, '.version')

with open(version_file, 'r') as f:
    version = f.readline().strip()

readme_file = os.path.join(file_dir, 'README.md')

with open(readme_file, 'r') as f:
    long_description = f.read()

url = 'https://gitlab.shukun.net/algorithm-engineering/services/algorithm-task-scheduler.git'

# class BuildPy(build_py):
#     def run(self):
#         os.system('sh proto2py.sh')

#         self.packages = find_packages()

#         super().run()

class Register(register):
    def _get_rc_file(self):
        return os.path.join(file_dir, '.pypirc')

class Upload(upload):
    def _get_rc_file(self):
        return os.path.join(file_dir, '.pypirc')

# install_requires = ['grpcio==1.42.0', 'protobuf==3.19.1']

install_requires = []

setup(
        name = 'algorithm-task-scheduler',
        version = version,
        description = 'Algorithm Task Scheduler ...',
        long_description = long_description,
        long_description_content_type = 'text/markdown',
        author = 'Ziqiang-XU',
        author_email = 'xuzq1@shukun.net',
        maintainer = 'Algorithm-Engineering-Team',
        maintainer_email = 'xuke@shukun.net',
        url = url,
        packages = find_packages(),
        classifiers = ['Service'],
        # cmdclass = {'build_py': BuildPy, 'register': Register, 'upload': Upload},
        cmdclass = {'register': Register, 'upload': Upload},
        include_package_data = True,
        install_requires = install_requires,
        python_requires = '>=3.8.0'
	)

