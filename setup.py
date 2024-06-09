from setuptools import setup, find_packages

setup(
    name='mobiledogs',
    version='0.1',
    description='MobileDogs_API is a dog monitoring and management system',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Ivan Pomogaev',
    author_email='shokorev2003@gmail.com',
    maintainer='Shokorev Aleksandr',
    maintainer_email='shokorev2003@gmail.com',
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
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
