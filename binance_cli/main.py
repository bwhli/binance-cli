import typer

app = typer.Typer()


@app.command()
def debug():
    print(__name__)
