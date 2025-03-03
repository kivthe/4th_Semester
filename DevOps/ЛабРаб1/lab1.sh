show_help() {
    echo "usage:"
    echo "[options] <directory> or <filename>"
    echo "-p <template>  template deletion (*.txt for instance)"
    echo "-h show this message"
}

if [ "$#" -lt 1 ]; then
  show_help
  exit 1
elif [ "$#" -gt 3 ]; then
  echo "error: up to 3 arguments expected, $# given"
  exit 0
fi

file=""
dir=""
pattern=""

while getopts ":hp:" opt; do
  case ${opt} in
    h )
      show_help
      exit 0
      ;;
    p )
      pattern=$OPTARG
      ;;
    \? )
      echo "error: incorrect flag: $OPTARG" 1>&2
      show_help
      exit 1
      ;;
    : )
      echo "error: flag -$OPTARG demands an argument" 1>&2
      show_help
      exit 1
      ;;
  esac
done

shift $((OPTIND -1))

if [ -z "$pattern" ] && [ "$#" -ne 2 ]; then
    echo "error: either filename or -p flag with pattern expected" 1>&2
    show_help
    exit 0
fi

if [ -n "$pattern" ]; then
  dir=$1
else
if [ "$#" -gt 2 ]; then
  echo "error: no more than 2 arguments allowed on single file deletion"
  exit 0
fi
  file=$2
  dir=$1
fi

if [ ! -n "$pattern" ]; then
if [ ! -e $dir/$file ]; then
  echo "error: file '$dir/$file' does not exist"
  exit 0
elif [ ! -f $dir/$file ]; then
  echo "error: '$dir/$file' is not a file"
  exit 0
fi
fi

if [ -n "$pattern" ]; then
    echo "deleting according to pattern '$pattern' in directory '$dir'"
    find "$dir" -type f -name "$pattern" -exec rm -f {} +
else
    # Удаление по имени
    echo "deleting file '$file' in directory '$dir'"
    rm -f "$dir/$file"
fi