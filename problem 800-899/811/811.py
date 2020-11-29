from typing import List

class Solution:
    def __init__(self):
        self.domain_list = list()
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cp_table = dict()
        for domains in cpdomains:
            length, domains = domains.split()
            length = int(length)
            while "." in domains:
                if domains not in cp_table:
                    cp_table[domains] = length
                else:
                    cp_table[domains] += length
                domains = domains[domains.index(".")+1 : ]
            if domains not in cp_table:
                cp_table[domains] = length
            else:
                cp_table[domains] += length
        for domain in cp_table:
            self.domain_list.append(str(cp_table[domain]) + " " + domain)
        return self.domain_list

if __name__ == "__main__":
    input_list = [
        ["9001 discuss.leetcode.com"],
        ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    ]
    for input_item in input_list:
        print("\ninput=", input_item)
        output = Solution().subdomainVisits(input_item)
        print("output=", output)