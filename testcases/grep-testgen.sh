for i in `seq 1 100`; 
do
    sed "${i}q;d" /scratch/testsubjects/grepsrc/testsArgs.txt | xargs > TC$i
done
