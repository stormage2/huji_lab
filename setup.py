import setuptools

with open(r"README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="huji_lab",
    version="0.0.9",
    author="Agam Ankori",
    author_email="agam.ankori@mail.huji.ac.il",
    description="A physics lab data analysis package. Mostly a wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stormage2/huji_lab/",
    packages=setuptools.find_packages(),
	install_requires=["numpy","scipy","pandas","matplotlib","sympy","seaborn","uncertainties","mplcursors","wolframalpha","analytic_wfm"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)