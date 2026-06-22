マップの行数 H と列数 W , 障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H が与えられます。
続けて現在の座標 sy , sx ,１マス移動する方角 m が与えられるので、移動が可能かどうかを判定してください。

移動が可能であるということは、以下の図の通り
「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
ということを意味します。

なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


allin = input().split()

h = int(allin[0])
w = int(allin[1])
sy = int(allin[2])
sx = int(allin[3])
m = allin[4]


grid = []
# grid.append(int(h))
# grid.append(int(w))

# print(m)

for i in range(h):
    string = input()
    # print(string)
    grid.append(string)


answer = "No"
# print(grid)

for r, row_content in enumerate(grid):          
    for c, column_content in enumerate(row_content):
        
        # whether sy, sx == grid(row, column) 
        if r == sy and c == sx:
            
            # check m 
            if m == 'E':
                next_c = c + 1  # COLUMN + 1
                # CHECK WHETHER OUT OF BOUNDARY
                if next_c < w:
                    if grid[r][next_c] != '#':
                        answer = "Yes"
                        
            elif m == 'W':
                next_c = c - 1  # COLUMN - 1
                if next_c >= 0:
                    if grid[r][next_c] != '#':
                        answer = "Yes"
                        
            elif m == 'N':
                next_r = r - 1  # NORTH ROW--
                if next_r >= 0:
                    if grid[next_r][c] != '#':
                        answer = "Yes"
                        
            elif m == 'S':
                next_r = r + 1  # SOUTH ROW++
                if next_r < h:
                    if grid[next_r][c] != '#':
                        answer = "Yes"

print(answer)