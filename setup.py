'''
MIT License

Copyright (c) 2019 Hyeonki Hong <hhk7734@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

from setuptools import setup, find_packages, Extension
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from os import path
import subprocess
import sys

here = path.abspath(path.dirname(__file__))
script = path.join(here, "install_requires.sh")
if subprocess.call(["sudo", "sh", script]) != 0:
    sys.exit(1)

classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX :: Linux",
    "Intended Audience :: Developers",
    "Topic :: Software Development",
    "Topic :: System :: Hardware",
]

ext_modules = [
    Extension(
        "Odroid._GPIO",
        [
            "wrap/wiringPi.i"
        ],
        libraries = ["wiringPi", "wiringPiDev", "m", "pthread", "rt", "crypt"],
    ),
]

'''
for upload
'''
class sdist_after_ext(sdist):
    def run(self):
        self.run_command("build_ext")
        return sdist.run(self)

'''
in the distribution when running setup.py bdist or bdist_wheel.
'''
class build_py_after_ext(build_py):
    def run(self):
        self.run_command("build_ext")
        return build_py.run(self)

setup(
    name                            = "Odroid.GPIO",
    version                         = "0.0.2",
    description                     = "A module to control Odroid GPIO channels",
    url                             = "https://github.com/hhk7734/odroid_gpio",
    classifiers                     = classifiers,
    keywords                        = ["Odroid", "GPIO"],
    package_dir                     = {"": "src"},
    packages                        = find_packages('src'),
    license                         = "MIT",
    ext_modules                     = ext_modules,
    project_urls                    = {
                                        'Source': 'https://github.com/hhk7734/odroid_gpio',
                                    },
    cmdclass                        = {'sdist' : sdist_after_ext},
)