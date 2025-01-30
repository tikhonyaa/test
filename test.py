# Вопрос №1: Алгоритм определения четности числа

# Классическая проверка через остаток от деления
def isEven1(value): # + Простой алгоритм, работает во всех случаях, упрощяет читаемость
    return value % 2 == 0 # - В некоторых случаях работает медленее для больших объемов данных или для низкоуровневых систем

# Альтернативная проверка через побитовую операцию
def isEven2(value): # + Работает быстрее деления, особенно для низкоуровневых систем
    return (value & 1) == 0 # - Усложняет читаемость кода


# Вопрос №2: Реализация циклического буфера FIFO

# 1-я реализация с использованием списка
class CircularBuffer1: # + Простой и гибкий способ, адаптирующийся под разные требования и задачи
    def __init__(self, size): # - Неэффективен для больших данных (pop(0) сдвигает все элементы), так как снижена производиттельность 
        self.size = size
        self.buffer = []

    def enqueue(self, item):
        if len(self.buffer) == self.size:
            self.buffer.pop(0)
        self.buffer.append(item)

    def dequeue(self):
        if len(self.buffer) == 0:
            return None
        return self.buffer.pop(0)

    def peek(self):
        return self.buffer[0] if self.buffer else None

# 2-я реализация с использованием deque
from collections import deque

class CircularBuffer2: # + Времязатраты O(1) в отличие от O(n) предыдущего алгоритма, maxlen позволяет ограничивать размер буфера
    def __init__(self, size): # - Зависимость от сторонней библиотеки, менее гибкий для других структур данных
        self.size = size
        self.buffer = deque(maxlen=size)

    def enqueue(self, item):
        self.buffer.append(item)

    def dequeue(self):
        if len(self.buffer) == 0:
            return None
        return self.buffer.popleft()

    def peek(self):
        return self.buffer[0] if self.buffer else None


# Вопрос №3: Алгоритм быстрой сортировки

def quicksort(arr): # + Высокая средняя скорость (O(n log n)), стандартный алгоритм, не требующий дополнительных библиотек, имеет рекурсивную структуру, для больших массивов
    if len(arr) <= 1: # можно оптимизировать при помощи опорного элемента или медианы
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


# Пример использования и тестирования

def test_isEven():
    print("Тестирование функции isEven:")
    print(isEven1(4))  # Ожидаем True
    print(isEven1(5))  # Ожидаем False
    print(isEven2(4))  # Ожидаем True
    print(isEven2(5))  # Ожидаем False

def test_circular_buffers():
    print("\nТестирование циклических буферов:")

    # Тестируем CircularBuffer1
    buffer1 = CircularBuffer1(3)
    buffer1.enqueue(1)
    buffer1.enqueue(2)
    buffer1.enqueue(3)
    buffer1.enqueue(4)  # Ожидаем, что 1 будет удален
    print(f"Buffer1 (enqueue): {buffer1.buffer}")
    print(f"Dequeue Buffer1: {buffer1.dequeue()}")
    print(f"Buffer1 после dequeue: {buffer1.buffer}")

    # Тестируем CircularBuffer2
    buffer2 = CircularBuffer2(3)
    buffer2.enqueue(1)
    buffer2.enqueue(2)
    buffer2.enqueue(3)
    buffer2.enqueue(4)  # Ожидаем, что 1 будет удален
    print(f"Buffer2 (enqueue): {list(buffer2.buffer)}")
    print(f"Dequeue Buffer2: {buffer2.dequeue()}")
    print(f"Buffer2 после dequeue: {list(buffer2.buffer)}")

def test_quick_sort():
    print("\nТестирование QuickSort:")
    arr = [10, 7, 8, 9, 1, 5]
    print(f"Исходный массив: {arr}")
    sorted_arr = quicksort(arr)
    print(f"Отсортированный массив: {sorted_arr}")


# Запуск всех тестов
test_isEven()
test_circular_buffers()
test_quick_sort()

