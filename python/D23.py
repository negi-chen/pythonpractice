1 マスの陣取り

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

start_y, start_x = -1, -1
for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            start_y, start_x = y, x
            break

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(4):
    ny = start_y + dy[i]
    nx = start_x + dx[i]
    
    if 0 <= ny < h and 0 <= nx < w:
        grid[ny][nx] = '*'

for row in grid:
    print("".join(row))


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }

        int startY = -1, startX = -1;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '*') {
                    startY = y;
                    startX = x;
                }
            }
        }
        

        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};

        for (int i = 0; i < 4; i++) {
            int ny = startY + dy[i];
            int nx = startX + dx[i];
            if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                grid[ny][nx] = '*';
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        
        sc.close();
    }
}


#ans from paiza
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

flag_out = False
for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            if y > 0:
                s[y - 1][x] = "*"
            if y < H - 1:
                s[y + 1][x] = "*"
            if x > 0:
                s[y][x - 1] = "*"
            if x < W - 1:
                s[y][x + 1] = "*"
            flag_out = True
            break
    if flag_out:
        break

for y in range(H):
    print("".join(s[y]))


2. 1マスの陣取り2 

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

start_y, start_x = -1, -1
for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            start_y, start_x = y, x
            break

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(4):
    ny = start_y + dy[i]
    nx = start_x + dx[i]
    if 0 <= ny < h and 0 <= nx < w:
        if grid[ny][nx] == '.':
            grid[ny][nx] = '*'

for row in grid:
    print("".join(row))



import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        int startY = -1, startX = -1;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '*') {
                    startY = y;
                    startX = x;
                }
            }
        }
        
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        for (int i = 0; i < 4; i++) {
            int ny = startY + dy[i];
            int nx = startX + dx[i];
            
            if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                if (grid[ny][nx] == '.') {
                    grid[ny][nx] = '*';
                }
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        
        sc.close();
    }
}


[陣取りの結末]

from collections import deque

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

queue = deque()

for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            queue.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    cy, cx = queue.popleft()
    
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == '.':
                grid[ny][nx] = '*'
                queue.append((ny, nx))

for row in grid:
    print("".join(row))


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        Queue<int[]> queue = new LinkedList<>();
        
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '*') {
                    queue.offer(new int[]{y, x});
                }
            }
        }
        
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cy = current[0];
            int cx = current[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                
                if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                    if (grid[ny][nx] == '.') {
                        grid[ny][nx] = '*';
                        queue.offer(new int[]{ny, nx});
                    }
                }
            }
        }
        
        for (int i = 0; i < h; i++) {
            System.out.println(new String(grid[i]));
        }
        
        sc.close();
    }
}



[陣取りの手間]
 
from collections import deque

h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

dist = [[-1] * w for _ in range(h)]
queue = deque()

for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            dist[y][x] = 0
            queue.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    cy, cx = queue.popleft()
    
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[cy][cx] + 1
                queue.append((ny, nx))

for y in range(h):
    row_output = []
    for x in range(w):
        if grid[y][x] == '#':
            row_output.append('#')
        else:
            row_output.append(str(dist[y][x]))
    print("".join(row_output))


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        int[][] dist = new int[h][w];
        for (int i = 0; i < h; i++) {
            Arrays.fill(dist[i], -1);
        }
        
        Queue<int[]> queue = new LinkedList<>();
        
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '*') {
                    dist[y][x] = 0;
                    queue.offer(new int[]{y, x});
                }
            }
        }
        
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cy = current[0];
            int cx = current[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                
                if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                    if (grid[ny][nx] == '.' && dist[ny][nx] == -1) {
                        dist[ny][nx] = dist[cy][cx] + 1;
                        queue.offer(new int[]{ny, nx});
                    }
                }
            }
        }
        
        for (int y = 0; y < h; y++) {
            StringBuilder sb = new StringBuilder();
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '#') {
                    sb.append('#');
                } else {
                    sb.append(dist[y][x]);
                }
            }
            System.out.println(sb.toString());
        }
        
        sc.close();
    }
}


#ans from  paiza
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
my_p = []

for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            s[y][x] = 0
            my_p.append([y, x, 1])

while my_p:
    [y, x, n] = my_p[0]
    my_p.pop(0)

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = n
        my_p.append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = n
        my_p.append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = n
        my_p.append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = n
        my_p.append([y, x + 1, n + 1])

for y in range(int(H)):
    for x in range(int(W)):
        print(s[y][x], end="")
    print()


[ 陣取りのターン数 ]


from collections import deque

h, w, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

target_lengths = set()
for _ in range(n):
    target_lengths.add(int(input()))

dist = [[-1] * w for _ in range(h)]
queue = deque()

