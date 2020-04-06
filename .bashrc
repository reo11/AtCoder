function cpp(){
    basename=$1
    dirname=$(pwd)
    g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -I/opt/boost/gcc/include -L/opt/boost/gcc/lib -o ${dirname}/a.out ${dirname}/${basename}
    ${dirname}/a.out
}

function python(){
    basename=$1
    dirname=$(pwd)
    python3.8 ${dirname}/${basename}
}

function pypy(){
    basename=$1
    dirname=$(pwd)
    pypy3 ${dirname}/${basename}
}



