if [ $# -eq 0 ]
  then
    echo "> URL missing! Usage: $0 'URL'"
    exit 1
fi

pipenv run python palermo-grab.py "$1"