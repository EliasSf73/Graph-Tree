# """
# MiniExam #5 Skeleton code
#
# Write additional codes below if necessary
# """
#
#
# def problem1(links):
#     redundant_link_indices = []
#     """
#     TODO: compute redundant links from given links
#     """
#     # get the cycle in the graph, edges of that cycle are redundant.
#
#     # graph of adjacent list (vertes: {neighbors and the index of edge (vertex, neighbor)})
#     graph = {}
#     for k, (i, j) in enumerate(links):
#         if i in graph:
#             graph[i][j] = k
#         else:
#             graph[i] = {j: k}
#         if j in graph:
#             graph[j][i] = k
#         else:
#             graph[j] = {i: k}
#
#     def dfs(graph, parent, vertex, visited):
#
#         for neighbor in graph[vertex]:
#             if neighbor != parent:
#                 if neighbor in visited:
#                     # cycle found
#                     return visited[visited.index(neighbor):] + [vertex]
#                 else:
#                     ret = dfs(graph, vertex, neighbor, visited + [vertex])
#                     if ret:
#                         return ret
#
#     cycle_vertices = dfs(graph, -1, 0, [])
#
#     for ind in range(-1, len(cycle_vertices) - 1):
#         a, b = cycle_vertices[ind], cycle_vertices[ind + 1]
#         redundant_link_indices.append(graph[a][b])
#
#     return redundant_link_indices
#
#
# def problem2(new_links, max_traffic):
#     """
#     TODO: compute whether given links never exceeds the max traffic
#     """
#
#     def dfs(graph, parent, vertex, steps):
#         if steps > max_traffic:
#             return False
#         for neighbor in graph[vertex]:
#             if neighbor == 0:
#                 return True
#             if neighbor != parent:
#                 if dfs(graph, vertex, neighbor, steps + len(graph[neighbor]) - 1):
#                     return True
#         return False
#
#     graph = {}
#     for (i, j) in new_links:
#         if i in graph:
#             graph[i].add(j)
#         else:
#             graph[i] = {j}
#         if j in graph:
#             graph[j].add(i)
#         else:
#             graph[j] = {i}
#     n = len(new_links) + 1
#     ret = all(dfs(graph, -1, vertex, 1) for vertex in range(1, n))
#     return ret
#
#
# #######################################
# # DO NOT edit below this line!        #
# #   though you are welcome to read :) #
# #######################################
#
# def simulate_problem2(links, max_traffic):
#     result = []
#     redundant_link_indices = problem1(links)
#     for link_index in redundant_link_indices:
#         new_links = links.copy()
#         new_links.pop(link_index)
#         if problem2(new_links, max_traffic):
#             result.append(link_index)
#     return result
#
#
# if __name__ == "__main__":
#     import sys
#
#     sys.setrecursionlimit(3000)
#
#
#     def readline():
#         return sys.stdin.readline().strip()
#
#
#     def read_links(n):
#         return [tuple(int(x) for x in readline().split()) for _ in range(n)]
#
#
#     # Help when no args given
#     argc = len(sys.argv)
#     if argc != 2 or sys.argv[1] not in ['1', '2']:
#         print(f"usage: python {sys.argv[0]} PROBLEM_NUMBER", file=sys.stderr)
#         exit(1)
#
#     if sys.argv[1] == '1':
#         # Problem 1
#         n = int(readline().split()[0])
#         links = read_links(n)
#         result = problem1(links)
#     else:
#         # Problem 2
#         n, max_traffic = (int(x) for x in readline().split())
#         links = read_links(n)
#         result = simulate_problem2(links, max_traffic)
#
#     # Print result
#     print(len(result))
#     for link_index in result:
#         print(link_index)

#
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z = zip(name, animal, age)
# print(z)
# l=[]
# for name,animal,age in z:
#     l.append((name,animal,age))
# print(l)
# Define the two dates in the year-month-date format

# import datetime
#
# date1 = "2022-12-11"
# date2 = "2021-01-01"
#
# # Convert the dates to datetime objects
# datetime1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
# datetime2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
#
# # Calculate the difference between the two dates
# difference = datetime1 - datetime2
#
# # Check if the difference is greater than 14 days
# if difference.days > 14:
#   # If the difference is greater than 14 days, print the difference
#   print(difference)


# Import the turtle and time modules
import turtle
import time

# Create a turtle object
sun = turtle.Turtle()

# Define the sun's size and color
sun.shapesize(3)
sun.color("yellow")

# Create a list of planet names, colors, and sizes
planets = [
    ("Mercury", "gray", 0.5),
    ("Venus", "orange", 0.8),
    ("Earth", "blue", 1.0),
    ("Mars", "red", 0.6),
    ("Jupiter", "brown", 1.8),
    ("Saturn", "beige", 1.4),
    ("Uranus", "lightblue", 1.2),
    ("Neptune", "darkblue", 1.1)
]

# Loop through the planets
for planet in planets:
  # Create a new turtle for each planet
  t = turtle.Turtle()

  # Set the planet's color and size
  t.color(planet[1])
  t.shapesize(planet[2])

  # Move the turtle to the correct position
  t.penup()
  t.forward(100 * planet[2])
  t.pendown()

  # Draw the planet
  t.circle(100 * planet[2])

  # Write the planet's name
  t.write(planet[0])

# Set the turtle speed to maximum
sun.speed(0)

# Animate the planets moving around the sun
for i in range(360):
  sun.right(1)
  time.sleep(0.05)



















