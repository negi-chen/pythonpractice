
#D -20
「座標系での向きの変わる移動 Java編」

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String line[] = sc.nextLine().split(" ");
        
        int x = Integer.parseInt(line[0]);
        int y = Integer.parseInt(line[1]);
        int n = Integer.parseInt(line[2]);
        
        String directions = "N"; 
        
        String store[] = new String[n];
        
        for (int m = 0; m < n; m++) {
            String leftor = sc.next();
            store[m] = leftor; 
            
            if (directions.equals("N")) {
                if (leftor.equals("R")) {
                    x += 1;
                    directions = "E";
                } else if (leftor.equals("L")) {
                    x -= 1;
                    directions = "W";
                }
            } else if (directions.equals("W")) {
                if (leftor.equals("R")) {
                    y -= 1;
                    directions = "N";
                } else if (leftor.equals("L")) {
                    y += 1;
                    directions = "S";
                }
            } else if (directions.equals("E")) {
                if (leftor.equals("R")) {
                    y += 1;
                    directions = "S";
                } else if (leftor.equals("L")) {
                    y -= 1;
                    directions = "N";
                }
            } else if (directions.equals("S")) {
                if (leftor.equals("R")) {
                    x -= 1;
                    directions = "W";
                } else if (leftor.equals("L")) {
                    x += 1;
                    directions = "E";
                }
            }
        System.out.println(x + " " + y);
        }
        
    }
}



#PYTHON
x, y, n = input().split()
x = int(x)
y = int(y)
n = int(n)
dr = "N"

for i in range(n):
    rightorleft = input().strip()
    # print(rightorleft)
    if dr == "N":
        if rightorleft == "R":
            x += 1
            dr = "E"
        elif rightorleft == "L":
            x -= 1
            dr = "W"
            
    elif dr == "E":
        if rightorleft == "R":
            y += 1
            dr = "S"
        elif rightorleft == "L":
            y -= 1
            dr = "N"
            
    elif dr == "S":
        if rightorleft == "R":
            x -= 1
            dr = "W"
        elif rightorleft == "L":
            x += 1
            dr = "E"
            
    elif dr == "W":
        if rightorleft == "R":
            y -= 1
            dr = "N"
        elif rightorleft == "L":
            y += 1
            dr = "S"
            
    print(x, y)


#ans from paiza
x, y, n = map(int, input().split())
directions = ["N", "E", "S", "W"]
now_direction = 0

for _ in range(n):
    lr = input()
    if lr == "L":
        now_direction = (3 + now_direction) % 4
    else:
        now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        y -= 1
    elif directions[now_direction] == "E":
        x += 1
    elif directions[now_direction] == "S":
        y += 1
    elif directions[now_direction] == "W":
        x -= 1

    print(x, y)