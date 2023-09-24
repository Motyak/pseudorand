select sample and mean sorted by diff desc
```bash
./s.py \
    | awk NF \
    | sed -e '/i\tavg\tdiff/d' -e '/^=.*/d' -e 's/\t/ /g' \
    | sort -nk3 \
    | awk '{print "sample="$1 "\tmean="$2;}'
```
