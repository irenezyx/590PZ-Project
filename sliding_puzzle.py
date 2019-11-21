class SlidingPuzzle:
    def __init__(self, board):
        self.board = board
        self.m = len(board)
        self.n = len(board[0])
        self.N = self.m * self.n
        self.set_start()
        self.set_target()
        self.solution = None
    
    def A_star(self):
        # f(n)=g(n)+h(n), 
        # g(n) is the cost of the path from the start node to n
        # h(n) is a heuristic function that estimates the cost of the cheapest path from n to the goal
        # if h(n) doesn't overestimate the distance to the goal => best answer guaranteed
        # can use Manhattan Distance as h(n): d(p, q) = sum(abs(pi - qi)), where pi and qi are the ith element of p and q
        # why Manhattan Distance: 
        #   we can only change one number's either col or row index by 1 by each state move;
        #   then we need at least counts of the total diff to move to the final state
        #   therefore, h(n) won't overestimate
        if not self.board: return -1
        N, m, n, start, target = self.N, self.m, self.n, self.start, self.target
        
        def heur(state):
            ans = 0
            for k, v in enumerate(state):
                cur_i, cur_j = k // n, k % n
                if v == 0:
                    t_i, t_j = m - 1, n - 1
                else:
                    t_i, t_j = (v - 1) // n, (v - 1) % n
                ans += abs(t_i - cur_i) + abs(t_j - cur_j)
            return ans
        
        for pos in range(N):
            if start[pos] == 0:
                break
        
        visited = {start: 0} # state: current total distance estimated (f)
        import heapq
        heap = [[-1, start, pos, 0, [start]]] # f(n), state, pos_0, cur_depth, path
        heapq.heapify(heap)
        while heap:
            f, state, pos0, depth, path = heapq.heappop(heap)
            if state == target:
#                self.print_path(path)
                self.solution = path
                return depth
            if f > visited[state]:
                continue # has found a better path to state later, this one is useless
            depth += 1
            i0, j0 = pos0//n, pos0%n
            for di in (-1, 1, -n, n):
                if (i0 == 0 and di == -n) or (i0 == m-1 and di == n) or (j0 == 0 and di == -1) or (j0 == n-1 and di == 1):
                    continue
                tmp = [num for num in state] # new state
                tmp[pos0], tmp[pos0+di] = tmp[pos0+di], tmp[pos0]
                t = tuple(tmp)
                f = heur(tmp) + depth
                if t not in visited or f < visited[t]:
                    visited[t] = f
#                    print(f, 'added')
                    heapq.heappush(heap, [f, t, pos0+di, depth, path+[t]])
        # visited all possible states
        return -1
    
    def bfs(self):
        if not self.board: return -1
        N, m, n, target = self.N, self.m, self.n, self.target
        # 1. Use BFS to find the shortest path for start node (start state) to the target state (target node). A state is a kind of placement of numbers.
        # 2. When BFS, get neighbor nodes(states) by the position of 0
        # 3. to easier make the state hashable (tuple), store each state in one-demension
        
        start = self.start
        for pos in range(N):
            if start[pos] == 0:
                break
        
        visited = {start: 1}
        from collections import deque
        queue = deque([[start, pos, 0, [start]]]) # note that queue generates from the iterable in the bracket
        while queue:
            state, pos0, depth, path = queue.popleft()
            if state == target:
#                self.print_path(path)
                self.solution = path
                return depth
            depth += 1
            i0, j0 = pos0//n, pos0%n
            for di in (-1, 1, -n, n):
                if (i0 == 0 and di == -n) or (i0 == m-1 and di == n) or (j0 == 0 and di == -1) or (j0 == n-1 and di == 1):
                    continue
                tmp = [num for num in state]
                tmp[pos0], tmp[pos0+di] = tmp[pos0+di], tmp[pos0]
                t = tuple(tmp)
                if t not in visited:
                    visited[t] = 1
                    queue.append([t, pos0+di, depth, path+[t]])
        # visited all possible states
        return -1
    
    def print_path(self, path):
        m, n = self.m, self.n
        for state in path:
            k = 0
            for _ in range(m):
                for _ in range(n):
                    print(state[k], end='\t')
                    k += 1
                print()
            print('------------------------')
    
    def set_target(self):
        N = self.N
        target = [i+1 for i in range(N)]
        target[N-1] = 0
        self.target = tuple(target)
        
    def set_start(self):
        start = [self.board[i][j] for i in range(self.m) for j in range(self.n)]
        self.start = tuple(start)

class PuzzleGenerator:
    def __init__(self, m, n, use_bfs=True):
        self.sol = self.ans = None
        self.board = self.generate(m, n, use_bfs)
        
    def generate(self, m, n, use_bfs=True):
        N = m * n
        init_state = list(range(N))
        board = [[-1] * n for _ in range(m)]
        import random
        cot = 0
        while cot < 100:
            cot += 1
            random.shuffle(init_state)
#            print(init_state)
            k = 0
            for i in range(m):
                for j in range(n):
                    board[i][j] = k
                    k += 1
            sp = SlidingPuzzle(board)
            steps = sp.bfs() if use_bfs else sp.A_star()
            if steps != -1:
                self.sp = sp
                self.sol = sp.solution
                self.ans = steps
                return board
        print('failed')
            
    def print_solution(self, file=None):
        print('Best Solution:')
        print(self.sol)
        print(self.ans, 'steps to get to target in total.')
        
if __name__ == '__main__':
#    board = [[0,2,3],[4,5,6],[7,1,8]]
#    sol = SlidingPuzzle(board)
#    print('Best Solution:')
#    ans = sol.bfs()
#    ans = sol.A_star()
#    print(ans, 'steps to get to target in total.')
    exper = [(3, 2), (3, 3), (3, 4), (4, 4)]
    num = 4
    step = 10
    import time
    
    for i in range(num):
        m, n = exper[i]
        with open('bfs_{0}_{1}.txt'.format(m, n), 'w') as bfs_file, \
        open('A_star_{0}_{1}.txt'.format(m, n), 'w') as a_star_file:
            print('--------------------')
            print('bfs:')
            for _ in range(step):
                st_time = time.time()
                pz = PuzzleGenerator(m, n, True)
                end_time = time.time()
                used = end_time-st_time
                pz.print_solution()
                print('time:', used)
                bfs_file.write('time: {0}\n'.format(used))
            print('--------------------')
            print('A*:')
            for _ in range(step):
                st_time = time.time()
                pz = PuzzleGenerator(m, n, False)
                end_time = time.time()
                used = end_time-st_time
                pz.print_solution()
                print('time:', used)
                a_star_file.write('time: {0}\n'.format(used))