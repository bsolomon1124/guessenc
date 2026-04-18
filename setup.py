import os
import re

from setuptools import setup

# PyPI:
# $ python -m build
# $ twine upload dist/guessenc-x.y*

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "guessenc", "__init__.py"), encoding="utf-8") as f:
    __version__ = re.search(r'^__version__\s*=\s*"([^"]+)"', f.read(), re.M).group(1)

if __name__ == "__main__":
    setup(
        name="guessenc",
        version=__version__,
        author="Brad Solomon",
        author_email="brad.solomon.1124@gmail.com",
        description="[DEPRECATED] Infer HTML encoding from response headers & content. Use charset-normalizer or bs4.UnicodeDammit instead.",
        license="MIT",
        keywords="encoding http html chardet detection",
        url="https://github.com/bsolomon1124/guessenc",
        long_description=open(os.path.join(here, "README.md"), encoding="utf-8").read(),
        long_description_content_type="text/markdown",
        install_requires=["lxml", "chardet"],
        packages=["guessenc"],
        tests_require=["pytest"],
        python_requires=">=3.5",
        classifiers=[
            "Intended Audience :: Developers",
            "Development Status :: 7 - Inactive",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
        ],
    )
