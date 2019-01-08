import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kv_prod_union",
    version="0.1.0",
    author="Wen Jie Liang",
    author_email="l.wen.jie@qq.com",
    description="parameter sampling config",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/2bright/kv_prod_union",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    license="Apache-2.0",
    packages=setuptools.find_packages(),
)
