'''
Задачка: Написать функцию, которая принимает список целых чисел 
и возвращает новый список, содержащий только нечётные числа из 
исходного списка, возведённые в квадрат. 
Используйте конструкцию List Comprehension.
'''
def get_squared_odds(numbers):
    """ Your code Here """
    squared_odds = []
    return squared_odds


def test_get_squared_odds():
    assert get_squared_odds([1, 2, 3, 4, 5]) == [1, 9, 25]
    assert get_squared_odds([0, 2, 4, 6, 8]) == []
    assert get_squared_odds([1, 3, 5, 7, 9]) == [1, 9, 25, 49, 81]
    assert get_squared_odds([-1, -2, -3, -4, -5]) == [1, 9, 25]
    assert get_squared_odds([2, 4, 6, 7, 8, 9]) == [49, 81]

    
 

if __name__ == '__main__':
    test_get_squared_odds()
