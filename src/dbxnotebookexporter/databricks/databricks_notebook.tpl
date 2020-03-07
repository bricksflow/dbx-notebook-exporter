{%- extends 'null.tpl' -%}

{% block header %}
# Databricks notebook source

{{ resources.libsRun }}
{% endblock header %}

{% block in_prompt %}
# COMMAND ----------
{% endblock in_prompt %}

{% block input %}
{{ cell.source | ipython2python }}
{% endblock input %}

{% block markdowncell scoped %}
{{ cell.source | comment_lines }}
{% endblock markdowncell %}
