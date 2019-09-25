from setuptools import setup, find_packages

setup(
    name='pybitrix24',
    description='A tiny Python3 client to make requests of Bitrix24 API.',
    keywords='bitrix24 api rest python3 client',
    version='0.4.0',
    url='https://github.com/yarbshk/bitrix24-python3-client',
    author='Yuriy Rabeshko',
    author_email='george.rabeshko@gmail.com',
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
