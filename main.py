class SnowFlakes:
    """
    Класс для создания и управления снежинками в виде квадратной матрицы.

    Атрибуты:
    - n (int): Размер стороны матрицы снежинки.
    - s (list): Матрица, представляющая снежинку.

    Методы:
    - __init__(self, n): Инициализирует снежинку с размером n.
    - thaw(self, steps): Уменьшает размер снежинки на это количество шагов.
    - freeze(self, k): Увеличивает размер снежинки в k раз.
    - thicken(self, steps): Увеличивает толщину на указанное количество шагов.
    - show(self): Выводит снежинку на экран.
    """

    def __init__(self, n):
        """
        Инициализирует снежинку с размером n.
        Параметры:
        - n (int): Размер стороны матрицы снежинки.
        """
        self.n = n
        self.s = [['-' for i in range(n)] for j in range(n)]
        for i in range(n):
            self.s[i][i] = '*'
            self.s[i][n - i - 1] = '*'
            self.s[i][n // 2] = '*'
            self.s[n // 2][i] = "*"

    def thaw(self, steps):
        """
        Уменьшает размер снежинки на указанное количество шагов.
        Параметры:
        - steps (int): Количество шагов, на которое уменьшается снежинка.
        """
        new_size = self.n - steps
        self.s = [['-' for i in range(new_size)] for j in range(new_size)]
        for i in range(new_size):
            self.s[i][i] = '*'
            self.s[i][new_size - i - 1] = '*'
            self.s[i][new_size // 2] = '*'
            self.s[new_size // 2][i] = "*"

    def freeze(self, k):
        """
        Увеличивает размер снежинки в k раз.
        Параметры:
        - k (int): Коэффициент увеличения размера снежинки.
        """
        new_size = self.n * k
        self.s = [['-' for i in range(new_size)] for j in range(new_size)]
        for i in range(new_size):
            self.s[i][i] = '*'
            self.s[i][new_size - i - 1] = '*'
            self.s[i][new_size // 2] = '*'
            self.s[new_size // 2][i] = "*"

    def thicken(self, steps):
        """
        Увеличивает толщину снежинки на указанное количество шагов.
        Параметры:
        - steps (int): Количество шагов, на которое увеличивается толщина.
        """
        new_n = self.n + steps
        self.s = [['-' for i in range(new_n)] for j in range(new_n)]
        for i in range(new_n):
            self.s[i][i] = '*'
            self.s[i][new_n - i - 1] = '*'
            self.s[i][new_n // 2] = '*'
            self.s[new_n // 2][i] = "*"

    def show(self):
        """
        Выводит снежинку на экран.
        """
        for i in self.s:
            print("".join(i))
