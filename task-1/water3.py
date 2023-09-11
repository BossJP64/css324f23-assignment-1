def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    x, y, z = s
    actions = []

    if x > 0 and y < 5:
        pour_amount = min(x, 5 - y)
        actions.append(("8 to 5", (x - pour_amount, y + pour_amount, z)))

    if x > 0 and z < 3:
        pour_amount = min(x, 3 - z)
        actions.append(("8 to 3", (x - pour_amount, y, z + pour_amount)))

    if y > 0 and x < 8:
        pour_amount = min(y, 8 - x)
        actions.append(("5 to 8", (x + pour_amount, y - pour_amount, z)))

    if y > 0 and z < 3:
        pour_amount = min(y, 3 - z)
        actions.append(("5 to 3", (x, y - pour_amount, z + pour_amount)))

    if z > 0 and x < 8:
        pour_amount = min(z, 8 - x)
        actions.append(("3 to 8", (x + pour_amount, y, z - pour_amount)))

    if z > 0 and y < 5:
        pour_amount = min(z, 5 - y)
        actions.append(("3 to 5", (x, y + pour_amount, z - pour_amount)))

    return actions
