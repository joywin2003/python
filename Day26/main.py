dic = {
    "names": ["joy", "jos", "chris", "canon"],
    "scores": [23, 34, 67, 34]

}
import pandas

student_scores = pandas.DataFrame(dic)
# print(student_scores)

for (ix, row) in student_scores.iterrows():
    print(ix)
