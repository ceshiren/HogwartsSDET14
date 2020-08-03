import yaml


def test_yaml():
    with open("../page/main.yaml") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "action" in step.keys():
            action = step["action"]
            if "click" == action:
                print("find(xxx).click()")

def test_replace():
    a = {"stock_name": "alibaba", "xxx": 1234}
    b = "xxxxxxxxxxxxxx${stock_name}xxxxxx"
    for key, value in a.items():
        b = b.replace('${' + key + '}', repr(value))
    print(b)

    a = '${' + "stock_name" + '}'
    print(a)