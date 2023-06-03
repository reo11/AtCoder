#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<long long, long long> LP;
#define INF 999999999
#define MOD 1000000007
#define EPS 0.000001
#define MAX_N 61
#define out cout
#define in cin

#define REP(i, n) for (ll i = 0, i##_len = (n); i < i##_len; ++i)
#define REP_AB(i, a, b) for (ll i = ll(a); i < ll(b); ++i)

map<string, ll> SIDE_SIMBOLS = {
    {"|", 0},
    {"-", 1},
    {"/", 2},
    {"\\", 3}
};

vector<vector<ll>> DIRECTIONS = {
    {-1, -1},
    {-1, 0},
    {-1, 1},
    {0, -1},
    {0, 1},
    {1, -1},
    {1, 0},
    {1, 1}
};

struct Coordinate{
public:
    ll x;
    ll y;

    Coordinate(){
        x = 0;
        y = 0;
    }

    Coordinate(ll x_in, ll y_in){
        x = x_in;
        y = y_in;
    }
};

class Square{
public:
    Coordinate coordinates[4];

    Square(){
        Coordinate new_c(0, 0);
        coordinates[0] = new_c;
        coordinates[1] = new_c;
        coordinates[2] = new_c;
        coordinates[3] = new_c;
    }

    Square(Coordinate c1, Coordinate c2, Coordinate c3, Coordinate c4){
        coordinates[0] = c1;
        coordinates[1] = c2;
        coordinates[2] = c3;
        coordinates[3] = c4;
    }

    float get_size(){
        if (abs(coordinates[0].x - coordinates[1].x) == 0 || abs(coordinates[0].y - coordinates[1].y) == 0){
            // 縦か横
            ll s1 = abs(coordinates[0].x - coordinates[1].x) + abs(coordinates[0].y - coordinates[1].y);
            ll s2 = abs(coordinates[1].x - coordinates[2].x) + abs(coordinates[1].y - coordinates[2].y);
            return 2 * s1 + 2 * s2;
        } else {
            // 斜め
            ll s1 = max(abs(coordinates[0].x - coordinates[1].x), abs(coordinates[0].y - coordinates[1].y));
            ll s2 = max(abs(coordinates[1].x - coordinates[2].x), abs(coordinates[1].y - coordinates[2].y));
            return 2 * s1 + 2 * s2;
        }
    }

    ll get_type(){
        // type1 0: 横向き
        // type1 1: 斜め
        if (coordinates[0].x == coordinates[1].x || coordinates[0].y == coordinates[1].y){
            return 0;
        } else {
            return 1;
        }
    }

    Coordinate get_left_c(){
        // 横向きの場合は左上、斜めの場合は左の座標を返す
        Coordinate c = coordinates[0];
        if (get_type() == 0){
            REP(i, 3){
                if (c.x > coordinates[i+1].x){
                    c = coordinates[i+1];
                } else if (c.x == coordinates[i+1].x){
                    if (c.y < coordinates[i+1].y){
                        c = coordinates[i+1];
                    }
                }
            }
        } else {
            REP(i, 3){
                if (c.x > coordinates[i+1].x){
                    c = coordinates[i+1];
                }
            }
        }
        return c;
    }

    void display_square(){
        REP(j, 4){
            out << coordinates[j].x << " " << coordinates[j].y;
            if (j < 3){
                out << " ";
            } else {
                out << endl;
            }
        }
    }
};

class CoordinateController{
public:
    ll size; // 座標系のサイズ
    ll init_coordinate_size; // 初期座標数

    bool coordinates_exsits[MAX_N][MAX_N] = {false};
    bool sides_exsits[MAX_N][MAX_N][4] = {false};
    vector<Coordinate> coordinates_list;
    vector<Square> answers;

    CoordinateController(ll N, ll M){
        size = N;
        init_coordinate_size = M;
    }

    // 座標をソート、x, y
    static bool compare_coordinate(Coordinate c1, Coordinate c2) {
        if (c1.x != c2.x) {
            return c1.x < c2.x;
        } else  {
            return c1.y < c2.y;
        }
    }

