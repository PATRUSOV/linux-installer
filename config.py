from structs import Package
from pathlib import Path


class Hyprland(Package):
    packages = ["hyprland"]

    config.source = Path("configs/Hyprland")

    config.path = Path("~/.config")


print(Hyprland.config)
