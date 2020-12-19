#include <iostream>
#include <fstream>
#include <cstring>

constexpr int sz = 24;
using namespace std;

ifstream f("input17.txt");

int sys[sz][sz][sz][sz];
int temp[sz][sz][sz][sz];


int lookup_neighbours(int w, int z, int y, int x)
{
    int s = 0;
    for (int i = max(0, w - 1); i <= min(w + 1, sz - 1); i++)
        for (int j = max(0, z - 1); j <= min(z + 1, sz - 1); j++)
            for (int k = max(0, y - 1); k <= min(y + 1, sz - 1); k++)
                for (int l = max(0, x - 1); l <= min(x + 1, sz - 1); l++)
                    if (sys[i][j][k][l])
                        if (i != w || j != z || k != y || l != x)
                            s++;
    return s;
}

int read_data() {
    int row = 0;
    int ofs;
    int l;
    while (!f.eof())
    {
        char line[10];
        f >> line;
        l = strlen(line);
        ofs = 0.5 * (sz - strlen(line));
        for (int i = 0; i < strlen(line); i++)
            if (line[i] == '#')
            {
                sys[ofs][ofs][ofs + row][ofs + i] = 1;
            }
            else if (line[i] == '.')
            {
                sys[ofs][ofs][ofs + row][ofs + i] = 0;
            }
        row++;
    }
    return l;
}

void copy_temp_to_sys() {
    for (int i = 0; i < sz; i++)
        for (int j = 0; j < sz; j++)
            for (int k = 0; k < sz; k++)
                for (int l = 0; l < sz; l++)
                    sys[i][j][k][l] = temp[i][j][k][l];
}

int count_active() {
    int s = 0;
    for (int i = 0; i < sz; i++)
        for (int j = 0; j < sz; j++)
            for (int k = 0; k < sz; k++)
                for (int l = 0; l < sz; l++)
                    if (sys[i][j][k][l])
                        s++;
    return s;
}

int main()
{
    int x, y, z, w, loop = 0;
    int len = read_data();
    int ofs = 0.5 * (sz - len);
    while (loop < 6)
    {
        for(int i = ofs - loop - 1; i <= ofs + loop + 1; i++)
            for (int j = ofs - loop - 1; j <= ofs + loop + 1; j++)
                for (int k = ofs - loop - 1; k <= ofs + len + loop + 1; k++)
                    for (int l = ofs - loop - 1; l <= ofs + len + loop + 1; l++) {
                        int nr = lookup_neighbours(i, j, k, l);
                        if (sys[i][j][k][l]) {
                            if (nr == 2 || nr == 3)
                                temp[i][j][k][l] = 1;
                            else
                                temp[i][j][k][l] = 0;
                        }
                        else {
                            if (nr == 3)
                                temp[i][j][k][l] = 1;
                            else
                                temp[i][j][k][l] = 0;
                        }
                    }
        copy_temp_to_sys();
        loop++;
    }
    cout << count_active();
}

