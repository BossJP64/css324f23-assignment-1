def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4  

def successors(s):
    x, y, z = s
    actions = []

    if x > 0 and y < 5:
        pour_amount = min(x, 5 - y)
        actions.append(((x - pour_amount, y + pour_amount, z), pour_amount))

    if x > 0 and z < 3:
        pour_amount = min(x, 3 - z)
        actions.append(((x - pour_amount, y, z + pour_amount), pour_amount))

    if y > 0 and x < 8:
        pour_amount = min(y, 8 - x)
        actions.append(((x + pour_amount, y - pour_amount, z), pour_amount))

    if y > 0 and z < 3:
        pour_amount = min(y, 3 - z)
        actions.append(((x, y - pour_amount, z + pour_amount), pour_amount))

    if z > 0 and x < 8:
        pour_amount = min(z, 8 - x)
        actions.append(((x + pour_amount, y, z - pour_amount), pour_amount))

    if z > 0 and y < 5:
        pour_amount = min(z, 5 - y)
        actions.append(((x, y + pour_amount, z - pour_amount), pour_amount))

    if y < 5 and x >= 5:
        actions.append(((x - (5 - y), 5, z), 5 - y))

    if y + z <= 5 and z != 0:
        actions.append(((x, y + z, 0), z))

    if z < 3 and x >= 3:
        actions.append(((x - (3 - z), y, 3), 3 - z))

    if y != 0:
        actions.append(((x + y, 0, z), y))

    return actions
