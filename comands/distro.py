from rich.console import Console
from rich.table import Table
import platform


def paquetes(gestor):

    dist = platform.freedesktop_os_release()
    console = Console()
    table = Table(box=None)
    table.add_column("Propiedad", style="cyan")
    table.add_column("Valor", style="green")
    table.add_row("Gestor de paquetes", gestor)
    table.add_row("Distribucion", dist.get("NAME", "Desconocida"))
    console.print(table)

    return gestor
