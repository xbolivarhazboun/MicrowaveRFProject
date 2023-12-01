class ReactiveComponent:
    def __init__(self, value: float):
        self.value = value

    def __str__(self):
        return f"{self.value}"


class Inductor(ReactiveComponent):
    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f"{self.value}"


class Capacitor(ReactiveComponent):
    def __init__(self, value: float):
        super().__init__(value)

    def __str__(self):
        return f"{self.value}"
