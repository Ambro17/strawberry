import click

from graphql.error import GraphQLError

from strawberry.cli.commands.schema_importer import sdl_importer


@click.command(
    "import-schema", short_help="Transpiles SDL from a path to strawberry types"
)
@click.argument("schema", type=str, required=True, nargs=-1)
def import_schema(schema):
    """Parses SDL to strawberry types and prints to console"""
    strawberries = ""
    for s in schema:
        try:
            sdl_string = sdl_importer.file_to_string(s)
            strawberries += sdl_importer.import_sdl(sdl_string)

        except FileNotFoundError:
            print(f"File not found on path: {s}")

        except GraphQLError:
            print(f"File {s} contains syntax errors")

    print("# Generated by strawberry")
    click.echo(strawberries)
