

class dictt(dict):

    def show(self) -> None:
        for k, v in self.items():
            print(f"{k} : {v}")