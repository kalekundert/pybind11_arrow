from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension
import pyarrow as pa

pa.create_library_symlinks()
setup(
        ext_modules=[
            Pybind11Extension(
                name='demo',
                sources=['demo.cc'],
                include_dirs=[pa.get_include()],
                libraries=pa.get_libraries(),
                library_dirs=pa.get_library_dirs(),
                cxx_std=17,
            ),
        ],
)
