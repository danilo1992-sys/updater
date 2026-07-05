from rich import console
from comands.utils import ejecutar, warning, info
import subprocess
import shutil
from rich.console import Console


def detectar():
    gestores = [
        "pacman",
        "apt",
        "dnf",
        "zypper",
        "apk",
    ]

    for gestor in gestores:
        if shutil.which(gestor):
            return gestor
    if shutil.which("brew"):
        return "brew"
    return None


def apt():
    comands = [
        "apt update -y",
        "apt upgrade -y",
        "apt full-upgrade -y",
        "apt autoremove -y",
        "apt clean",
    ]
    ejecutar(comands)


def pacman():
    comands = [
        "sudo rm -f /var/cache/pacman/pkg/download-*",
        "sudo rm -f /var/lib/pacman/db.lck",
        "pacman -Syu --noprogressbar",
        "pacman -Sc --noprogressbar",
    ]
    ejecutar(comands)

    orfanos = subprocess.run(
        ["pacman", "-Qtdq"], capture_output=True, text=True
    ).stdout.strip()
    if orfanos:
        ejecutar(["pacman -Rns $(pacman -Qtdq) --noprogressbar"])


def dnf():
    comands = [
        "dnf check-update",
        "dnf upgrade -y",
        "dnf autoremove -y",
    ]
    ejecutar(comands)


def zypper():
    comands = [
        "zypper refresh",
        "zypper update -y",
        "zypper clean",
    ]
    ejecutar(comands)


def apk():
    comands = [
        "apk update",
        "apk upgrade",
        "apk cache clean",
    ]
    ejecutar(comands)


def brew():
    comands = [
        "brew update",
        "brew upgrade",
        "brew cleanup",
    ]
    ejecutar(comands)


def update():
    gestor = detectar()

    if gestor == "apt":
        apt()
    elif gestor == "pacman":
        pacman()
    elif gestor == "dnf":
        dnf()
    elif gestor == "zypper":
        zypper()
    elif gestor == "apk":
        apk()
    elif gestor == "brew":
        brew()
    else:
        warning("Gestor no soportado")


info("Actualizacion en curso")
