from random import randint
import utils


def task_2(input_list, prob, k):
    if k > len(input_list):
        raise utils.WrongTaskInput("List doesn't have k elements")
    if k > len([p for p in prob if p != 0.0]):
        raise utils.WrongTaskInput("List doesn't have k elements with non-zero probability")

    splitted_list = [[] for _ in range(11)]
    for p, i in zip(prob, input_list):
        splitted_list[int(p*10)].append(i)

    result = []
    # exclude elements with zero probability and generate distribution
    indices = sum([[i] * i for i in range(1, 10) if splitted_list[i] != []], [])
    for _ in range(k):
        # include elements with 100% probability
        if splitted_list[10]:
            i, splitted_list[10] = utils.get_random(splitted_list[10])
        else:
            index = indices[randint(0, len(indices) - 1)]
            while not splitted_list[index]:
                while index in indices:
                    indices.remove(index)
                index = indices[randint(0, len(indices) - 1)]
            i, splitted_list[index] = utils.get_random(splitted_list[index])
        result.append(i)
    return result


def test_2(tests_count=10000):

    errors = 0

    for _ in range(tests_count):

        l, k = utils.get_input(max_size=256)
        p = [randint(0, 10) / 10 for _ in l]

        try:
            result = task_2(l, p, k)
        except utils.WrongTaskInput:
            pass
        else:
            try:
                l_nonzero_prob = [i for i, j in zip(l, p) if j != 0.0]
                if not utils.is_subset(result, l_nonzero_prob):
                    raise Exception("Result should consist of only elements with non-zero probability")
                l_one_prob = [i for i, j in zip(l, p) if j == 1.0]
                if k <= len(l_one_prob):
                    if not utils.is_subset(result, l_one_prob):
                        raise Exception("Result should be a subset of elements with probability one")
                else:
                    if not utils.is_subset(l_one_prob, result):
                        raise Exception("All elements with probability one should be in result")
            except Exception as e:
                print(f'task_2: {e}')
                print(f'l: {l}')
                print(f'k: {k}')
                print(f'result: {result}')
                print()
                errors += 1

    print(f'Failed tests: {errors}/{tests_count}')


if __name__ == '__main__':
    test_2()
