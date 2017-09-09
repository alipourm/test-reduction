
function download {
    sut=$1
    mkdir $sut
    scp maalipou@cusco.hpcc.uh.edu:/project/alipour/test-reduction-data/testcases/$sut/*.log $sut    
    }

mkdir data
cd data
download yaffs
download js
download grep
