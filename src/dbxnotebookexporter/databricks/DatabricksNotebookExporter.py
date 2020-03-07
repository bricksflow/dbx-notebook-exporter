import os
import os.path

from nbconvert.exporters.templateexporter import TemplateExporter

class DatabricksNotebookExporter(TemplateExporter):
    export_from_notebook = 'databricks Python Notebook'

    def _file_extension_default(self):
        return '.py'

    @property
    def template_path(self):
        return super().template_path + [os.path.dirname(__file__)]

    def _template_file_default(self):
        return 'databricks_notebook'
