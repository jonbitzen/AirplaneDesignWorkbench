from setuptools import setup
import os
# from freecad.workbench_starterkit.version import __version__
# name: this is the name of the distribution.
# Packages using the same name here cannot be installed together

version_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 
                            "freecad", "airplane_design", "version.py")
with open(version_path) as fp:
    exec(fp.read())

setup(name='freecad.airplane_design',
      version=str(__version__),
      packages=['freecad',
                'freecad.airplane_design'],
      maintainer="Jonathan E. Railsback",
      maintainer_email="jonbitzen@hotmail.com",
      url="",
      description="template for a freecad extensions, installable with pip",
      install_requires=[],
      include_package_data=True)
