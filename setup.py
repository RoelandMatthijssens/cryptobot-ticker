import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ticker",
    version="0.0.1",
    author="Enermis",
    author_email="fulgens.ailurus@gmail.com",
    description="A ticker for bitmex symbols",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RoelandMatthijssens/cryptobot-ticker",
    py_modules=["ticker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: IDGAF License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
