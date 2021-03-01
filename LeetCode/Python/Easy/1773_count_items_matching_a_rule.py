class Solution:
    def countMatches(self, items: List[List[str]], rule_key: str, rule_value: str) -> int:
        possible_keys = ['type', 'color', 'name']
        rule_key = possible_keys.index(rule_key)
        count = 0
        for item in items:
            if item[rule_key] == rule_value:
                count += 1
        return count
