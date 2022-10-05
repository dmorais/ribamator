from dataclasses import dataclass, field
import random
import pickle
import os.path

@dataclass
class makeMarkovModel:
    clean_txt: list = field(repr=False)
    n_gram: int = field(repr=False)
    markov_model: dict = field(init=False)


    def __post_init__(self) -> None:
        self.markov_model = self._make_model()

    def _make_model(self) -> dict:
        m_model: dict = {}

        for i in range(len(self.clean_txt) - self.n_gram - 1):
            curr_state, next_state = "", ""
            for j in range(self.n_gram):
                curr_state += self.clean_txt[i + j] + " "
                next_state += self.clean_txt[ i + j + self.n_gram] + " "
            curr_state = curr_state[:-1]
            next_state = next_state[:-1]

            if curr_state not in m_model:
                m_model[curr_state] = {}
                m_model[curr_state][next_state] = 1
            else:
                if next_state in m_model[curr_state]:
                    m_model[curr_state][next_state] += 1
                else:
                   m_model[curr_state][next_state] = 1

        # calculating transition probabilities
        for curr_state, transition in m_model.items():
            total = sum(transition.values())
            for state, count in transition.items():
                m_model[curr_state][state] = count/total

        return m_model


    @staticmethod
    def generate_text(markov_model:dict, limit = 100, start='o nordeste' ) -> str:
        n = 0
        curr_state = start
        next_state = None
        story=""

        story += curr_state + " "
        while n < limit:
            next_state = random.choices(list(markov_model[curr_state].keys()),
                                        list(markov_model[curr_state].values()))

            curr_state = next_state[0]
            story += curr_state + " "
            n += 1

        return story


    def save_model(self, dir:str, type: str) -> int:
        with open(os.path.join(dir, type + ".pkl"), 'wb') as f:
            pickle.dump(self.markov_model, f)

            return 0


    @staticmethod
    def load_model(dir:str, type:str) -> dict:
        with open(os.path.join(dir, type + ".pkl"), 'rb') as f:
            return pickle.load(f)


    @staticmethod
    def save_updated_model(model:dict, type: str, dir:str) -> int:
        with open(os.path.join(dir, type + ".pkl"), 'wb') as f:
            pickle.dump(model, f)

            return 0