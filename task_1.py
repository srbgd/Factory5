import utils


def task_1(input_list, k):
    if k > len(input_list):
        raise utils.WrongTaskInput("List doesn't have k elements")
    result = []
    for _ in range(k):
        i, input_list = utils.get_random(input_list)
        result.append(i)
    return result


def test_1():
    for _ in range(10000):

        l, k = utils.get_input()

        try:
            result = task_1(l, k)
        except utils.WrongTaskInput:
            pass
        else:
            try:
                if not utils.is_subset(result, l):
                    raise Exception("Result has more equal elements than input list")
            except Exception as e:
                print(f'task_1: {e}')
                print(f'l: {l}')
                print(f'k: {k}')
                print(f'result: {result}')
                print()


if __name__ == '__main__':
    test_1()
