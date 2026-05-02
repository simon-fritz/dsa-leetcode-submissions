class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += "$"+str(len(s))+"$"+s
        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []
        counter = 0
        while counter < len(s):
            #parse length
            num=""
            if s[counter] == "$":
                counter += 1
                while s[counter] != "$":
                    num+=s[counter]
                    counter += 1
            counter += 1
            #parse s
            d = ""
            for i in range(int(num)):
                d += s[counter]
                counter += 1
            decoded.append(d)
        return decoded
        



