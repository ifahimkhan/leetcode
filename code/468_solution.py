class Solution:
    def validIPAddress(self, IP: str) -> str:
        digits = set('0123456789')
        hexdigits = set('0123456789abcdefABCDEF')

        def valid_ipv4_num(num):
            if not num: return False
            if not set(num).issubset(digits): return False
            if num[0] == '0' and len(num) > 1: return False
            return 0 <= int(num) <= 255
        
        def valid_ipv4(IP):
            for num in IP.split('.'):
                if not valid_ipv4_num(num): return 'Neither'
            return 'IPv4'

        def valid_ipv6_num(num):
            if not num: return False
            if not set(num).issubset(hexdigits): return False
            return len(num) <= 4
        
        def valid_ipv6(IP):
            for num in IP.split(':'):
                if not valid_ipv6_num(num): return 'Neither'
            return 'IPv6'
        
        if IP.count('.') == 3: return valid_ipv4(IP)
        if IP.count(':') == 7: return valid_ipv6(IP)
        return 'Neither'