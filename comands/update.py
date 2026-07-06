from comands.utils import warning, info, progress_bar
from comands.distro import paquetes
import subprocess
import shutil


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
    progress_bar(comands)


def pacman():
    comands = [
        "sudo rm -f /var/cache/pacman/pkg/download-*",
        "sudo rm -f /var/lib/pacman/db.lck",
        "pacman -Syu --noconfirm --noprogressbar",
        "pacman -Sc --noconfirm --noprogressbar",
    ]
    progress_bar(comands)

    orfanos = subprocess.run(
        ["pacman", "-Qtdq"], capture_output=True, text=True
    ).stdout.strip()
    if orfanos:
        progress_bar(["pacman -Rns --noconfirm $(pacman -Qtdq) --noprogressbar"])


def dnf():
    comands = [
        "dnf check-update",
        "dnf upgrade -y",
        "dnf autoremove -y",
    ]
    progress_bar(comands)


def zypper():
    comands = [
        "zypper refresh --non-interactive",
        "zypper update -y",
        "zypper clean --non-interactive",
    ]
    progress_bar(comands)


def apk():
    comands = [
        "apk update --no-interactive",
        "apk upgrade --no-interactive",
        "apk cache clean",
    ]
    progress_bar(comands)


def brew():
    comands = [
        "brew update",
        "brew upgrade",
        "brew cleanup",
    ]
    progress_bar(comands)


def update():
    gestor = detectar()
    paquetes(gestor)
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
