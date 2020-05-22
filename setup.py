from distutils.core import Extension, setup

setup(
    name="pyprocar",
    version="5.3.1",
    author="Francisco Munoz,Aldo Romero,Sobhit Singh,Uthpala Herath,Pedram Tavadze,Eric Bousquet, Xu He",
    author_email="fvmunoz@gmail.com,alromero@mail.wvu.edu,smsingh@mix.wvu.edu,ukh0001@mix.wvu.edu,petavazohi@mix.wvu.edu,eric.bousquet@uliege.be,mailhexu@gmail.com",
    url="https://github.com/romerogroup/pyprocar",
    download_url="https://github.com/romerogroup/pyprocar/archive/5.3.1.tar.gz",
    packages=[
        "pyprocar",
        "pyprocar.utilsprocar",
        "pyprocar.procarparser",
        "pyprocar.procarfilefilter",
        "pyprocar.procarplot",
        "pyprocar.procarsymmetry",
        "pyprocar.procarunfold",
        "pyprocar.fermisurface",
        "pyprocar.procarselect",
        "pyprocar.elkparser",
        "pyprocar.abinitparser",
        "pyprocar.doscarplot",
    ],
    license="LICENSE.txt",
    description="A Python library for electronic structure pre/post-processing.",
    install_requires=[
        "matplotlib",
        "seekpath",
        "scipy",
        "ase",
        "scikit-image",
        "mayavi",
        "pychemia",
    ],
    scripts=["bin/procar"],
)
