from collections import deque


class AnimalShelter:
    def __init__(self):
        self.dog_deq = deque()
        self.cat_deq = deque()

    def enqueue(self, animal_name, animal_kind):
        if animal_kind == 'dog':
            self.dog_deq.append(animal_name)
        elif animal_kind == 'cat':
            self.cat_deq.append(animal_name)

    def dequeue_dog(self):
        self.dog_deq.popleft()

    def dequeue_cat(self):
        self.cat_deq.popleft()

    def print(self):
        print('개:')
        for dog in self.dog_deq:
            print(f"\t{dog}")
        print('고양이:')
        for cat in self.cat_deq:
            print(f"\t{cat}")


if __name__ == "__main__":
    qs = AnimalShelter()
    qs.enqueue("밥", "cat")
    qs.enqueue("미아", "cat")
    qs.enqueue("요다", "dog")
    qs.enqueue("울프", "dog")
    qs.print()

    print("하나의 개와 고양이에 대해서 dequeue를 실행합니다.")
    qs.dequeue_dog()
    qs.dequeue_cat()
    qs.print()
