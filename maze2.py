from pyamaze import maze,agent, textLabel

def BFS(m):
    start = (m.rows, m.cols)
    explored = [start]
    frontier = [start]
    bfsPath={}
    while len(frontier) > 0:
        currCell = frontier[0]
        if currCell == (1, 1):
            break
        frontier.remove(currCell)
        for d in 'ESNW':
            if m.maze_map[currCell][d] == True:
                if d == 'E':
                    childCell = (currCell[0], currCell[1] + 1)
                if d == 'W':
                    childCell = (currCell[0], currCell[1] - 1)
                if d == 'S':
                    childCell = (currCell[0] + 1, currCell[1])
                if d == 'N':
                    childCell = (currCell[0] - 1, currCell[1])
                if childCell in explored:
                    continue
                explored.append(childCell)
                frontier.append(childCell)
                bfsPath[childCell] = currCell
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[bfsPath[cell]] = cell
        cell = bfsPath[cell]
    return fwdPath
if __name__ == "__main__":
    m = maze(50, 70)
    m.CreateMaze(loopPercent=100)
    path = BFS(m)
    a = agent(m, footprints=True,filled=True)
    m.tracePath({a: path})
    l=textLabel(m, 'Length of shotrest path:', len(path)+1)
    m.run()