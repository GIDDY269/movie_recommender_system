from setuptools import find_packages,setup



setup(
      name='movie_recommender',
      version= '0.0.1',
      author='giddy',
      author_email='oviemunooboro@gamil.com',
      packages=find_packages(),
      install_requires=[line.strip() for line in open('requirements.txt')] )