packeges = {
    "Hyprland": {
        "packages": ["hyprland"],
        "config": {"source": "config/hyprland", "path": "~/.config", "backup": "True"},
        "preinstall": "packages/preinstall.py",
        "postinstall": "packages/hyprland/postinstall.py",
    }
}
