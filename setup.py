import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="email_function_failure_traceback",
    version="0.0.2",
    author="Stewart Renehan",
    author_email="sarenehan@gmail.com",
    description="Failed Function Error Traceback Email.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarenehan/email_function_failure_traceback",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
