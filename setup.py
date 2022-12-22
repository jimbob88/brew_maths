from pathlib import Path

from setuptools import setup

setup(
    name="brew_maths",
    version="0.0.1",
    description="A Recipe Calculation Module",
    author="James Blackburn",
    packages=['brew_maths'],
    install_requires=Path('./requirements.txt').read_text(encoding='utf-8').splitlines(),
)
