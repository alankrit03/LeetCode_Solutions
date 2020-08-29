class Solution:
    def defangIPaddr(self, address: str) -> str:
        import re

        address = re.sub('\.', '[.]', address)

        return address