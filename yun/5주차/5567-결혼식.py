friend_number = int(input())
list_length = int(input())
edges = []
result = set([])
for _ in range(list_length):
  a, b = input().split()
  if a > b:
    a, b = b, a
  edges.append((int(a), int(b)))


def get_firsthand(edges, starting_number):
  result = []
  for edge in edges:
    if starting_number in edge:
      if starting_number == edge[0]:
        result.append(edge[1])
      else:
        result.append(edge[0])
  return result

firsthand = get_firsthand(edges, 1)

for friend in firsthand:
  result.add(friend)
  for i in get_firsthand(edges, friend):
    result.add(i)

result.remove(1)
print(len(result))