import heapq
cable_lengths = [1, 10, 5, 6, 2, 11]

def connect_cables(cable_lengths):
    heapq.heapify(cable_lengths)
    connection_order = []
    
    while len(cable_lengths) > 1:
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)
        connection_order.append((first, second))
        heapq.heappush(cable_lengths, first + second)
    
    return connection_order

connection_order = connect_cables(cable_lengths)
print("Порядок об'єднання кабелів:")
for i, (first, second) in enumerate(connection_order, start=1):
    print(f"Крок {i}: Об'єднання кабелів з довжиною {first} та {second}, загальна довжина: {first + second}")