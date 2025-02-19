### Отчёт по лабораторной работе по предмету Объектно-ориентированное программирование
#### Хатуаева Дайана Тныбековна
#### ПИЖ-б-о-23-2(1)
#### Вариант 6
<hr>

# Цель работы
Цель данной работы заключается в ознакомлении с особенностями объектно-ориентированного программирования
в общем и его реализацией в языке *Python* на примере задачи.

# Задание
Класс Снежинка (SnowFlake)  
При инициализации класс принимает целое нечётное число - сторону квадрата, в  который вписана снежинка. 
***Методы***: 
- thaw() - таять, при этом на каждом шаге пропадают крайние звездочки со всех сторон; параметр показывает, сколько шагов прошло. 
- freeze(n) - намораживаться, при этом сторона квадрата, в который вписана снежинка, увеличивается на 2*n, одновременно добавляются звездочки в нужных местах, чтобы правило соблюдалось. 
- thicken() - утолщаться, ко всем линиям звёздочек с двух сторон добавляются 
параллельные (если перед этим снежинка таяла, то теперь звёздочки восстанавливаются). 
- show() - показывать (рисуется снежинка в виде квадратной матрицы со звездочками и дефисами в пустых местах).

# Выполнение лабораторной работы
В ходе выполнения лабораторной работы был создан класс **SnowFlakes**, который включает в себя методы, указанные выше.  
Инициализация (класс принимает нечётное число, которые служит для определения стороны квадрата и матрицы):

```python
def __init__(self, n):
        self.n = n
        self.s = [['-' for i in range(n)] for j in range(n)]
        for i in range(n):
            self.s[i][i] = '*'
            self.s[i][n - i - 1] = '*'
            self.s[i][n // 2] = '*'
            self.s[n // 2][i] = "*"
```
Метод ***thaw()*** позволяет снежинке "таять", уменьшая значение сторон квадрата:
```python
def thaw(self, steps):
        new_size = self.n - steps
        self.s = [['-' for i in range(new_size)] for j in range(new_size)]
        for i in range(new_size):
            self.s[i][i] = '*'
            self.s[i][new_size - i - 1] = '*'
            self.s[i][new_size // 2] = '*'
            self.s[new_size // 2][i] = "*"
```
Метод ***freeze(n)*** отвечает за то, чтобы размер снежинки увеличивался в k-раз:
```python
def freeze(self, k):
        new_size = self.n * k
        self.s = [['-' for i in range(new_size)] for j in range(new_size)]
        for i in range(new_size):
            self.s[i][i] = '*'
            self.s[i][new_size - i - 1] = '*'
            self.s[i][new_size // 2] = '*'
            self.s[new_size // 2][i] = "*"
```
Метод ***thicken()*** работает противоположно методу thaw(). Он позволяет добавлять звёздочки к диагоналям и главным осям:
```python
def thicken(self, steps):
        new_n = self.n + steps
        self.s = [['-' for i in range(new_n)] for j in range(new_n)]
        for i in range(new_n):
            self.s[i][i] = '*'
            self.s[i][new_n - i - 1] = '*'
            self.s[i][new_n // 2] = '*'
            self.s[new_n // 2][i] = "*"
```
Последний метод ***show()*** отображает получившуюся снежинку c поомщью цикла for:
```python
def show(self):
        for i in self.s:
            print("".join(i))
```

# Выводы
По итогу проделанной работы можно  сказать, что мы применили знания, полученные на прошлом занятии, для реализации данного кода и получили класс, который позволяет создавать снежинку и изменять её размер.