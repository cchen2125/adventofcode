def read_data(puzzle_file):
    with open(puzzle_file, 'r') as file:
        input_data = file.read().splitlines()

    connections = {}
    for connection in input_data:
        c1, c2 = tuple(connection.split('-'))
        if c1 in connections.keys():
            connections[c1].append(c2)
        else:
            connections[c1] = [c2]

        if c2 in connections.keys():
            connections[c2].append(c1)
        else:
            connections[c2] = [c1]

    return connections


def solve_p1(connections):
    t_computers = list(filter(lambda connection: connection[0] == 't', list(connections.keys())))

    groups = []

    for computer in t_computers:
        connected_comps = connections[computer]
        for i in range(len(connected_comps)):
            for j in range(i + 1, len(connected_comps)):
                if connected_comps[j] in connections[connected_comps[i]]:
                    if set([computer, connected_comps[i], connected_comps[j]]) not in groups:
                        groups.append(set([computer, connected_comps[i], connected_comps[j]]))

    return len(groups)


def solve_p2(connections):
    cliques = []

    for connection in connections.items():
        for comp in connection[1]:
            if set([connection[0], comp]) not in cliques:
                cliques.append(set([connection[0], comp]))

    new_added = True

    while new_added:
        new_added = False
        for clique in cliques:
            for c in connections.keys():
                in_clique = True
                for comp in clique:
                    if comp not in connections[c]:
                        in_clique = False
                        break
                if in_clique:
                    clique.add(c)
                    new_added = True

    max_size = 1
    max_clique = {}
    for clique in cliques:
        if len(clique) > max_size:
            max_size = len(clique)
            max_clique = clique

    max_clique = list(max_clique)
    max_clique.sort()
    return ','.join(max_clique)


def main():
    puzzle_file = 'puzzle23.txt'
    connections = read_data(puzzle_file)
    print(solve_p1(connections))
    print(solve_p2(connections))


if __name__ == '__main__':
    main()
