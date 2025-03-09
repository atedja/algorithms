import copy


# Define colors
RED = 'R'
GREEN = 'G'
BLUE = 'B'
PINK = 'P'
DARKBLUE = 'DB'
LIGHTBLUE = 'LB'
DARKGREEN = 'DG'
LIGHTGREEN = 'LG'
YELLOW = 'Y'
DARKYELLOW = 'DY'
ORANGE = 'O'
CREME = 'C'
GREY = 'Gr'
NONE = '-'



class State:
    vials = []
    vials_id = None
    maxsize = 0

    def __init__(self, vials, maxsize):
        self.vials = vials
        self.maxsize = maxsize
        str(self)

    def __str__(self):
        if self.vials_id:
            return self.vials_id

        nones = [NONE] * self.maxsize
        s = []
        for v in self.vials:
            ps = (v + nones)[:len(nones)]
            s.append(','.join(ps))

        s.sort()

        self.vials_id = ':'.join(s)
        return self.vials_id


    def __eq__(self, other):
        return isinstance(other, State) and other is not None and self.vials_id == other.vials_id


    def __hash__(self, other):
        return self.vials_id


    # Returns true if vial is full and all of the same color
    def is_vial_complete(self, v):
        return len(v) == self.maxsize and len(set(v)) == 1


    # Returns true if vial is empty
    def is_vial_empty(self, v):
        return len(v) == 0


    # Returns true if vial is full
    def is_vial_full(self, v):
        return len(v) == self.maxsize


    # Returns true if vial is not empty but only has one color
    def vial_has_one_color(self, v):
        return len(v) < self.maxsize and len(set(v)) == 1


    # Check if we can pour vial v1 to v2
    # Top colors have to match and there's enough empty space
    # Returns true on success, false otherwise
    def can_pour(self, v1, v2):
        # can't pour if v1 is empty or v2 is full
        if self.is_vial_empty(v1) or self.is_vial_full(v2) or self.is_vial_complete(v1) or self.is_vial_complete(v2):
            return False

        # can't pour if v1 only has one color and v2 is empty
        # this is pointless and reduce the lookup path
        if self.vial_has_one_color(v1) and self.is_vial_empty(v2):
            return False

        if self.is_vial_empty(v2):
            return True

        v1_color = v1[-1]
        v2_color = v2[-1]

        if v2_color != v1_color:
            return False

        return True


    # Pours vial v1 to v2
    # Returns true on success, false otherwise
    def pour(self, v1, v2):
        if self.can_pour(v1, v2):
            v1_color = v1[-1]
            v2_color = None if self.is_vial_empty(v2) else v2[-1]

            # pour till v2 full
            while (len(v1) > 0 and len(v2) < self.maxsize and (v2_color == None or v1[-1] == v2_color)):
                c = v1.pop()
                v2.append(c)
                v2_color = c

            return True

        return False


    # Executes the steps
    # Returns a new State if steps are taken, otherwise returns self
    def traverse(self, steps):
        if not steps:
            return self

        vials = copy.deepcopy(self.vials)

        for s in steps:
            if not self.pour(vials[s[0]], vials[s[1]]):
                print(f"ERROR: Cannot pour {potions[s[0]]} to {potions[s[1]]}")
                print(f"ERROR: This should have been detected earlier!")
                return None

        return State(vials, self.maxsize)


    # Returns true if the set is complete
    # All vials are either complete or empty
    def is_complete(self):
        done = True
        for v in self.vials:
            done = done and (self.is_vial_complete(v) or self.is_vial_empty(v))

        return done



# Stores a list of all explored states to cut down on the number of search paths
class StateMap:
    state_map = []

    # Adds state to the StateMap
    # Returns true on success, false otherwise
    def add(self, state):
        if self.exists(str(state)):
            return False

        self.state_map.append(str(state))
        return True

    # Checks if state exists in the StateMap
    def exists(self, state):
        return str(state) in self.state_map

    # Checks if state exists in the StateMap
    def count(self):
        return len(self.state_map)


