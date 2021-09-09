import setuptools
# ---------------------------------------------------
# Requirements
# python-pyqt5
# python-qdarkstyle
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='xerolinux-xerolinux_rollback',
    version='0.3.6',
    author="The Duck Channel",
    author_email="fredcox@gmail.com",
    description='BTRFS xerolinux_rollback utility fom Xerolinux Distro',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/theduckchannel/xerolinux-rollback",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.8',
    scripts=['bin/xerolinux_rollback'],

    install_requires=[
        'PyQt6'
    ],
    include_package_data=True,
    zip_safe=False,
)



