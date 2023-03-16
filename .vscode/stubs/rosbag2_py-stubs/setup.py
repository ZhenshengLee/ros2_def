from setuptools import setup
import os


def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return dict(package=stubs)


setup(
    name='rosbag2_py-stubs',
    maintainer="rosbag2_py Developers",
    maintainer_email="example@python.org",
    description="PEP 561 type stubs for rosbag2_py",
    version='1.0',
    packages=['rosbag2_py-stubs'],
    # PEP 561 requires these
    install_requires=['rosbag2_py'],
    package_data=find_stubs('rosbag2_py-stubs'),
)