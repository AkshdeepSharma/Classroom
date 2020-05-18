class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        known_cities = set()
        for A, B in paths:
            known_cities.add(A)
        for A, B in paths:
            if B not in known_cities:
                return B
