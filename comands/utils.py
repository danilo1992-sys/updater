import subprocess
import getpass
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import Progress
import logging
import sys
import os

console = Console()


def sudo():
    password = getpass.getpass("Introduce la contraseña: ")
    proc = subprocess.Popen(
        ["sudo", "-S", "-v"], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    _, stderr = proc.communicate(input=password + "\n")

    if proc.returncode != 0:
        console.print(f":x: Error en la Autenticacion {stderr.strip()}")
        sys.exit(1)

    console.print(":heavy_check_mark: Autenticacion exitosa")


def ejecutar(comandos):
    for cmd in comandos:
        subprocess.run(f"sudo {cmd}", shell=True)


def info(text):
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        handlers=[RichHandler()],
    )
    log = logging.getLogger("rich")
    log.info(f"{text} :rocket:")


def warning(text):
    logging.basicConfig(
        level="WARNING",
        format="%(message)s",
        handlers=[RichHandler()],
    )
    log = logging.getLogger("rich")
    log.info(f"{text} :warning:")


def error(text):
    logging.basicConfig(
        level="ERROR",
        format="%(message)s",
        handlers=[RichHandler()],
    )
    log = logging.getLogger("rich")
    log.info(f"{text} :boom:")


def progress_bar(comandos):
    with Progress(transient=True) as progress:
        task = progress.add_task("Actualizando el sistema...", total=None)
        for cmd in comandos:
            subprocess.run(
                f"sudo {cmd}", shell=True,
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
