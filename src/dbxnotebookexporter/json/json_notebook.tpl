{%- extends 'null.tpl' -%}

{%- set counter = {'i': 1} -%}

{%- macro increment(dct, inc=1) -%}
    {% if dct.update({'i': dct['i'] + inc}) %} {% endif %}
{%- endmacro -%}

{%- block header -%}
{
"version":"NotebookV1",
"name":"{{ resources.metadata.name }}",
"language":"python",
"commands":[
{%- endblock header -%}

{%- block codecell -%}
  {
    "version":"CommandV1",
    "subtype":"command",
    "commandType":"auto",
    "position":{{ counter.i }}.0,
    "command":"{{ cell.source | formatCellContent }}",
    "commandVersion":1,
    "state": "finished",
    "workflows":[],
    "collapsed":false,
    "bindings":{},
    "inputWidgets":{},
    "displayType":"table",
    "width":"auto",
    "height":"auto",
    "useConsistentColors":false,
    "customPlotOptions":{},
    "commentThread":[],
    "commentsVisible":false,
    "parentHierarchy":[],
    "diffInserts":[],
    "diffDeletes":[],
    "globalVars":{},
    "commandTitle":"",
    "showCommandTitle":false,
    "hideCommandCode":false,
    "hideCommandResult":false,
    "isLockedInExamMode":false,
    "streamStates":{},
    "datasetPreviewNameToCmdIdMap":{}
  }
  {%- if counter.i < nb.cells|length -%}
  ,
  {%- endif -%}
  {{- increment(counter) -}}

{%- endblock codecell -%}

{% block markdowncell scoped %}
  {
    "version":"CommandV1",
    "subtype":"command",
    "commandType":"auto",
    "position":{{ counter.i }}.0,
    "command":"%md\n\n{{ cell.source | formatCellContent }}",
    "commandVersion":1
  }
  {%- if counter.i < nb.cells|length -%}
  ,
  {%- endif -%}
  {{- increment(counter) -}}
{% endblock markdowncell %}

{%- block footer -%}
],
"dashboards":[],
"globalVars":{},
"inputWidgets":{}
}
{%- endblock footer-%}
