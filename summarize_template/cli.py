import click
import re

tags_re = re.compile(r"(\{\%.*?\%\}|\{\{.*?\}\})")
not_whitespace_re = re.compile(r"[^\s]")


@click.command()
@click.version_option()
@click.argument("file", type=click.File("r"))
def cli(file):
    "Show a summary of the specified template file"
    template = file.read()
    tokens = tags_re.split(template)
    output = []
    for token in tokens:
        if tags_re.match(token):
            output.append(token)
        else:
            # Output just the whitespace
            output.append(not_whitespace_re.sub("", token))
    # Join it all together, then output everything that's not a blank line
    lines = "".join(output).split("\n")
    for line in lines:
        if line.strip():
            click.echo(line)
