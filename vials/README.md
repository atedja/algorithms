### Problem

A vials mini-game solver. Each vial contains a set of different colors. You can transfer one color to another vial as long as the their top color matches, and there is enough space in the destination vial.
Your goal is to group/sort the colors each into their own vial.


### Example:

    Vial #0: ['R', 'G', 'B']
    Vial #1: ['G', 'R', 'B']
    Vial #2: ['B', 'R', 'G']
    Vial #3: []

Solution:

    Steps: [[0, 3], [1, 3], [2, 0], [2, 1], [2, 3], [1, 2], [0, 1], [0, 2]]

    Vial #0: []
    Vial #1: ['G', 'G', 'G']
    Vial #2: ['R', 'R', 'R']
    Vial #3: ['B', 'B', 'B']
