from setuptools import setup, find_packages

setup(
    name='python-bitrix24-wrapper',
    description='A Python3 wrapper to make requests of Bitrix24 API with multi_urlencode.',
    keywords='bitrix24 api rest python3 client',
    version='0.4.0',
    url='https://github.com/EugeneFadeev/pybitrix24',
    author='Eugene Fadeev',
    author_email='fadeev2012fadeev@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    packages=find_packages(),
    install_requires=[
        'requests>=2.18.0'
        'multidimensional_urlencode>=0.0.4'
    ],
    python_requires='>=3'
)
