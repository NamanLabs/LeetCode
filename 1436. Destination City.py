class Solution:

  def destCity(self, paths: list[list[str]]) -> str:
    # Set of all cities with an outgoing path
    outgoing_cities = {path[0] for path in paths}

    # Find the destination city that has no outgoing path
    for path in paths:
      dest = path[1]
      if dest not in outgoing_cities:
        return dest
