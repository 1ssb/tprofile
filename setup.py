from setuptools import setup, find_packages

setup(
    name="tprofiler",
    version="1.0.0",
    author="Subhransu S. Bhattacharjee",
    author_email="Subhransu.Bhattacharjee@anu.edu.au",
    description="A combined time and memory profiler using psutil",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/1ssb/tprofile",
    packages=find_packages(),
    install_requires=[
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "tprofiler = tprofiler.core:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
