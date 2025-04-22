from setuptools import setup, find_packages

# Load dependencies
try:
    with open("requirement.txt", "r") as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = ["soundfile", "edge_tts", "sounddevice"]

setup(
    name="tts_accelerator",  # or anything you want
    version="0.1.0",
    description="Text-to-Speech accelerator with split, generate, and play functions",
    author="Ranjit",
    author_email="ranjitdax89@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
