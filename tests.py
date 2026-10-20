from stress_analyzer import *
assert score_pss([0]*10) == 16          # reverse items give 4 each
assert score_pss([4,4,4,0,0,4,0,0,4,4]) == 40
assert score_pss([0,0,0,4,4,0,4,4,0,0]) == 0
assert categorize(13)=="Low Stress" and categorize(14)=="Moderate Stress" and categorize(27)=="High Stress"
assert stress_index(20)==50.0
print("All tests passed")
