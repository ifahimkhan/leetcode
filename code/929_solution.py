class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse_local(s):
            out = []
            for c in s:
                if c == '+': break
                if c == '.': continue
                out.append(c)
            return ''.join(out)
                    
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@', maxsplit=1)
            local = parse_local(local)
            unique_emails.add(local + '@' + domain)
        return len(unique_emails)
            
