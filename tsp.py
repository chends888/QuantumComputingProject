import sys
import math

def dist(p1, p2):
    '''
        Distance between two points
    '''
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def path_dist(best_sol, points):
    '''
        Calculate the total distance of a specific path
    '''
    d = dist(points[best_sol[-1]], points[best_sol[0]])
    for i in range(len(best_sol)-1):
        d += dist(points[best_sol[i]], points[best_sol[i+1]])
    return d

def backtrack(points, idx, curr_cost, curr_sol, best_cost, best_sol):
    # idx is at the end, so return the current best solution
    if idx == len(points):
        curr_cost += dist(points[curr_sol[0]], points[curr_sol[-1]])
        if curr_cost < best_cost:
            best_sol[:] = curr_sol.copy()
            best_cost = curr_cost
            # print('best:', best_cost, file=sys.stderr)
        count.append(0)
        return best_cost

    # Change the 'i', which is the start point for the new recursive call
    for i in range(len(points)):
        if not usado[i]:
            usado[i] = True
            curr_sol[idx] = i

            new_cost = curr_cost + dist(points[curr_sol[idx-1]], points[curr_sol[idx]])
            best_cost = backtrack(points, idx+1, new_cost, curr_sol, best_cost, best_sol)

            usado[i] = False
            curr_sol[idx] = -1

    return best_cost


count = []

N = int(input())
points = []
for i in range(N):
    x, y = [float(x) for x in input().split()]
    points.append((x, y))

usado = [False] * N
curr_sol = [-1] * N
best_sol = [-1] * N

curr_sol[0] = 0
usado[0] = True

backtrack(points, 1, 0, curr_sol, math.inf, best_sol)
print('{:.5f}'.format(round(path_dist(best_sol, points), 5)), '1')
print(' '.join([str(i) for i in best_sol]))
print('Total tries:', len(count))
