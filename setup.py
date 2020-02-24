from setuptools import setup

setup(
    name="autosuspend-mcstatus",
    version="0.1",
    description="autosuspend checks for your Minecraft server",
    url="https://github.com/jakobend/autosuspend-mcstatus",
    author="jakobend",
    license="MIT",
    packages=["autosuspend_mcstatus"],
    install_requires=[
        "autosuspend",
        "mcstatus"
    ],
    zip_safe=True
)
