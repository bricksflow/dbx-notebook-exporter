import os
import os.path
from jinja2 import contextfilter
from nbconvert.exporters.templateexporter import TemplateExporter
from DbxNotebookExporter.Json.formatCellContent import formatCellContent

class JsonNotebookExporter(TemplateExporter):
    export_from_notebook = 'Databricks JSON Notebook'

    def _file_extension_default(self):
        return '.python'

    @property
    def template_path(self):
        return super().template_path + [os.path.dirname(__file__)]

    def _template_file_default(self):
        return 'json_notebook'

    @contextfilter
    def formatCellContent(self, context, source):
        return formatCellContent(source)

    def default_filters(self):
        yield ('formatCellContent', self.formatCellContent)
