alias python="python3.8"
function cpp(){
    basename=$1
    dirname=$(pwd)
    g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -I/opt/boost/gcc/include -L/opt/boost/gcc/lib -o ${dirname}/a.out ${dirname}/${basename}.cpp
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

function login_atcoder(){
    oj login https://atcoder.jp/
}

function dl(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    rm -r test
    oj d https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name}
}

function submit_pypy(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    # rm -f root/.cache/online-judge-tools/download-history.jsonl
    dl $problem_name
    oj t -c "pypy3 ${problem_name}.py"
    # 4047: PyPy3
    oj s -l 4047 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.py
}

function submit_python(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    # rm -f root/.cache/online-judge-tools/download-history.jsonl
    dl $problem_name
    oj t -c "python3.8 ${problem_name}.py"
    # 4047: PyPy3
    oj s -l 4006 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.py
}

# バグってる
function submit_cpp(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    # rm -f root/.cache/online-judge-tools/download-history.jsonl
    dirname=$(pwd)
    g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -I/opt/boost/gcc/include -L/opt/boost/gcc/lib -o a.out ${problem_name}.cpp
    dl $problem_name
    oj t
    # 4047: PyPy3
    oj s -l 4003 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.cpp
}

# cppファイルの生成
function cpp_create_mod(){
    problem_name=$1
    dirname=$(pwd)
    cp /work/cpp_template/mod_template.cpp ${dirname}/${problem_name}.cpp
}

function cpp_create_short(){
    problem_name=$1
    dirname=$(pwd)
    cp /work/cpp_template/short_template.cpp ${dirname}/${problem_name}.cpp
}

