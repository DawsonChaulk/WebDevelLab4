midterms = { "CP1520": [77, 83, 99], "CP1890": [57,79,82] }
print(list(midterms.values())[1][1])
midterms["CP2800"] = [86,77]
midterms["CP2800"].append(90)
print(midterms)
averages= {}
for key, value in midterms.items():
    averages[key] = int((sum(value)/len(value)))
print(averages)
