for i in `seq 1 100`;
do
    tr -cd '[:alnum:]' < /dev/urandom | fold -w`shuf -i 500-3500 -n 1` | head -n1 > TC$i

done
