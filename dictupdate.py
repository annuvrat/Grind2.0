scores = {
    "alice": 10,
    "bob": 20
}


def update_scores(new_scores):
    scores.update(new_scores)

new_scores = {
    "charlie": 30,
    "dave": 40
}
update_scores(new_scores)
print(scores)
