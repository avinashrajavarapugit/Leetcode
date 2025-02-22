class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        domains = collections.defaultdict(set)
        for email in emails:
            name, domain = email.split('@')
            name = name.replace('.', '')
            name = name.split('+')
            domains[domain].add(name[0])
        res = 0
        for u, v in domains.items():
            res += len(v)
        return res
