#!/usr/bin/python
from distutils.core import setup
from distutils.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

extensions = [
    Extension('cymesh.vector3D', ['cymesh/vector3D.pyx']),
    Extension('cymesh.structures', ['cymesh/structures.pyx']),
    Extension('cymesh.mesh', ['cymesh/mesh.pyx'])
]

setup(
    name = "cymesh",
    version = '1.0.0',
    author = 'joelsimon.net',
    author_email='joelsimon6@gmail.com',
    install_requires = ['numpy', 'cython'],
    license = 'MIT',
    cmdclass={'build_ext' : build_ext},
    packages = ['cymesh'],
    ext_modules = cythonize(
        extensions,
    )
)
