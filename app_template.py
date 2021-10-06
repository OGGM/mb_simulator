template = """
{% extends base %}

<!-- goes in body -->
{% block postamble %}
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.6.0/css/bootstrap.min.css">
{% endblock %}

<!-- goes in body -->
{% block contents %}
<app >
  <div>
      {{ embed(roots.header) }}
  </div>
  <menu_and_figures>
      {{ embed(roots.menu_and_figures) }}
  </menu_and_figures>
</app>
{% endblock %}
"""
