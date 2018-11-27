#! /bin/bash
# light gtk+shell theme

# gnome-shell theme
dconf write /org/gnome/shell/extensions/user-theme/name "'vimix-light-laptop-ruby'"

# mutter/gtk theme
gsettings set org.gnome.desktop.interface gtk-theme "vimix-light-laptop-ruby"

# cursor-theme
gsettings set org.gnome.desktop.interface cursor-theme "DMZ-Black"

# gnome-terminal profile
#gsettings set org.gnome.Terminal.ProfilesList default '541f30c9-1ead-4d3e-9643-2af0beb8e6d5'

# Wallpaper
gsettings set org.gnome.desktop.background picture-uri ~/Téléchargements/ricing/jour.png

# gedit theme
gsettings set org.gnome.gedit.preferences.editor scheme 'classic'
