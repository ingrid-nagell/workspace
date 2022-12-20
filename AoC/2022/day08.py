import numpy as np

#my_path = 'C:/Users/G020772/workspace/AoC/2022/test.txt'
my_path = 'C:/Users/G020772/data/AoC/input08.txt'

with open(my_path, 'r') as f:
    m =  np.array([list(map(int, l.strip())) for l in f])
 

tree_count = 0
for r in range(0, len(m)):
    for e in range(0, len(m[r])):
        if r == 0 or e == 0 or r == len(m)-1 or e == len(m[r])-1:
            tree_count += 1
        else:
            elem = m[r][e]
            check_row_left = min(np.less(m[r][:e], elem))
            check_row_right = min(np.less(m[r][e+1:], elem))
            check_col_up = min(np.less(m[:,e][:r], elem))
            check_col_down = min(np.less(m[:,e][r+1:], elem))

            if check_row_left or check_row_right or check_col_up or check_col_down:
                tree_count += 1

print("Trees:", tree_count)

# part II

def tree_scores(trees, hut_tree):
    score = 0
    for tree in trees:
        if hut_tree > tree:
            score += 1
        else:
            score += 1
            break
    return score

scenic_score = 0
for r in range(0, len(m)):
    for e in range(0, len(m[r])):
        if r == 0 or e == 0 or r == len(m)-1 or e == len(m[r])-1:
            continue
        else:
            elem = m[r][e]
    
            check_row_left = np.flip(m[r][:e])
            check_row_right = m[r][e+1:]
            check_col_up = np.flip(m[:,e][:r])
            check_col_down = m[:,e][r+1:]

            score_left = tree_scores(check_row_left, elem)
            score_right = tree_scores(check_row_right, elem)
            score_up = tree_scores(check_col_up, elem)
            score_down = tree_scores(check_col_down, elem)

            score_total = score_left * score_right * score_up * score_down
            if score_total > scenic_score:
                scenic_score = score_total

print("Highest scenic score:", scenic_score)