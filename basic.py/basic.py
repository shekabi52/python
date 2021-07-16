class animal:
    id=10
    def walk(self):
        print("i am walking")


class dog(animal):
    def bark(self):
        print("i am barking",animal.id)


class wolf(dog):
    def meat(self):
        print("i am carnivores")


def main():
    w=wolf()
    w.meat()
    w.walk()
    w.bark()

if __name__=="__main__":
    main()
