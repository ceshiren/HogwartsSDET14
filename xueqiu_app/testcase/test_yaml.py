import yaml


def test_yaml():
    with open("../page/main.yaml") as f:
        steps = yaml.safe_load(f)
    for step in steps:
        if "action" in step.keys():
            action = step["action"]
            if "click" == action:
                print("find(xxx).click()")