for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            dist[y][x] = 0
            queue.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while queue:
    cy, cx = queue.popleft()
    
    for i in range(4):
        ny = cy + dy[i]
        nx = cx + dx[i]
        
        if 0 <= ny < h and 0 <= nx < w:
            if grid[ny][nx] == '.' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[cy][cx] + 1
                queue.append((ny, nx))

for y in range(h):
    row_output = []
    for x in range(w):
        if grid[y][x] == '#':
            row_output.append('#')
        elif dist[y][x] != -1:
            if dist[y][x] in target_lengths:
                row_output.append('?')
            else:
                row_output.append('*')
        else:
            row_output.append('.')
    print("".join(row_output))



# java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        int n = sc.nextInt();
        
        char[][] grid = new char[h][w];
        for (int i = 0; i < h; i++) {
            grid[i] = sc.next().toCharArray();
        }
        
        HashSet<Integer> targetLengths = new HashSet<>();
        for (int i = 0; i < n; i++) {
            targetLengths.add(sc.nextInt());
        }
        
        int[][] dist = new int[h][w];
        for (int i = 0; i < h; i++) {
            Arrays.fill(dist[i], -1);
        }
        
        Queue<int[]> queue = new LinkedList<>();
        
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '*') {
                    dist[y][x] = 0;
                    queue.offer(new int[]{y, x});
                }
            }
        }
        
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cy = current[0];
            int cx = current[1];
            
            for (int i = 0; i < 4; i++) {
                int ny = cy + dy[i];
                int nx = cx + dx[i];
                
                if (ny >= 0 && ny < h && nx >= 0 && nx < w) {
                    if (grid[ny][nx] == '.' && dist[ny][nx] == -1) {
                        dist[ny][nx] = dist[cy][cx] + 1;
                        queue.offer(new int[]{ny, nx});
                    }
                }
            }
        }
        
        for (int y = 0; y < h; y++) {
            StringBuilder sb = new StringBuilder();
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == '#') {
                    sb.append('#');
                } else if (dist[y][x] != -1) {
                    if (targetLengths.contains(dist[y][x])) {
                        sb.append('?');
                    } else {
                        sb.append('*');
                    }
                } else {
                    sb.append('.');
                }
            }
            System.out.println(sb.toString());
        }
        
        sc.close();
    }
}



A さんと B さんは次の操作を交互に繰り返すことで陣取りゲームをしようと考えました。 2 人の操作によって盤面が変化しなくなったらゲームを終了します。

・ 現在の陣地から上下左右に 1 マス移動することで到達できる、まだ誰の陣地でもない全てのマスを新たに陣地にする。ただし、障害物( '#' )のマスは陣地にできない。
・ 新たに陣地にできるマスが無い場合、何もしない。

盤面の情報と、先攻のプレイヤーの名前が与えられます。
盤面では、はじめに A さんのいるマスが 'A' , B さんのいるマスが 'B' で表されています。
ゲーム終了時に A さん、B さん、それぞれの陣地のマス数と勝った人の名前を出力してください。

なお、引き分けにはならないことが保証されています。

例として、ゲームが次のような状態でスタートした場合、 Aさんが先攻のときは次のような結果になるので、

from collections import deque

h, w = map(int, input().split())
first_player = input().strip()
grid = [list(input().strip()) for _ in range(h)]

queue_A = deque()
queue_B = deque()

