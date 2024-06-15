echo "> Setting up pipenv..."
pipenv sync
echo "> Configuring privileges..."
chmod +x palermo-grab.sh
chmod +x update.sh

echo "> Done. Goodbye!"