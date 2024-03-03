xset -b

picom &

unclutter --timeout 3 --jitter 10  --ignore-scrolling --start-hidden --fork

xrandr --output eDP1 --mode 1920x1080 --rate 60

xwallpaper --no-randr --center ~/Pictures/Wallpapers/plane-sand.jpg

# nm-applet &

qtile start

