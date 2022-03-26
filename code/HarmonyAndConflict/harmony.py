from itu.algs4.fundamentals import queue

nodes , edges = map(int, input().split())

harmony_dict = {i: [] for i in range(nodes)}
conflict_dict = {i: [] for i in range(nodes)}
col_list = [None] * nodes

for _ in range(edges):
    x, y, edge_type = map(int, input().split())

    if edge_type == 1: 
        conflict_dict[x].append(y)
        conflict_dict[y].append(x)
    elif edge_type == 0:
        harmony_dict[x].append(y)
        harmony_dict[y].append(x)

# laws of the network
# if it is a conflict edge, 
#   all child nodes have a different colour/type to the parent node
# if it is a harmony edge,
#   all child nodes have the same colour/type as the parent node

for i in range(nodes):

    if conflict_dict[i] == []:
        continue
    
    elif col_list[i] != None:
        continue

    vis_queue = queue.Queue()
    vis_queue.enqueue(i)
    col_list[i] = True

    while not vis_queue.is_empty():
        node_a = vis_queue.dequeue()
        color_a = col_list[node_a]

        for node_b in conflict_dict[node_a]:
            color_b = col_list[node_b]
            if color_b == None:
                vis_queue.enqueue(node_b)
                col_list[node_b] = not color_a
            # if node_a has the same color as node_b then stop the loop
            elif color_b == color_a:
                print(0)
                quit()
        
        for node_b in harmony_dict[node_a]:
            color_b = col_list[node_b]
            if color_b == None:
                vis_queue.enqueue(node_b)
                col_list[node_b] = color_a
            # if node_a does not have the same color as node_b then stop the loop
            elif color_b != color_a:
                print(0)
                quit()

print(1)
