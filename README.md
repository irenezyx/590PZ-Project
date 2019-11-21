# 590PZ-Project
Forks of this are student projects for IS 590PZ

This sliding puzzle project is our final project for IS590-PZ class.

Topic Setting
We did consider the different topics of sudoku, Klotski and number slide puzzle. We chose the number slide puzzle after careful consideration.
	• Sudoku (https://en.wikipedia.org/wiki/Sudoku)
		○ We did not choose sudoku because it is not a proper choice for this class project--it needs us to write too much code on specific deterministic strategies but the time we have for project is very limited. 
	• Klotski (https://en.wikipedia.org/wiki/Klotski )
		○ Klotski is a kind of sliding puzzle with 10 different-size block pieces placed in a 4x5 board.  
		○ The numbers of starting state and solutions are limited. 
		○ When randomly change the board size and movable blocks, the puzzle is very likely to be meaningless and not challenging any more. 
	• Number slide puzzle (https://en.wikipedia.org/wiki/Sliding_puzzle)
		○ Comparing with Klotski, there are more game states.
		○ And it allows us to generate the starting game board much more flexibly.

 About number slide puzzle 
	• The number slide puzzle consists of a frame of numbered blocks in random order with one block missing. 
	• To solve the puzzle, the players will need to rearrange the numbers into orders by sliding the blocks in the board. 
	• In our situation, we are looking for the shortest moving path solution. 
	• More details see here in wiki https://en.wikipedia.org/wiki/Sliding_puzzle

Game Solver
	• BFS
		○ Start at the tree root. 
		○ Explore horizontally first, visit all the nodes of current layer before moving on to the next depth layer.
		○ Time Complexity: O(Row*Column*(Row*Column )!)
    
	• A* search
		○ Start from a specific starting node of a graph. 
		○ Maintain a tree of paths originating at the start node and extend those paths one edge at a time until its termination criterion is satisfied.
		○ It aims to find a path to the given goal node having the smallest cost. 
		○ Time Complexity: O(Row*Column*(Row*Column )!)
    
	• An important pruning
		○ According to research, the set of states can be split in half which are exclusive. One could transform to target. The other half must could transform to 1, 2, ..., N-3, N-1, N-2, 0
	
	• More about A* search
		○ f(n)=g(n)+h(n)
		○ g(n): the cost of the path from the start node to n
		○ h(n): a heuristic function that estimates the cost of the cheapest path from n to the goal
		○ Best answer guaranteed: if h(n) doesn't overestimate the distance to the goal
		○ Apply Manhattan Distance as h(n): d(p, q) = sum(abs(pi - qi)), where pi and qi are the ith element of p and q
		○ Why Manhattan Distance: 
				□ For each move, only the number’s column or row index can be changed 
				□ Then we need at least counts of the total differences to move to the final state. 
	
Game Generator
	• Randomly shuffle the blocks in games board
	• Applied BFS or A* to check if there is a solution
		○ If yes, return the solution. Save the solution and print out the solution. 


Comparison of BFS and A*
	• Experiment design
		○ Generate the starting game board in different sizes using BFS or A* generator 
		○ Collect ten pieces of data for each specified starting game board
		○ Take the average since we have random shuffle when generating game boards
		○ Compare the results 
 	• Experiment Result
  	○ The graph shows the average number and variance of each type of game board powered by BFS or A*
		○ The bar is the average runtime generating the specific game board. 
		○ The variance is too small. So it is not very conspicuous in graph. 
		○ It takes more than an hour to generate a 4 x 4 game board using BFS. Because the testing time is too long, we will not include the runtime data of 4 x 4 game board. 
    ○ The data of 3x3 game board shows a great time performance of A* search algorithm. 