    vector<Coordinate> sort_coordinates(vector<Coordinate> coordinates){
        sort(coordinates.begin(), coordinates.end(), compare_coordinate);
        return coordinates;
    }

    // 直交or45度
    bool is_parralell(Coordinate c1, Coordinate c2){
        return (c1.x - c2.x) == 0 || (c1.y - c2.y) == 0;
    }

    bool is_forty_five(Coordinate c1, Coordinate c2){
        return abs(c1.x - c2.x) == abs(c1.y - c2.y);
    }

    bool not_same(Coordinate c1, Coordinate c2){
        return !(c1.x == c2.x && c1.y == c2.y);
    }

    bool is_valid_angle(Coordinate c1, Coordinate c2){
        return not_same(c1, c2) && (is_parralell(c1, c2) || is_forty_five(c1, c2));
    }

    // 最小の辺
    bool is_uni_side(Coordinate c1, Coordinate c2){
        float distance = sqrt(pow(c1.x - c2.x, 2) + pow(c1.y - c2.y, 2));
        return (1.0 - EPS <= distance) && (distance <= sqrt(2) + EPS);
    }

    // 2つの座標間の座標列挙
    vector<Coordinate> all_coordinate_included(Coordinate c1, Coordinate c2){
        vector<Coordinate> all_coordinates = {c1, c2};
        vector<Coordinate> sc = sort_coordinates(all_coordinates);
        vector<Coordinate> coordinates = {};
        ll x = sc[0].x;
        ll y = sc[0].y;
        if (sc[0].x == sc[1].x){
            while(y <= sc[1].y){
                Coordinate new_c(x, y);
                coordinates.push_back(new_c);
                y += 1;
            }
        } else if (sc[0].y == sc[1].y){
            while(x <= sc[1].x){
                Coordinate new_c(x, y);
                coordinates.push_back(new_c);
                x += 1;
            }
        } else if ((sc[1].x - sc[0].x) == (sc[1].y - sc[0].y)){
            while(x <= sc[1].x && y <= sc[1].y){
                Coordinate new_c(x, y);
                coordinates.push_back(new_c);
                x += 1;
                y += 1;
            }
        } else {
            while(x <= sc[1].x && y >= sc[1].y){
                Coordinate new_c(x, y);
                coordinates.push_back(new_c);
                x += 1;
                y -= 1;
            }
        }
        return coordinates;
    }

    bool is_valid_coordinate(Coordinate c){
        return !coordinates_exsits[c.y][c.x];
    }

