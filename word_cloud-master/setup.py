from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='wordcloud',
    version='1.0.0',
    url='https://github.com/amueller/word_cloud',
    license='MIT',
    ext_modules=cythonize('wordcloud/query_integral_image.pyx'),
    packages=['wordcloud'],
    package_data={'wordcloud': ['stopwords']}
)
