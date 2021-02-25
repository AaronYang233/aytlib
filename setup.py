import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'aytlib',
    version = '0.0.5',
    description = "A example package",
    author = 'AaronYang',
    author_email = '3300390005@qq.com',
    url = 'https://test.pypi.org/legacy/',
    project_urls={
        "tlib":"https://github.com/AaronYang233/aytlib"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data = True,
    zip_safe = False,
    packages=setuptools.find_packages(),
    python_requires='>=3',
)