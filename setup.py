from setuptools import setup


with open('README.md') as f:
    long_description = f.read()

setup(
    name='AlphaCopy',
    version='0.0.0',
    license='GNU General Public License v3.0',
    description='A Raspberry Pi backup application with GUI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ozzysp/AlphaCopy',
    package_dir={'': 'src'},
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8'
    ],
    platforms='Linux',
)
