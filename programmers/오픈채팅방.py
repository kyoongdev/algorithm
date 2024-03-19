# link : https://school.programmers.co.kr/learn/courses/30/lessons/42888


def solution(record):
    answer = []

    resultDict = {}
    for idx, re in enumerate(record):
        splitted = re.split(" ")
        if splitted[0] == "Enter":
            if splitted[1] in resultDict:
                resultDict[splitted[1]]["name"] = splitted[2]
                resultDict[splitted[1]]["info"].append([idx, "Enter"])
            else:
                resultDict[splitted[1]] = {"name": "", "info": []}
                resultDict[splitted[1]]["name"] = splitted[2]
                resultDict[splitted[1]]["info"] = [[idx, "Enter"]]

        elif splitted[0] == "Leave":
            resultDict[splitted[1]]["info"].append([idx, "Leave"])
        else:
            resultDict[splitted[1]]["name"] = splitted[2]

    # print(resultDict)
    result = []
    for key, value in resultDict.items():
        name = value["name"]
        info = value["info"]

        for inf in info:
            idx = inf[0]
            word = inf[1]
            hangul = ""
            if word == "Enter":
                hangul = "님이 들어왔습니다."
            elif word == "Leave":
                hangul = "님이 나갔습니다."
            result.append([idx, name + hangul])
    result.sort()
    # print(result)

    return [x[1] for x in result]
