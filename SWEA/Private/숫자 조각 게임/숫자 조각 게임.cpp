#include <cstring>
#include <queue>
#include <map>
#include <utility>

using namespace std;

#define MAX_ROW 40
#define MAX_COL 30

struct Result{
    int row;
    int col;

    bool operator<(const Result& other) {
        if (row < other.row) return true;
        if (row == other.row) return col < other.col;
        return false; 
    }
};

int row, col;
int origin[MAX_ROW][MAX_COL];
int chk[MAX_ROW][MAX_COL];
map<int, vector<Result>> hash_table[5];
const vector<pair<int, int>> nxt[5] = {
    {{0, 1}},
    {{0, 1}, {0, 1}},
    {{1, 0}, {1, 0}},
    {{0, 1}, {1, 0}, {0, 1}},
    {{1, 0}, {0, 1}, {0, 1}, {1, 0}}
};

int calc_type(int tile[3][3]) {
    if (tile[1][0] == 0) {
        if (tile[0][2] == 0) {
            if (tile[1][1] == 0) return 0;
            else return 3;
        } else {
            return 1;
        }
    } else {
        if (tile[2][2] == 0) return 2;
        else return 4;
    }
}

int hash_tile(int tile[3][3]) {
    int tile_type = calc_type(tile);
    int h = 0, x = 0, y = 0;
    for (auto n : nxt[tile_type]) {
        h <<= 4;
        h += (tile[x+n.first][y+n.second] - tile[x][y] + 5);
        x += n.first;
        y += n.second;
    }
    return h;
}

void hash_field() {
    for (int type=0; type<5; ++type) {
        for (int i=0; i<row; ++i) {
            for (int j=0; j<col; ++j) {
                int h = 0, x = i, y = j;
                bool impossible = false;
                for (auto n : nxt[type]) {
                    h <<= 4;
                    if (x+n.first >= row || y+n.second >= col) {
                        impossible = true;
                        break;
                    }
                    h += (origin[x+n.first][y+n.second] - origin[x][y] + 5);
                    x += n.first;
                    y += n.second;
                }
                if (impossible) continue;
                hash_table[type][h].push_back({i, j});
                for (int k=hash_table[type][h].size()-1; k>0; --k) {
                    if (hash_table[type][h][k] < hash_table[type][h][k-1]) 
                        swap(hash_table[type][h][k], hash_table[type][h][k-1]);
                }
            }
        }
    }
}

bool check(int type, int x, int y) {
    if (chk[x][y] == 1) return false;
    for (auto n : nxt[type]) {
        x += n.first, y += n.second;
        if (chk[x][y] == 1) return false;
    }
    return true;
}

void mark(int type, int x, int y) {
    chk[x][y] = 1;
    for (auto n : nxt[type]) {
        x += n.first, y += n.second;
        chk[x][y] = 1;
    }
}

void init(int mRows, int mCols, int mCells[MAX_ROW][MAX_COL]) {
    memcpy(origin, mCells, sizeof(origin));
    row = mRows, col = mCols;
    memset(chk, 0, sizeof(chk));
    for (int i=0; i<5; ++i) {
        hash_table[i].clear();
    }
    hash_field();
}

Result putPuzzle(int mPuzzle[3][3]) {
    Result ret = {-1, -1};

    int tile_type = calc_type(mPuzzle);
    int h = hash_tile(mPuzzle);

    for (auto xy : hash_table[tile_type][h]) {
        if (check(tile_type, xy.row, xy.col)) {
            mark(tile_type, xy.row, xy.col);
            return xy;
        }
    }
    return ret;
}

void clearPuzzles() {
    memset(chk, 0, sizeof(chk));
    return;
}