    // 2座標間に辺が既に存在するか
    bool uni_side_already_exist(Coordinate c1, Coordinate c2){
        assert (is_valid_angle(c1, c2));
        assert (is_uni_side(c1, c2));

        vector<Coordinate> v = {c1, c2};
        vector<Coordinate> sc = sort_coordinates(v);
        if (sc[0].x == sc[1].x) {
            return sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["|"]];
        } else if (sc[0].y == sc[1].y) {
            return sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["-"]];
        } else if ((sc[1].x - sc[0].x) == (sc[1].y - sc[0].y)) {
            return sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["/"]];
        } else {
            return sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["\\"]];
        }
    }

    // 有効な辺か
    bool is_valid_sides(Coordinate c1, Coordinate c2){
        bool is_valid = true;
        vector<Coordinate> coordinates = all_coordinate_included(c1, c2);
        REP(i, coordinates.size() - 1){
            is_valid &= !uni_side_already_exist(coordinates[i], coordinates[i+1]);
            if (!is_valid) return false;
        }
        return is_valid;
    }

    bool is_valid_square_sides(Square s){
        bool is_valid = true;
        REP(i, 4){
            is_valid &= is_valid_sides(s.coordinates[i], s.coordinates[(i + 1) % 4]);
            if (!is_valid) return false;
        }
        return is_valid;
    }

    // 有効な座標か
    bool is_valid_square_coordinates(Square s){
        bool is_valid = true;
        REP(i, 4){
            vector<Coordinate> coordinates = all_coordinate_included(s.coordinates[i], s.coordinates[(i + 1) % 4]);
            REP(j, coordinates.size() - 1){
                if (j == 0) continue;
                is_valid &= !coordinates_exsits[coordinates[j].y][coordinates[j].x];
                if (!is_valid) return false;
            }
            if (!is_valid) return false;
        }
        return is_valid;
    }

    // 座標を追加
    void add_coordinate(Coordinate c){
        assert (!coordinates_exsits[c.y][c.x]);
        coordinates_exsits[c.y][c.x] = true;
        coordinates_list.push_back(c);
    }

    // 最後に追加した座標を削除
    void delete_last_coordinate(Coordinate c){
        assert (coordinates_exsits[c.y][c.x]);
        Coordinate last_coordinate = coordinates_list.back();
        assert (last_coordinate.x == c.x && last_coordinate.y == c.y);
        coordinates_exsits[c.y][c.x] = false;
        coordinates_list.pop_back();
    }

    // 辺を追加(隣接する2座標)
    void add_side(Coordinate c1, Coordinate c2){
        assert (is_valid_angle(c1, c2));
        assert (is_uni_side(c1, c2));

        vector<Coordinate> v = {c1, c2};
        vector<Coordinate> sc = sort_coordinates(v);

        if (sc[0].x == sc[1].x) {
            assert (!sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["|"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["|"]] = true;
        } else if (sc[0].y == sc[1].y) {
            assert (!sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["-"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["-"]] = true;
        } else if ((sc[1].x - sc[0].x) == (sc[1].y - sc[0].y)) {
            assert (!sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["/"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["/"]] = true;
        } else {
            assert (!sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["\\"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["\\"]] = true;
        }
    }

    // 辺を削除
    void delete_side(Coordinate c1, Coordinate c2){
        assert (is_valid_angle(c1, c2));
        assert (is_uni_side(c1, c2));

        vector<Coordinate> v = {c1, c2};
        vector<Coordinate> sc = sort_coordinates(v);

        if (sc[0].x == sc[1].x) {
            assert (sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["|"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["|"]] = false;
        } else if (sc[0].y == sc[1].y) {
            assert (sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["-"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["-"]] = false;
        } else if ((sc[1].x - sc[0].x) == (sc[1].y - sc[0].y)) {
            assert (sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["/"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["/"]] = false;
        } else {
            assert (sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["\\"]]);
            sides_exsits[sc[0].y][sc[0].x][SIDE_SIMBOLS["\\"]] = false;
        }
    }

    void add_sides(Coordinate c1, Coordinate c2){
        vector<Coordinate> coordinates = all_coordinate_included(c1, c2);
        REP(i, coordinates.size() - 1){
            add_side(coordinates[i], coordinates[i+1]);
        }
    }

    void delete_sides(Coordinate c1, Coordinate c2){
        vector<Coordinate> coordinates = all_coordinate_included(c1, c2);
        REP(i, coordinates.size() - 1){
            delete_side(coordinates[i], coordinates[i+1]);
        }
    }

    bool is_valid_square(Square s){
        bool is_valid = true;
        is_valid &= is_valid_square_coordinates(s);
        is_valid &= is_valid_square_sides(s);
        // 1点目が存在しない
        is_valid &= !coordinates_exsits[s.coordinates[0].y][s.coordinates[0].x];
        // それ以外は存在する
        REP(i, 3){
            is_valid &= coordinates_exsits[s.coordinates[i+1].y][s.coordinates[i+1].x];
        }
        return is_valid;
    }

    void add_square_sides(Square s){
        REP(i, 4){
            add_sides(s.coordinates[i], s.coordinates[(i + 1) % 4]);
        }
    }

    void add_square_coordinates(Square s){
        add_coordinate(s.coordinates[0]);
    }

    void add_square(Square s){
        assert (is_valid_square(s));

        add_square_sides(s);
        add_square_coordinates(s);
        add_answers(s);
    }

    ll calc_score(){
        float n = float(size), m = float(init_coordinate_size);
        float q_score = 0.0, s = 0.0, w = 0.0, center = (n - 1.0) / 2.0;
        REP(y, n){
            REP(x, n){
                w = pow(x - center, 2) + pow(y - center, 2) + 1.0;
                s += w;
                if (coordinates_exsits[y][x]){
                    q_score += w;
                }
            }
        }

        return ll(round(pow(10, 6) * (n * n / m) * (q_score / s)));
    }

    void add_answers(Square s){
        answers.push_back(s);
    }

    void display_answers(){
        out << answers.size() << endl;
        REP(i, answers.size()){
            Square s = answers[i];
            s.display_square();
        }
    }

    void set_initial_coordinates(vector<Coordinate> coordinates){
        REP(i, coordinates.size()){
            add_coordinate(coordinates[i]);
        }
    }

    bool in_valid_area(ll x){
        return (0 <= x) && (x < size);
    }

    // 直近で追加した四角形を消す
    void undo(){
        if (answers.size() == 0) return;

        Square last_square = answers.back();

        // coordinate
        Coordinate c = last_square.coordinates[0];
        delete_last_coordinate(c);

        // sides
        REP(i, 4){
            delete_sides(last_square.coordinates[i], last_square.coordinates[(i + 1) % 4]);
        }
        answers.pop_back();
    }

    // そこに点が出来た場合、それを使ってできる四角形の個数
    vector<Square> get_squares_from_new_square(Square s){
        if (is_valid_square(s)){
            add_square(s);
        } else {
            return {};
        }
        Coordinate c1 = s.coordinates[0];
        vector<Square> squares = {};
        REP(i, coordinates_list.size()){
            Coordinate c2 = coordinates_list[i];
            if (c1.x == c2.x && c1.y == c2.y) continue;
            if (!is_valid_angle(c1, c2)) continue;
            if (!is_valid_sides(c1, c2)) continue;

            ll length = max(abs(c2.x - c1.x), abs(c2.y - c1.y));
            // 単位ベクトルにする
            vector<ll> dxy = {(c2.x - c1.x) / length, (c2.y - c1.y) / length};
            vector<vector<ll>> normal_vectors = {
                {dxy[1], -dxy[0]},
                {-dxy[1], dxy[0]}
            };

            REP(k, normal_vectors.size()){
                // 単位法線ベクトル
                vector<ll> rdxy = normal_vectors[k];

                REP_AB(side_length, 1, size){
                    ll x3 = c2.x + rdxy[0] * side_length, y3 = c2.y + rdxy[1] * side_length;
                    ll x4 = c1.x + rdxy[0] * side_length, y4 = c1.y + rdxy[1] * side_length;
                    if (!(in_valid_area(x3) && in_valid_area(y3) && in_valid_area(x4) && in_valid_area(y4))){
                        // 範囲外なら打ち切り
                        break;
                    }

                    Coordinate c3 = {x3, y3};
                    Coordinate c4 = {x4, y4};

                    if (is_valid_coordinate(c3) && is_valid_coordinate(c4)) continue;
                    if (!is_valid_coordinate(c3) && !is_valid_coordinate(c4)) break;
                    if (is_valid_coordinate(c3)){
                        Square s = {c3, c2, c1, c4};
                        if (is_valid_square(s)){
                            squares.push_back(s);
                            break;
                        }
                    } else {
                        Square s = {c4, c3, c2, c1};
                        if (is_valid_square(s)){
                            squares.push_back(s);
                            break;
                        }
                    }
                }
            }
        }
        undo();
        return squares;
    }

    // 現在の状態から作成できる四角形の全列挙
    vector<Square> get_squares(){
        vector<Square> squares = {};
        REP(i, coordinates_list.size()){
            Coordinate c1 = coordinates_list[i];
            REP_AB(j, i + 1, coordinates_list.size()){
                Coordinate c2 = coordinates_list[j];
                if (c1.x == c2.x && c1.y == c2.y) continue;
                if (!is_valid_angle(c1, c2)) continue;
                if (!is_valid_sides(c1, c2)) continue;

                ll length = max(abs(c2.x - c1.x), abs(c2.y - c1.y));
                // 単位ベクトルにする
                vector<ll> dxy = {(c2.x - c1.x) / length, (c2.y - c1.y) / length};
                vector<vector<ll>> normal_vectors = {
                    {dxy[1], -dxy[0]},
                    {-dxy[1], dxy[0]}
                };

                REP(k, normal_vectors.size()){
                    // 単位法線ベクトル
                    vector<ll> rdxy = normal_vectors[k];

                    REP_AB(side_length, 1, size){
                        ll x3 = c2.x + rdxy[0] * side_length, y3 = c2.y + rdxy[1] * side_length;
                        ll x4 = c1.x + rdxy[0] * side_length, y4 = c1.y + rdxy[1] * side_length;
                        if (!(in_valid_area(x3) && in_valid_area(y3) && in_valid_area(x4) && in_valid_area(y4))){
                            // 範囲外なら打ち切り
                            break;
                        }

                        Coordinate c3 = {x3, y3};
                        Coordinate c4 = {x4, y4};

                        if (is_valid_coordinate(c3) && is_valid_coordinate(c4)) continue;
                        if (!is_valid_coordinate(c3) && !is_valid_coordinate(c4)) break;
                        if (is_valid_coordinate(c3)){
                            Square s = {c3, c2, c1, c4};
                            if (is_valid_square(s)){
                                squares.push_back(s);
                                break;
                            }
                        } else {
                            Square s = {c4, c3, c2, c1};
                            if (is_valid_square(s)){
                                squares.push_back(s);
                                break;
                            }
                        }
                    }
                }
            }
        }
        return squares;
    }

    ll get_score(){
        return get_squares().size() + coordinates_list.size();
    }

    vector<Coordinate> get_random_coordinates(){
        std::random_device get_rand;
        std::mt19937 get_rand_mt(get_rand());
        vector<Coordinate> shuffled_coordinates = {};
        REP(i, coordinates_list.size()){
            shuffled_coordinates.push_back(coordinates_list[i]);
        }

        shuffle(shuffled_coordinates.begin(), shuffled_coordinates.end(), get_rand_mt);
        return shuffled_coordinates;
    }

    bool generate_square(Coordinate c1, ll max_length){
        std::random_device get_rand;
        std::mt19937 get_rand_mt(get_rand());
        vector<ll> random_direction_numbers = {};
        queue<ll> que;
        REP(i, DIRECTIONS.size()){
            random_direction_numbers.push_back(i);
        }
        shuffle(random_direction_numbers.begin(), random_direction_numbers.end(), get_rand_mt);

        REP(i, random_direction_numbers.size()){
            que.push(random_direction_numbers[i]);
        }
        // que.push(random_direction_numbers[0]);
        // 近くから探す
        REP(i, max_length){
            if (i == 0) continue;
            if (que.empty()) break;

            ll num = que.front();
            que.pop();
            ll x = c1.x + DIRECTIONS[num][0] * i;
            ll y = c1.y + DIRECTIONS[num][1] * i;

            if (in_valid_area(x) && in_valid_area(y)){
                if (!coordinates_exsits[y][x]){
                    que.push(num);
                    continue;
                }
                Coordinate c2(x, y);
                if (!is_valid_sides(c1, c2)) {
                    // 辺がある場合、それ以上伸ばせないので打ち切り
                    continue;
                }
                // 長方形を探す
                // 2点が確定すると探索方向は2方向に減る
                vector<vector<ll>> dxy = {
                    {DIRECTIONS[num][1], -DIRECTIONS[num][0]},
                    {-DIRECTIONS[num][1], DIRECTIONS[num][0]}
                };
                vector<ll> rand_nums = {0, 1};
                queue<ll> next_que;
                shuffle(rand_nums.begin(), rand_nums.end(), get_rand_mt);
                REP(j, 2){
                    next_que.push(rand_nums[j]);
                }

                REP(j, max_length){
                    if (j == 0) continue;
                    if (next_que.empty()) break;
                    ll rand_num = next_que.front();
                    next_que.pop();

                    ll x1 = c1.x + dxy[rand_num][0] * j;
                    ll y1 = c1.y + dxy[rand_num][1] * j;
                    ll x2 = c2.x + dxy[rand_num][0] * j;
                    ll y2 = c2.y + dxy[rand_num][1] * j;
                    if (!(in_valid_area(x1) && in_valid_area(y1) && in_valid_area(x2) && in_valid_area(y2))){
                        // 範囲外なら打ち切り
                        continue;
                    }
                    if (coordinates_exsits[y1][x1] && coordinates_exsits[y2][x2]){
                        // どちらの座標も埋まってる場合打ち切り
                        continue;
                    }
                    if (!coordinates_exsits[y1][x1] && !coordinates_exsits[y2][x2]){
                        // どちらも埋まってない場合続行
                        que.push(rand_num);
                        continue;
                    }
                    if (coordinates_exsits[y1][x1]){
                        // 追加できそうだったら追加、ダメなら打ち切り
                        Coordinate c3(x2, y2);
                        Coordinate c4(x1, y1);
                        Square s(c3, c2, c1, c4);
                        if (is_valid_square(s)){
                            add_square(s);
                            return true;
                        }
                    } else {
                        Coordinate c3(x2, y2);
                        Coordinate c4(x1, y1);
                        Square s(c4, c3, c2, c1);
                        if (is_valid_square(s)){
                            add_square(s);
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    }
};


// 追加できる四角形を全列挙して、追加できる数が多い候補から探索をしていくダイクストラ + ある程度のランダム要素
// void solve_one(){

// }

bool operator< (const pair<ll, CoordinateController> p1, const pair<ll, CoordinateController> p2){
    return p1.first > p2.first;
}

bool operator> (const pair<ll, CoordinateController> p1, const pair<ll, CoordinateController> p2){
    return p1.first < p2.first;
}

bool operator< (const pair<ll, Square> p1, const pair<ll, Square> p2){
    return p1.first > p2.first;
}

bool operator> (const pair<ll, Square> p1, const pair<ll, Square> p2){
    return p1.first < p2.first;
}

ll get_square_score(Square square, ll n, ll m){
    float q_score = 0.0, s = 0.0, w = 0.0, center = (float(n) - 1.0) / 2.0;
    REP(y, n){
        REP(x, n){
            w = pow(x - center, 2) + pow(y - center, 2) + 1.0;
            s += w;
            if (square.coordinates[0].x == x && square.coordinates[0].y == y){
                q_score += w;
            }
        }
    }

    return ll(round(pow(10, 6) * (float(n) * float(n) / float(m)) * (q_score / s)));
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    REP(i, 50){
        std::ostringstream oss;
        oss << i;
        string file_name = oss.str();
        while(file_name.size() < 4){
            file_name = "0" + file_name;
        }
        file_name = file_name + ".txt";
        ifstream in("in/" + file_name);

        ll N, M, x, y;
        in >> N >> M;

        vector<Coordinate> initial_coordinates = {};

        REP(i, M) {
            in >> x >> y;
            Coordinate c(x, y);
            initial_coordinates.push_back(c);
        }

        out << N << endl;

        ifstream in("out/" + file_name);

        ll out_N;
        in >> out_N;
        vector<vector<Coordinate>> answer_coordinates = {};

        ll x1, x2, x3, x4;
        ll y1, y2, y3, y4;
        REP(i, out_N){
            in >> x1 >> y1 >> x2 >> y2 >> x3 >> y3 >> x4 >> y4;
            REP(i, 4){
                continue;
            }
        }
    }
    return 0;
}
