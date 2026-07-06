import shutil
from rich.prompt import Prompt
from rich.console import Console
from comands.utils import check_folder, info
from pathlib import Path
from datetime import datetime


console = Console()


def folder(name=None):
    if name is None:
        name = Prompt.ask(
            "Introduce el [bold cyan]nombre de la carpeta[/bold cyan]",
            default="nueva_carpeta",
            validate=check_folder,
            validation_error_message="[red]Nombre inválido. No uses caracteres especiales.[/red]",
        )
    check_folder(name)
    return Path(name)


def comprimir():
    home = Path.home()
    origen = home / ".config"
    destino = folder()

    time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"destino_{time}"

    archivo = shutil.make_archive(
        base=str(destino / nombre_archivo), format="zip", root_dir=str(origen)
    )
    info(f"Archivo creado: {archivo}")
