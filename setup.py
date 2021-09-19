from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
    "matplotlib",
    "ipython",
    "rebound",
    "numpy",
    "astropy",
]


setup(
    name="dsw", 
    version="0.1.07",
    author="Cameron McEwing",
    author_email="tech.mechanic@gmail.com",
    description="Tools used by Deep Sky Wonder",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeepSkyWonder/dsw",
    install_requires=requirements,
    
    packages=find_packages("dsw"),
    package_dir={"": "dsw"},
    package_data={
        "": ["*.txt"],
        "cepheid": ["BVI_templates/*.dat"],
    },
    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
