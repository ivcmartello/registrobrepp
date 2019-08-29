import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="registrobrepp",
    version="0.0.1",
    author="Ivan Carlos Martello",
    author_email="ivcmartello@gmail.com",
    description="Package to manage domains (RegistroBr)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ivcmartello/registrobrepp",
    keywords='domain epp registrobr',
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
          'EPP==0.9.1',
          'lxml==4.4.1',
          'python-decouple'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
