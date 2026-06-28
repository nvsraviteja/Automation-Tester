def log_failed_tests(*test_ids):
    for n in test_ids:
        print(n)


test = log_failed_tests("TC101", "TC205", "TC999")


def show_bug_details(**bug):
    dic = {}
    for key,value in bug.items():
        dic[key] = value
    return dic

tt = show_bug_details(id="BUG101", severity="High", status="Open")
print (tt)


players = [
    ("Ravi", 80),
    ("Teja", 95),
    ("Sai", 70)
]

print(sorted(players, key=lambda player: player[0]))

