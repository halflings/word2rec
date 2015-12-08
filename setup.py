from distutils.core import setup

requirements = ['gensim>=0.12']

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='Word2Rec',
    description='A (simple) recommender system based on word2vec.',
    long_description=readme,
    author='Ahmed Kachkach',
    author_email='ahmed.kachkach@gmail.com',
    version='0.1',
    packages=['word2rec'],
    install_requires=requirements,
    license='Apache 2.0'
)
