class Feature:
    def __init__(self, identity: str) -> None:
        self.identity = identity

    def print(self):
        print(f"Feature {self.identity}")


print("Hello World")
Feature("A").print()
Feature("B").print()
