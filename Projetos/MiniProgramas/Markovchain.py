import random
import re
from collections import defaultdict
import pickle

class MarkovChainTextComposer:
    def __init__(self):
        self.chain = defaultdict(list)

    def tokenize(self, text):
        """Tokeniza o texto, preservando pontuações e símbolos."""
        return re.findall(r'\w+|[^\w\s]', text)

    def train(self, text, n=2):
        """Treina a cadeia de Markov com base no texto fornecido, usando n-gramas."""
        words = self.tokenize(text)
        
        if len(words) <= n:  # Caso o texto seja muito curto para gerar n-gramas
            raise ValueError("O texto fornecido é muito curto para a construção de n-gramas.")
        
        # Cria as cadeias de Markov de n-gramas
        for i in range(len(words) - n):
            key = tuple(words[i:i+n])  # n-gramas como chave
            self.chain[key].append(words[i + n])

    def generate(self, length=50, seed=None):
        """Gera texto a partir de um seed opcional (ou aleatório), com probabilidade baseada em frequências."""
        if seed is not None:
            seed_words = tuple(seed.split())
            if seed_words not in self.chain:
                raise ValueError(f"Seed '{seed}' não encontrado no modelo treinado.")
        else:
            seed_words = random.choice(list(self.chain.keys()))

        output = list(seed_words)
        
        for _ in range(length - len(seed_words)):
            current_state = tuple(output[-len(seed_words):])  # Últimos n-gramas
            next_word_options = self.chain.get(current_state)

            if not next_word_options:  # Se não houver palavras seguintes, reinicia
                break

            # Escolhe a próxima palavra com base nas frequências (probabilidades)
            next_word = random.choices(
                next_word_options, 
                weights=[next_word_options.count(w) for w in next_word_options]
            )[0]
            output.append(next_word)

            # Insere uma quebra de linha após ponto final
            if next_word in {'.', '!', '?'}:
                output.append('\n')

        return ' '.join(output)

    def save_model(self, filepath):
        """Salva a cadeia de Markov em um arquivo para uso futuro."""
        with open(filepath, 'wb') as f:
            pickle.dump(self.chain, f)

    def load_model(self, filepath):
        """Carrega a cadeia de Markov de um arquivo salvo."""
        with open(filepath, 'rb') as f:
            self.chain = pickle.load(f)

# Exemplo de uso:

# Texto de exemplo
text = """Markov chains are a mathematical system that undergoes transitions from one state to another 
according to certain probabilistic rules. The next state is dependent only on the current state, 
not the sequence of events that preceded it."""

# Inicializa o compositor
composer = MarkovChainTextComposer()

# Treina o modelo com o texto de exemplo
composer.train(text, n=2)  # Utiliza bigramas (n=2)

# Gera um texto novo com 50 palavras
generated_text = composer.generate(length=50)
print("Texto gerado:\n", generated_text)

# Gera texto com uma seed específica
generated_with_seed = composer.generate(length=50, seed="Markov chains")
print("\nTexto gerado com seed:\n", generated_with_seed)

# Salva o modelo treinado
composer.save_model("markov_chain_model.pkl")

# Carrega o modelo salvo
composer.load_model("markov_chain_model.pkl")

# Gera texto com o modelo carregado
generated_from_loaded_model = composer.generate(length=50)
print("\nTexto gerado após carregar o modelo salvo:\n", generated_from_loaded_model)
