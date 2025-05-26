packages = {
    "Hyprland": {
        "packages": ["hyprland"],
        "config": {
            "source": "config/hyprland",
            "path": "~/.config",
            "backup": "True",
        },  # TODO: Добавить поддержку путей типа ~/
        "preinstall": "packages/preinstall.py",
        "postinstall": "packages/hyprland/postinstall.py",
    }
}
