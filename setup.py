import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sacredfig",
    version="0.1.0",
    author="Luc Rocher",
    author_email="luc@rocher.lc",
    description="Concise and clear figures for scientific publishing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cynddl/sacredfig",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'matplotlib; python_version >= "3.3"',
    ],
)