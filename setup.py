import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='PRGenius', 
    version='0.2.0',  
    packages=find_packages(), 
    install_requires=[
        'requests', 
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'prgenius=prgenius.pr_creator:main',  
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='Automates PR creation on GitHub using GPT-3 for description generation based on commit messages.',
    long_description=read('README.md'),  
    long_description_content_type='text/markdown',
    keywords='GitHub PR automation GPT-3',
    url='https://github.com/yourusername/PRGenius',  
    license='MIT',  
    classifiers=[
        'Development Status :: 3 - Alpha',  
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
