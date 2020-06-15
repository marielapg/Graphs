from util import Stack, Queue

def earliest_ancestor(ancestors, starting_node):
    parents = {}

    for pc in ancestors:
        if pc[1] not in parents.keys():
            parents[pc[1]] = {pc[0]}
        else:
            parents[pc[1]].add(pc[0])

    print(parents)
    print(starting_node)

    if starting_node not in parents:
        print("NOT FOUND")
        return -1
    else:
        q = Queue()
        q.enqueue(starting_node)
        visited = set()
        child = None

        while q.size() > 0:
            child = q.dequeue()
            if child not in visited:
                print("PARENT: ", child)
                visited.add(child)
                if child in parents:
                    for parent in parents[child]:
                        q.enqueue(parent)
        print("")
        print("RETURN: ", child)
        return child
 