def test_state():
    print("Testing State object ...", end='')
    state = State([
        [RED, PINK, DARKBLUE, DARKGREEN],
        [DARKGREEN, RED, RED, PINK],
        [PINK, DARKBLUE, RED, PINK],
        [DARKBLUE, DARKBLUE, DARKGREEN, DARKGREEN],
        [],
        [],
    ], 4)

    # test can_pour
    assert state.can_pour([RED, PINK, DARKBLUE, DARKGREEN], [DARKBLUE, DARKBLUE, DARKGREEN, DARKGREEN]) == False
    assert state.can_pour([RED, PINK, DARKBLUE, DARKGREEN], []) == True
    assert state.can_pour([RED, PINK, DARKBLUE, DARKGREEN], [DARKGREEN]) == True
    assert state.can_pour([RED, PINK, DARKBLUE, DARKGREEN], [DARKGREEN, RED]) == False
    assert state.can_pour([], [DARKGREEN, RED]) == False
    assert state.can_pour([RED, RED, RED], []) == False
    assert state.can_pour([RED, RED, RED], [RED]) == True
    assert state.can_pour([RED, RED, RED, RED], [RED]) == False

    # test pour
    v1 = [RED, RED, RED, CREME]
    v2 = [LIGHTBLUE, CREME]
    assert state.pour(v1, v2) == True
    assert v1 == [RED, RED, RED]
    assert v2 == [LIGHTBLUE, CREME, CREME]

    v1 = [RED, CREME, CREME, CREME]
    v2 = [LIGHTBLUE, CREME]
    assert state.pour(v1, v2) == True
    assert v1 == [RED, CREME]
    assert v2 == [LIGHTBLUE, CREME, CREME, CREME]

    # same as state above, just order is different
    state2 = State([
        [DARKBLUE, DARKBLUE, DARKGREEN, DARKGREEN],
        [DARKGREEN, RED, RED, PINK],
        [],
        [RED, PINK, DARKBLUE, DARKGREEN],
        [],
        [PINK, DARKBLUE, RED, PINK]
    ], 4)
    assert state == state2

    # test traverse
    state = State([
        [RED, PINK, DARKBLUE, DARKGREEN],
        [DARKGREEN, RED, RED, PINK],
        [PINK, DARKBLUE, RED, PINK],
        [DARKBLUE, DARKBLUE, DARKGREEN, DARKGREEN],
        [],
        [],
    ], 4)
    state_result = state.traverse([[0,4],[3,4],[1,5],[2,5]])
    state_comp = State([
        [RED, PINK, DARKBLUE],
        [DARKGREEN, RED, RED],
        [PINK, DARKBLUE, RED],
        [DARKBLUE, DARKBLUE],
        [DARKGREEN, DARKGREEN, DARKGREEN],
        [PINK, PINK],
    ], 4)
    assert state_result == state_comp

    # test complete
    state = State([
        [RED, RED, RED, RED],
        [PINK, PINK, PINK, PINK],
        [],
    ], 4)
    assert state.is_complete() == True
    print("OK")


def solve(initial):
    stack = []
    stack.append([])

    found = False
    while len(stack) > 0:
        steps = stack.pop()

        this_state = initial.traverse(steps)
        if this_state == None:
            break

        if not state_map.add(this_state):
            continue

        if this_state.is_complete():
            print("Found a solution:")
            print(steps)
            print(this_state)
            found = True
            break

        # search
        for i, v1 in enumerate(this_state.vials):
            for j, v2 in enumerate(this_state.vials):
                if i == j:
                    continue

                if this_state.can_pour(v1, v2):
                    s = copy.deepcopy(steps)
                    s.append([i, j])
                    stack.append(s)

    if not found:
        print("Unable to find a solution")

    print("Number of explored states:", state_map.count())



# input vials
initial_state = State([
    [DARKGREEN, PINK, DARKBLUE, DARKGREEN],
    [LIGHTBLUE, DARKYELLOW, RED, ORANGE],
    [CREME, GREY, LIGHTBLUE, LIGHTGREEN],
    [LIGHTGREEN, ORANGE, LIGHTBLUE, GREY],
    [ORANGE, DARKBLUE, DARKYELLOW, DARKGREEN],
    [RED, PINK, DARKBLUE, LIGHTGREEN],
    [PINK, DARKBLUE, DARKYELLOW, ORANGE],
    [LIGHTGREEN, DARKYELLOW, CREME, GREY],
    [DARKGREEN, CREME, RED, CREME],
    [PINK, GREY, RED, LIGHTBLUE],
    [],
    [],
    [],
], 4)

initial_state2 = State([
    [RED, GREEN, BLUE],
    [GREEN, RED, BLUE],
    [BLUE, RED, GREEN],
    [],
], 3)

initial_state3 = State([
    [RED, PINK, DARKBLUE, DARKGREEN],
    [DARKGREEN, RED, RED, PINK],
    [PINK, DARKBLUE, RED, PINK],
    [DARKBLUE, DARKBLUE, DARKGREEN, DARKGREEN],
    [],
    [],
], 4)

state_map = StateMap()


if __debug__:
    test_state()
else:
    solve(initial_state)
