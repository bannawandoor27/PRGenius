from setuptools import setup, find_packages

setup(
    name='PRGenius',  # Your package name
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=[
        'requests',  # Ensure you list all dependencies
        'openai',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'prgenius=prgenius.pr_creator:main',  # Allows users to run your tool from the command line
        ],
    },
    author='Your Name',
    author_email='your_email@example.com',
    description='Automates PR creation on GitHub using GPT-3 for description generation based on commit messages.',
    keywords='GitHub PR automation GPT-3',
    url='https://github.com/yourusername/PRGenius',  # Project home page or repository URL
    license='MIT',  # Choose the appropriate license
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose the appropriate development status
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Ensure this matches your chosen license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
