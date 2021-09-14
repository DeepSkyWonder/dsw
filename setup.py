import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
    "matplotlib",
]


setuptools.setup(
    name="dsw", 
    version="0.1.01",
    author="Cameron McEwing",
    author_email="tech.mechanic@gmail.com",
    description="Tools used by Deep Sky Wonder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepSkyWonder/dsw",
    install_requires=requirements,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
