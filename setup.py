import setuptools

BASE_DIR = 'src'

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dbx-notebook-exporter',
    author='Jiri Koutny',
    author_email='jiri.koutny@datasentics.com',
    description='Databrics Notebook Exporter',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/DataSentics/dbx-notebook-exporter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'nbconvert.exporters': [
            'dbx-python-notebook = DbxNotebookExporter.Python.PythonNotebookExporter:PythonNotebookExporter',
            'dbx-json-notebook = DbxNotebookExporter.Json.JsonNotebookExporter:JsonNotebookExporter',
        ],
    },
    packages=setuptools.find_namespace_packages(where=BASE_DIR),
    package_data = {
        '': ['*.tpl']
    },
    package_dir={'': BASE_DIR},
    install_requires=[
        'nbconvert',
    ],
    version='0.1.1',
    script_args=['bdist_wheel'],
)
