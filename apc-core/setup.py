from setuptools import setup, find_packages

setup(
    name="apc-core",
    version="0.1.0",
    description="APC (Agent Protocol Conductor) core protocol library for decentralized agent orchestration.",
    author="APC Contributors",
    packages=find_packages(),
    install_requires=[
        "grpcio",
        "grpcio-tools",
        "websockets",
        "redis",
        "boto3"
    ],
    python_requires=">=3.8",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
