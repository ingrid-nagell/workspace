import math as m, re

data_path = "AoC\\2023\\03_1_test.txt"
data_path = "AoC\\2023\\03_2_test.txt"
data_path = "AoC\\2023\\03_input.txt"

# supersmooth solution from the internet (https://topaz.github.io/paste/#XQAAAQAcAgAAAAAAAAA0m0pnuFI8c+fPp4G3Y5M2miSs3R6AnrKm3fbDkugpdVsCgQOTZL/yzxGwy/N08UeBslxE7G36XluuSq4Y/2FE0+4nPcdj9lpkrrjBk5HRCFLEKuPjUV8tYPx04VDoJ1c6yyLzScmAGwNvzpPoqb5PkRyyy4dSEcuEDe/k0/U7h7pZVh4eTrNAIPsTNZohcltxuwuA4lrZSN37i0QZiufFpvLVyhV/dLBnmSr+2jwFcFE+W6OEIFQxK6MIJ2z7TWKj8lg6yV4yhJzTm+c+QHh2omzhGVLd2WdcHdhjmCyC+Btbr3yCqemYb/6tMUvz8VchnyHstx7QKKeLVmTOEyYqHH/qRDhlKXSQ23RWuPibCf4quQUPGpPDRsH4KITzLbIUVUdssnSp6ffcHO+dAISdzBOiznl5/+PI+jE=)

# Makes a coordinates of all characters

board = list(open(data_path))

chars = {
    (r, c): [] for r in range(len(board)) for c in range(len(board)) 
    if board[r][c] not in '01234566789.'
}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))

print(
    sum(sum(p)    for p in chars.values()),
    sum(m.prod(p) for p in chars.values() if len(p)==2)
)