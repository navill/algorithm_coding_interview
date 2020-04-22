"""
먼저 들어온 동물(개 또는 고양이)이 먼저 나가는 동물 보호소
사람들은 가장 오래된 동물부터 입양할 수 있다.

class Aniaml
- Dog(Animal): dogs Queue에 저장된다
- Cat(Animal): cats Queue에 저장된다.

AnimalQueue: 두 개의 큐를 이용해 각각 고양이와 강아지를 저장한다.
- cats
- dogs
"""
from queue import Queue


class Animal:
    def __init__(self, name=None):
        self.name = name
        self.order = 0

    def is_older_than(self, a):
        return self.order < a.order


class Dog(Animal):
    def __init__(self, name=None):
        super().__init__(name)


class Cat(Animal):
    def __init__(self, name=None):
        super().__init__(name)


class AnimalQueue:
    dogs = Queue()
    cats = Queue()
    order = 0  # 오래된 동물을 판단하기 위해 사용될 order

    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if isinstance(animal, Dog):
            self.dogs.put(animal)
        else:
            self.cats.put(animal)

    def dequeue_any(self):
        if self.dogs.qsize() == 0:
            return self.dequeue_cats()
        elif self.cats.qsize() == 0:
            return self.dequeue_dogs()

        dog = self.dogs.queue[0]
        cat = self.cats.queue[0]

        # 고양이와 강아지 중 더 오래된 동물은?
        if dog.is_older_than(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()

    def dequeue_dogs(self):
        try:
            return self.dogs.get_nowait()
        except:
            # 강아지 큐가 비었을 경우 빈 Dog 객체 전달
            return Dog()

    def dequeue_cats(self):
        try:
            # get_nowait: queue가 있을 경우 값을 가져오고 없을 경우 기다리지 않고 task 종료->raise empty error
            # get: queue가 있을 경우 값을 가져오고 없을 경우 기다림
            return self.cats.get_nowait()
        except:
            # 고양이 큐가 비었을 경우 빈 Cat 객체 전달
            return Cat()


animals = AnimalQueue()
cat1 = Cat('cat1')
cat2 = Cat('cat2')
cat3 = Cat('cat3')
cat4 = Cat('cat4')

dog1 = Dog('dog1')
dog2 = Dog('dog2')
dog3 = Dog('dog3')
dog4 = Dog('dog4')

animals.enqueue(cat1)
animals.enqueue(cat2)
animals.enqueue(dog1)
animals.enqueue(cat3)
animals.enqueue(dog2)
animals.enqueue(cat4)
animals.enqueue(dog3)
animals.enqueue(dog4)

print(animals.dequeue_any().name)
print(animals.dequeue_dogs().name)
print(animals.dequeue_dogs().name)
print(animals.dequeue_dogs().name)
print(animals.dequeue_dogs().name)
print(animals.dequeue_dogs().name)
