from setuptools import setup, find_packages

setup(
    name="git-pulse",
    version="1.0.0",
    author="Prajwal Khadka",
    author_email="prajwalkhadkcr7@gmail.com",
    description="The aesthetic Git terminal dashboard and repository health analyzer",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/prajwalkkhadka-cpu/git-pulse",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Topic :: Software Development :: Version Control :: Git",
    ],
    python_requires=">=3.8",
    install_requires=[
        "colorama>=0.4.6",
        "tabulate>=0.9.0",
        "rich>=13.0.0",
    ],
    entry_points={
        "console_scripts": [
            "git-pulse=git_pulse.cli:main",
        ],
    },
)
