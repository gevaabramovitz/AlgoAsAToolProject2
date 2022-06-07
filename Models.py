import numpy as np
import openai
from Reflection_examples import *
import pandas as pd
import matplotlib.pyplot as plt
API_KEY = "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"

def zero_shot(txt):
    command1 = "Express the feeling from the sentence in other words: "
    command2 = "Change the sentence from first person to second person: "
    txt2 = zero_shot_helper(txt, command1)
    x = zero_shot_helper(txt2, command2)
    return x
def zero_shot_helper(txt, command):
    lam1 = lambda response: response.to_dict()['choices'][0]["text"][2:]
    openai.api_key = API_KEY
    response = openai.Completion.create(
    engine="text-davinci-001",
    prompt= command + txt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6)
    return lam1(response)

def few_shots(txt):
    lam1 = lambda response: response.to_dict()['choices'][0]["text"][2:]
    openai.api_key = API_KEY
    content = ""
    for t1,t2 in FEW_SHOTS_EXAMPLES:
        content += f"\n Sentence: {t1} => Reflection: {t2}"

    prompt = f"make a psychology reflection: \n {content}\n Sentence: {txt} => Reflection: "
    response = openai.Completion.create(
        engine="text-davinci-001",
        prompt= prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6)
    return lam1(response)
def make_a_test(reflect_func, txt_dict):
    name  = reflect_func.__name__
    df = pd.DataFrame()
    for key, val in txt_dict.items():
        lst = []
        for sen in val:
            lst.append(reflect_func(sen))
        df[name + '_'+key] = val
        df[name + '_'+key + "_reflection"] = lst
        df[name + '_'+key + "_score"] = [""]*10
    df.to_csv(name + ".csv")

def plot_histogram_precision(lst, name):
    key = (lambda tup: abs(tup[1] - tup[2]))
    lst = sorted(lst, key=key)
    df = pd.DataFrame()
    df["classes"] = [tup[0] for tup in lst]
    df["few shots"] = [tup[2] for tup in lst]
    df["zero shots"] = [tup[1] for tup in lst]
    df.plot.bar(x="classes", y=["few shots", "zero shots"])
    plt.xlabel('classes', fontweight='bold')
    plt.ylabel('PERCENTAGE', fontweight='bold')
    plt.ylim(0, 100)
    plt.title(name)
    plt.rcParams.update({'font.size': 24})
    plt.rcParams["figure.figsize"] = (14,14)
    plt.xticks(rotation=30, ha='right')
    plt.savefig(name + ".png",bbox_inches='tight')
    plt.show()


def build_from_csv(path_zero, path_few):
    zero = pd.read_csv(path_zero())
    few = pd.read_csv(path_few())
    cols_zero = zero.columnes()[1:]
    cols_few = zero.columnes()[1:]
    for col in cols_zero:
        if "score" in col:
            new_name = "".join(col.split("_")[1:-1])
            zero[new_name] = zero[col]
            del zero[col]
    for col in cols_few:
        if "score" in col:
            new_name = "".join(col.split("_")[1:-1])
            few[new_name] = few[col]
            del zero[col]
    cols = zero.columnes()[1:]
    lst = []
    for col in cols:
        lst.append((col, np.mean(zero[col]), np.mean(few[col])))
    return lst









if __name__ == '__main__':
    # make_a_test(zero_shot, REFLECTION_EXAMPLES_DICT_TEST)
    make_a_test(few_shots, REFLECTION_EXAMPLES_DICT_TEST)
    # plot_histogram_precision(build_from_csv("zero_shot.csv", "few_shots.csv"), "Models Score per class - sorted by diff")
    # print(few_shots(txt3))
    # print(zero_shot(txt1, command2))
    # print(zero_shot_helper("", "Make list of different sentences that include emotions and the reason for them"))
    # print(zero_shot_helper("", "Make a list of different emotions"))



