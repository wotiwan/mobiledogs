from setuptools import setup, find_packages

setup(
   name='mobiledogs',
   version='1.0',
   description='MobileDogs_API is a dog monitoring and management system.',
   license='MIT',
   author='shokorev25',
   author_email='shokorev25@gmail.com',
   url='https://github.com/wotiwan/mobiledogs',
   packages=find_packages(),
   install_requires=[
        'fastapi~=0.111.0',
        'uvicorn',
        'sqlalchemy~=2.0.30',
        'pydantic~=2.7.3',
        'mysql-connector-python',
        'requests',
        'sphinx',
        'sphinx-autobuild',
        'sphinx_rtd_theme',
    ],
   extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
   },
   python_requires='>=3',
)
