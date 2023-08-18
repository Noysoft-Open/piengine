import setuptools

setuptools.setup(
  name="piengine",
  description="Piengine is a game engine framework.",
  version="0.0.1",
  author="Jayson B. Abad",
  author_email="jayson_abad@outlook.com",
  license="MIT",
  packages=["piengine", "piengine.core", "piengine.main", "piengine.utils"],
  install_requires=[
    'glfw',
    'pyopengl',
    'pyopengl_accelerate',
    'numpy',
    'pyrr',
    'pillow'
  ],
  zip_safe=False
)
# this package must install offline
# 'pyopengl_accelerate',
# python setup.py sdist bdist_wheel
# sdist and bdist_wheel will create dirstibutable pywheel
# python setup.py install
# pip install piengine
# pyinstaller 