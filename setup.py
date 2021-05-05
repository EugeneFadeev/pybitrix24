from setuptools import setup, find_packages

setup(
    name='pybitrix24-rest',
    description='A Python3 Rest API access',
    keywords='bitrix24 rest python3',
    version='0.5.0',
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
    ],
    python_requires='>=3'
)
