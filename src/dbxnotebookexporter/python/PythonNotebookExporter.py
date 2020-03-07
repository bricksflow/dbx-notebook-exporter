import os
import os.path

from nbconvert.exporters.templateexporter import TemplateExporter

class PythonNotebookExporter(TemplateExporter):
    export_from_notebook = 'Python Notebook'

    def _file_extension_default(self):
        return '.py'

    @property
    def template_path(self):
        return super().template_path + [os.path.dirname(__file__)]

    def _template_file_default(self):
        return 'python_notebook'
