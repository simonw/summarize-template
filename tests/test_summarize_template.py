from click.testing import CliRunner
from summarize_template.cli import cli


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


TEMPLATE = """
{% extends "base.html" %}

{% block title %}This is the title{% endblock %}

{% block content %}
<h1>{{ title }}</h1>
{% if docs %}
    <ul>
        {% for doc in docs %}
            <li><a href="{{ doc.url }}">{{ doc.title }}</a></li>
        {% endfor %}
    </ul>
{% endif %}
{% endblock %}
""".strip()

EXPECTED = """
{% extends "base.html" %}
{% block title %}   {% endblock %}
{% block content %}
{{ title }}
{% if docs %}
        {% for doc in docs %}
             {{ doc.url }}{{ doc.title }}
        {% endfor %}
{% endif %}
{% endblock %}
"""


def test_summarize():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["-"], input=TEMPLATE)
        assert result.exit_code == 0
        assert result.output.strip() == EXPECTED.strip()
