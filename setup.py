from setuptools import setup
import sys

install_requires = ['six']
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    install_requires.append('ordereddict')


setup(
    name='pyfaidx',
    provides='pyfaidx',
    version='0.2.5',
    author='Matthew Shirley',
    author_email='mdshw5@gmail.com',
    url='http://mattshirley.com',
    description='pyfaidx: efficient pythonic random '
                'access to fasta subsequences',
    license='MIT',
    packages=['pyfaidx'],
    install_requires=install_requires,
    entry_points={'console_scripts': ['faidx = pyfaidx.cli:main']},
    classifiers=[
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: MIT License",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "Natural Language :: English",
            "Operating System :: Unix",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 2.6",
            "Programming Language :: Python :: Implementation :: PyPy",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)
