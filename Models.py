import numpy as np
import openai
from Reflection_examples import *
import pandas as pd
import matplotlib.pyplot as plt
API_KEY = "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"

def zero_shot(txt):
    """
    this function reflects the text txt by using zero shot prompt
    :param txt: msg to be reflected
    :return: the reflection of the txt
    """
    command1 = "Express the feeling from the sentence in other words: "
    command2 = "Change the sentence from first person to second person: "
    txt2 = zero_shot_helper(txt, command1)
    x = zero_shot_helper(txt2, command2)
    return x
def zero_shot_helper(txt, command):
    """
    A wrapper that helps to run the zero shot function
    :param txt: msg to be reflected
    :param command: a command that brought to the gpt 3 as a prompt input
    :return: the results of running gpt 3 with the prompt  on the txt
    """
    lam1 = lambda response: response.to_dict()['choices'][0]["text"]
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
    """
    this function reflects the text txt by using few shot prompt the example
    to the prompt took from Reflection_example.FEW_SHOTS_EXAMPLES
    :param txt: msg to be reflected
    :return: the reflection of the txt
    """
    lam1 = lambda response: response.to_dict()['choices'][0]["text"]
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
    """
    this function runs the reflection function on the values of the txt_dict
    and export it to a csv with an additional score column
    :param reflect_func: the function that made the reflection
    :param txt_dict: dict with the name of the class as a key and a list of
    sentences as value
    :return: None
    """
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
    """
    this function plots a histogram with the score of each model as a function
    of the class type
    :param lst: the lst that contains a tuple
    (class_name, zero_shots_avg_score, few_shots_svg_score)
    :param name: the title of the graph and the name of the saved png
    :return: None
    """
    key = (lambda tup: abs(tup[1] - tup[2]))
    lst = sorted(lst, key=key)
    df = pd.DataFrame()
    df["classes"] = [tup[0] for tup in lst]
    df["few shots"] = [tup[2] for tup in lst]
    df["zero shots"] = [tup[1] for tup in lst]
    df.plot.bar(x="classes", y=["few shots", "zero shots"])
    plt.xlabel('CLASSES', fontweight='bold')
    plt.ylabel('SCORE', fontweight='bold')
    plt.ylim(1, 5)
    plt.title(name)
    plt.rcParams.update({'font.size': 24})
    plt.rcParams["figure.figsize"] = (14,14)
    plt.xticks(rotation=30, ha='right')
    plt.savefig(name + ".png",bbox_inches='tight')
    plt.show()


def build_from_csv(path_zero, path_few):
    """
    build a list that contains tuples:
    (class_name, zero_shots_avg_score, few_shots_svg_score)
    :param path_zero: path to the zero_shot's scored csv
    :param path_few: path to the few_shot's scored csv
    :return: list of tuple as mention above
    """
    zero = pd.read_csv(path_zero)
    few = pd.read_csv(path_few)
    cols_zero = zero.columns[1:]
    cols_few = few.columns[1:]
    for col in cols_zero:
        if "score" in col:
            new_name = "_".join(col.split("_")[2:-1])
            zero[new_name] = zero[col]
        zero.drop(col, inplace=True, axis=1)
    for col in cols_few:
        if "score" in col:
            new_name = "_".join(col.split("_")[2:-1])
            few[new_name] = few[col]
        few.drop(col, inplace=True, axis=1)
    cols1 = zero.columns[1:]
    cols2 = few.columns[1:]
    cols = [(cols1[i],cols2[i]) for i in range(len(cols1))]
    lst = []
    for col1,col2 in cols:
        lst.append((col1, np.mean(zero[col1]), np.mean(few[col2])))
    print(np.mean([tup[1] for tup in lst]),np.mean([tup[2] for tup in lst]))
    return lst









if __name__ == '__main__':
    pass
    # make_a_test(zero_shot, REFLECTION_EXAMPLES_DICT_TEST)
    # make_a_test(few_shots, REFLECTION_EXAMPLES_DICT_TEST)
    # plot_histogram_precision(build_from_csv("zero_shot.csv", "few_shots.csv"), "Models Score per class - sorted by diff")





