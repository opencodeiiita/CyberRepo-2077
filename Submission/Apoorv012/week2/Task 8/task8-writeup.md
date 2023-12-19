# Task 8: Cracking Password
### Introduction
I had to find the correct password, to get the flag. I had the python file which checked if the input password is same as the desired password. If it is the same, it would give out the flag.

### Approach
I realized that the possible passwords in `dictionary.txt` are 4 character long strings, made up of numbers, and `a to f`.

So I wrote a quick code in python that would generate the probable password from `0000` to `ffff` and break out if it got the password.

Code:
```py
def main():
    chars = "0123456789abcdef"
    for i in chars:
        for j in chars:
            for k in chars:
                for l in chars:
                    guess = i + j + k + l
                    _hash = hash_pw(guess)
                    
                    if _hash == correct_pw_hash:
                        print(guess)
                        return

main()
```

This gave me the correct password, which I used to get the flag.

### Flag: `opencode{f1r5t_f1a&}`
