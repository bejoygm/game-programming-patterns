from typing import NewType

Texture = NewType('Texture', str)
Mesh = NewType('Mesh', str)

class TreeModel:
    mesh: Mesh = None
    bark: Texture = None
    leaves: Texture = None

class Tree:
    model = TreeModel()
    height: int = 10