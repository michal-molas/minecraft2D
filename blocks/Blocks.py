from blocks.Dirt import Dirt
from blocks.Water import Water
from blocks.Stone import Stone
from blocks.Grass import Grass
from blocks.Sky import Sky
from blocks.Bedrock import Bedrock
from blocks.Tree import Tree
from blocks.Leaves import Leaves
from blocks.Iron import Iron
from blocks.Gold import Gold
from blocks.Diamond import Diamond

# TODO: change this global reference
blocks = {}

blocks.update({"dirt": Dirt})
blocks.update({"water": Water})
blocks.update({"stone": Stone})
blocks.update({"grass": Grass})
blocks.update({"sky": Sky})
blocks.update({"bedrock": Bedrock})
blocks.update({"tree": Tree})
blocks.update({"leaves": Leaves})
blocks.update({"iron": Iron})
blocks.update({"gold": Gold})
blocks.update({"diamond": Diamond})

print(blocks)
