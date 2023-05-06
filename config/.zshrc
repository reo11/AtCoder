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

function rust(){
    basename=$1
    dirname=$(pwd)
    rustc ${dirname}/${basename} -o ${dirname}/${basename}.out
    ${dirname}/${basename}.out
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
    number=$(echo $(oj t -c "pypy3 ${problem_name}.py") | grep -c "FAILURE")
    # 4047: PyPy3
    if [ $number -eq 0 ]; then
        oj s -l 4047 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.py
    else
        echo "Wrong Answer"
        oj t -c "pypy3 ${problem_name}.py"
    fi
}

function submit_python(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    # rm -f root/.cache/online-judge-tools/download-history.jsonl
    dl $problem_name
    number=$(echo $(oj t -c "python3.8 ${problem_name}.py") | grep -c "FAILURE")
    # 4047: PyPy3
    if [ $number -eq 0 ]; then
        oj s -l 4006 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.py
    else
        echo "Wrong Answer"
        oj t -c "python3.8 ${problem_name}.py"
    fi
}

# バグってる
function submit_cpp(){
    problem_name=$1
    contest_name=$(basename `pwd`)
    # rm -f root/.cache/online-judge-tools/download-history.jsonl
    dirname=$(pwd)
    dl $problem_name
    g++ -std=gnu++17 -Wall -Wextra -O2 -DONLINE_JUDGE -I/opt/boost/gcc/include -L/opt/boost/gcc/lib -o ${dirname}/a.out ${dirname}/${problem_name}.cpp
    number=$(echo $(oj t) | grep -c "FAILURE")
    # 4047: PyPy3
    if [ $number -eq 0 ]; then
        oj s -l 4003 https://atcoder.jp/contests/${contest_name}/tasks/${contest_name}_${problem_name} ${problem_name}.cpp
    else
        echo "Wrong Answer"
        oj t
    fi
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

# rust用エイリアス集
function rust_atcoder(){
    cargo compete init atcoder
}

function rust_c(){
    cargo compete n $1
    for f in $1/src/bin/*.rs; do
        cp /work/algorithm_libraries/rust/rust_template.rs $f
    done
}

function rust_s(){
    cargo compete s $1
}

function rust_t(){
    cargo compete t $1
}
