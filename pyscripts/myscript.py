import random
import string


def generate_random_sentence():
    subjects = ["The cat", "A robot", "My neighbor", "The code", "An alien"]
    verbs = ["jumps", "calculates", "dances", "whispers", "runs"]
    objects = ["over a fence", "a secret", "the matrix", "in the rain", "through space"]
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}."


def generate_random_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))


def main():
    print("Random sentence:")
    print(generate_random_sentence())
    print()
    print("Random number between 1 and 100:", random.randint(1, 100))
    print("Random password:", generate_random_password(14))


if __name__ == "__main__":
    main()