for y in range(h):
    for x in range(w):
        if grid[y][x] == 'A':
            queue_A.append((y, x))
        elif grid[y][x] == 'B':
            queue_B.append((y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

current_turn = first_player

while queue_A or queue_B:
    has_moved = False
    
    if current_turn == 'A':
        if queue_A:
            has_moved = True
            size = len(queue_A)
            for _ in range(size):
                cy, cx = queue_A.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '.':
                        grid[ny][nx] = 'A'
                        queue_A.append((ny, nx))
        current_turn = 'B'
    else:
        if queue_B:
            has_moved = True
            size = len(queue_B)
            for _ in range(size):
                cy, cx = queue_B.popleft()
                for i in range(4):
                    ny, nx = cy + dy[i], cx + dx[i]
                    if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '.':
                        grid[ny][nx] = 'B'
                        queue_B.append((ny, nx))
        current_turn = 'A'
        
    if not has_moved and not queue_A and not queue_B:
        break

count_A = sum(row.count('A') for row in grid)
count_B = sum(row.count('B') for row in grid)

winner = 'A' if count_A > count_B else 'B'

print(count_A, count_B)
print(winner)

#java

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int h = sc.nextInt();
        int w = sc.nextInt();
        String firstPlayer = sc.next();
        
        char[][] grid = new char[h][w];
        Queue<int[]> queueA = new LinkedList<>();
        Queue<int[]> queueB = new LinkedList<>();
        
        for (int y = 0; y < h; y++) {
            grid[y] = sc.next().toCharArray();
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == 'A') {
                    queueA.offer(new int[]{y, x});
                } else if (grid[y][x] == 'B') {
                    queueB.offer(new int[]{y, x});
                }
            }
        }
        
        int[] dy = {-1, 1, 0, 0};
        int[] dx = {0, 0, -1, 1};
        
        String currentTurn = firstPlayer;
        
        while (!queueA.isEmpty() || !queueB.isEmpty()) {
            boolean hasMoved = false;
            
            if (currentTurn.equals("A")) {
                if (!queueA.isEmpty()) {
                    hasMoved = true;
                    int size = queueA.size();
                    for (int i = 0; i < size; i++) {
                        int[] cur = queueA.poll();
                        for (int d = 0; d < 4; d++) {
                            int ny = cur[0] + dy[d];
                            int nx = cur[1] + dx[d];
                            if (ny >= 0 && ny < h && nx >= 0 && nx < w && grid[ny][nx] == '.') {
                                grid[ny][nx] = 'A';
                                queueA.offer(new int[]{ny, nx});
                            }
                        }
                    }
                }
                currentTurn = "B";
            } else {
                if (!queueB.isEmpty()) {
                    hasMoved = true;
                    int size = queueB.size();
                    for (int i = 0; i < size; i++) {
                        int[] cur = queueB.poll();
                        for (int d = 0; d < 4; d++) {
                            int ny = cur[0] + dy[d];
                            int nx = cur[1] + dx[d];
                            if (ny >= 0 && ny < h && nx >= 0 && nx < w && grid[ny][nx] == '.') {
                                grid[ny][nx] = 'B';
                                queueB.offer(new int[]{ny, nx});
                            }
                        }
                    }
                }
                currentTurn = "A";
            }
            
            if (!hasMoved && queueA.isEmpty() && queueB.isEmpty()) {
                break;
            }
        }
        
        int countA = 0;
        int countB = 0;
        for (int y = 0; y < h; y++) {
            for (int x = 0; x < w; x++) {
                if (grid[y][x] == 'A') countA++;
                else if (grid[y][x] == 'B') countB++;
            }
        }
        
        String winner = (countA > countB) ? "A" : "B";
        
        System.out.println(countA + " " + countB);
        System.out.println(winner);
        
        sc.close();
    }
}


規則的な数列の和

def sum_from_one(x):
    if x <= 0:
        return 0
    full_cycles = x // 3
    remainder = x % 3
    
    total = full_cycles * 0
    if remainder == 1:
        total += 1
    elif remainder == 2:
        total += 1 + 0
        
    return total

n, k = map(int, input().split())
ans = sum_from_one(k) - sum_from_one(n - 1)
print(ans)

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextLong();
        long k = sc.nextLong();
        
        long ans = sumFromOne(k) - sumFromOne(n - 1);
        System.out.println(ans);
        
        sc.close();
    }
    
    private static long sumFromOne(long x) {
        if (x <= 0) {
            return 0;
        }
        long remainder = x % 3;
        
        long total = 0;
        if (remainder == 1) {
            total += 1;
        } else if (remainder == 2) {
            total += 1; // 1 + 0
        }
        
        return total;
    }
}


べき乗の計算

n = int(input())
MOD = 1000003
print(pow(2, n, MOD))


import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextLong();
        long mod = 1000003;
        
        long ans = 1;
        long base = 2;
        
        while (n > 0) {
            if (n % 2 == 1) {
                ans = (ans * base) % mod;
            }
            base = (base * base) % mod;
            n /= 2;
        }
        
        System.out.println(ans);
        
        sc.close();
    }
}

[素数判定]

import math

n = int(input())

if n < 2:
    print("NO")
else:
    is_prime = True
    limit = int(math.isqrt(n))
    for i in range(2, limit + 1):
        if n % i == 0:
            is_prime = False
            break
            
    if is_prime:
        print("YES")
    else:
        print("NO")



import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long n = sc.nextLong();
        
        if (n < 2) {
            System.out.println("NO");
        } else {
            boolean isPrime = true;
            long limit = (long) Math.sqrt(n);
            for (long i = 2; i <= limit; i++) {
                if (n % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            
            if (isPrime) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        
        sc.close();
    }
}

[最大公約数]

import math

a, b = map(int, input().split())
print(math.gcd(a, b))


#java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        long a = sc.nextLong();
        long b = sc.nextLong();
        
        System.out.println(gcd(a, b));
        
        sc.close();
    }
    
    private static long gcd(long a, long b) {
        while (b != 0) {
            long temp = a % b;
            a = b;
            b = temp;
        }
        return a;
    }
}