class Solution(object):
    def validIPAddress(self, queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        def checkIPv4(queryIP):
            segs = queryIP.split(".")
            for seg in segs:
                # rule 1
                try:
                    if 0 <= int(seg) <= 255:
                        pass
                    else:
                        return False
                except:
                    return False
                # rule 2
                if seg[0] == "0" and len(seg) > 1:
                    return False
            return True

        def checkIPv6(queryIP):
            segs = queryIP.split(":")
            for seg in segs:
                # rule 1
                if 1 <= len(seg) <= 4:
                    pass
                else:
                    return False
                # rule 2
                for ch in seg:
                    if ord('0') <= ord(ch) <= ord('9') \
                        or ord('a') <= ord(ch) <= ord('f') \
                            or ord('A') <= ord(ch) <= ord('F'):
                        pass
                    else:
                        return False
            return True

        if len(queryIP.split(".")) == 4:
            if checkIPv4(queryIP):
                return "IPv4"

        if len(queryIP.split(":")) == 8:
            if checkIPv6(queryIP):
                return "IPv6"

        return "Neither"


queryIP = "172.16.254.1"
queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
queryIP = "256.256.256.256"
queryIP = "172.16.254.01"
queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334:7654"
queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7?34"
queryIP = "1e1.4.5.6"
queryIP = "00.0.0.0"
queryIP = "172.16.254.0"

solution = Solution()
print(solution.validIPAddress(queryIP))
