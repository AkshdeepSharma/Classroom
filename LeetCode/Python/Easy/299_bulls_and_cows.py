class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        d_secret = {}
        d_guess = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in d_secret:
                    d_secret[secret[i]] += 1
                else:
                    d_secret[secret[i]] = 1
                if guess[i] in d_guess:
                    d_guess[guess[i]] += 1
                else:
                    d_guess[guess[i]] = 1
        for key, val in d_secret.items():
            if key in d_guess:
                cows += min(val, d_guess[key])
        return str(bulls) + "A" + str(cows) + "B"