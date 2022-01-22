import typer
import ssg.site from Site

def main(source="content", dest="dist"):
    config = {"source": source, "dest":dest}

    Site(**config),build()

typer.run(main)
