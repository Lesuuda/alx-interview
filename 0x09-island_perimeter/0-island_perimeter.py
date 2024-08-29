#!/usr/bin/python3
"""solves the island perimeter problem using dfs"""


def island_perimeter(grid):
    """solves the island perimeter problem"""
    visited = set()

    def dfs(i, j):
        """a dfs function to store visited nodes"""
        if i >= len(grid) or j >= len(grid[0]) or \
                i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0

        visited.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)
        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
