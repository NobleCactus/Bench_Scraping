
def create_practice_dict(practice_list):
    practice_dict = {}
    for i in practice_list:
        if i not in practice_dict.keys():
            practice_dict[i] = 1
        else:
            practice_dict[i] += 1

    return practice_dict
def get_most_practitioners(bench_total, practice_dict):
    highest = 0
    practice = ''
    for i in practice_dict.keys():
        if practice_dict[i] > highest:
            highest = practice_dict[i]
            practice = i

    return [practice, (highest/bench_total)*100]

def get_least_practitioners(bench_total, practice_dict):
    highest = 999999999
    practice = ''
    for i in practice_dict.keys():
        if practice_dict[i] < highest:
            highest = practice_dict[i]
            practice = i

    return [practice, (highest/bench_total)*100]