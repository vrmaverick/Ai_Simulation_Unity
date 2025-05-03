AI BASED SIMULATION FOR NAVIGATION OF PATH FINDING AND AVOIDANCE

This project focuses on simulating AI-based navigation for pathfinding and avoidance using various algorithms. The primary goal is to compare and contrast different algorithms to determine their effectiveness in real-world scenarios.

Pathfinding Algorithms

Breadth-First Search (BFS)
Pros:

Guarantees the shortest path in an unweighted graph.
Well-suited for finding paths in small grids or maps.
Always explores the closest nodes first, leading to fewer unnecessary steps.
Cons:

Memory-intensive for larger graphs due to its breadth-first nature.
May not perform optimally in situations where the shortest path is long.
Depth-First Search (DFS)
Pros:

Memory usage is typically lower compared to BFS.
Can be effective in finding paths that go deep before going wide.
Suitable for situations where the path length is not critical.
Cons:

Doesn't guarantee the shortest path.
Can get stuck in infinite loops or long paths if not properly implemented.
A* Algorithm
Pros:

Utilizes both actual cost (g) and heuristic (h) to estimate the total cost (f), resulting in efficient pathfinding.
Guarantees the shortest path under certain conditions.
Well-suited for scenarios where performance is crucial.
Cons:

Requires a consistent and admissible heuristic for optimal results.
May not be the best choice for graphs with irregular costs or terrain.
Dijkstra's Algorithm
Pros:

Finds the shortest path in a weighted graph.
Can be used to find the shortest path even when there are negative weights, as long as there are no negative cycles.
Suitable for scenarios where the actual cost matters more than the heuristic.
Cons:

May not be the most efficient choice for graphs with lots of nodes and edges.
Doesn't consider heuristics, which might lead to suboptimal paths.
Conclusion

Each pathfinding algorithm discussed here has its own strengths and weaknesses. The choice of algorithm depends on the specific requirements of your project. BFS and DFS are useful for simpler scenarios, while A* and Dijkstra's Algorithm provide more sophisticated solutions for weighted graphs. Consider your project's needs, the nature of the graph, and the computational resources available when selecting the appropriate algorithm.


![MAP](Final/Python_Connection_final/Detailed_map.png
--
## File Structure

--
```
  /Final 
  |- Python Connections Final
      |---a_star.py # Applying A* algorithm
      |---connection.py # It acts as a conncetion point between Unity and Python using Sockets
      |---notify.py # It notfies the user via email or sms
      |---pdf.py # Genrates the PDF of dynamic template
      |---send_mail.py # Uses API to send Emails
      |---test.py # For Testing without Unity
      |---ui.py # tkinter UI
      |---qr.jpeg # My UPI QR code for Payment :) Buy me a Coffee
      |---invoice.html # Template for dynamic Invoice
      |---Detailed_map.png # Unity Map used for demo
  |- BotController.cs # C# file used by the agent in Unity
  BFS_DFS_A*_DJASTRA.py # Testing the algorithm
  mini_report.pdf # Report to refer for this project
```
--
## Contact 
Feel Free to Contact me regarding any Queries
[Portfolio](https://vedant-ranade.netlify.app/)
[vedantranade2612@gmail.com](vedantranade2612@gmail.com)
[LinkdIn](https://www.linkedin.com/in/vedant-ranade-683867271/)
