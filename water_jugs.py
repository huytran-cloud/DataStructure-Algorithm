from collections import deque


def min_steps(a, b, c):
    initial_state = (0, 0)

    queue = deque([initial_state])

    visited = {initial_state}

    steps = {initial_state: 0}

    while queue:
        state = queue.popleft()
        x, y = state

        if x == c or y == c:
            return steps[state]

        next_states = [(a, y), (x, b), (0, y), (x, 0), (min(x + y, a), 0 if x + y <= a else y - (a - x)),
                       (0 if x + y <= b else x - (b - y), min(x + y, b))]

        for next_state in next_states:
            if next_state not in visited:
                queue.append(next_state)
                visited.add(next_state)
                steps[next_state] = steps[state] + 1

    return -1


a, b, c = map(int, input().split())

print(min_steps(a, b, c))
