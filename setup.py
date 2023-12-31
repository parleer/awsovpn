from setuptools import setup

setup(
    name="awsovpn",
    version="1.0.0",
    author="Flying Hippo",
    description="Aws OpenVPN Tool",
    packages=["awsovpn"],
    install_requires=[
        # "click",
        # "pytest",
        *open('requirements.txt').read().splitlines(),
    ],
    entry_points={
        "console_scripts": [
            "awsovpn = awsovpn.awsovpn:main",
        ],
    },
)