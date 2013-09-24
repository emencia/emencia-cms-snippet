from setuptools import setup, find_packages

setup(
    name='emencia-cms-snippet',
    version=__import__('snippet').__version__,
    description=__import__('snippet').__doc__,
    long_description=open('README.rst').read(),
    author='David Thenon',
    author_email='dthenon@emencia.com',
    url='http://pypi.python.org/pypi/emencia-cms-snippet',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'django-cms>=2.3',
        'djangocodemirror>=0.9.3',
    ],
    include_package_data=True,
    zip_safe=False
)