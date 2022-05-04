import utils
from pathlib import Path


# Student name: WRITE YOUR NAME BELOW
# -----------------------------------------------------------------------------
name:    str = "Pau"
surname: str = "Figueras"
assert name and surname, 'Error: Please write your name and surname.'
# -----------------------------------------------------------------------------

# E1
# -----------------------------------------------------------------------------
# 1. Fes quatre classes: Seq, DNASeq, RNASeq, Protein.
# 2. DNASeq, RNASeq i Protein han d'heretar de Seq.
# 3. Codifica els atributs i els mètodes necessaris per tal que
#   passin tots els tests que hi ha a l'arxiu 'e1_test.py'.
# 4. Executeu els tests amb l'ordre: pytest -v
# 5. A l'arxiu 'utils.py' teniu codi que us pot ajudar.
# 6. Tot el codi ha d'estar a les classes o a utils.py.
# 7. En cap cas poseu codi a la secció Main. Us donarà problemes en executar pytest.
# -----------------------------------------------------------------------------


# Classes
# -----------------------------------------------------------------------------
# WRITE YOUR CODE HERE

class Seq:
    def __init__(self, s: str):
        self.seq: str = s
        if 'u' in s.lower():
            raise Exception

    @classmethod
    def from_fasta(cls, file: str):
        lines: list[str] = Path(file).read_text().splitlines()
        s: str = ""
        for line in lines:
            if not line.startswith(">"):
                s = s + line

        return cls(s)

    def __str__(self) -> str:
        return f"{self.seq}"

    def __len__(self):
        return len(self.seq)

class Protein(Seq):
    def __init__(self, s: str):
        for c in range(len(s)):
            if s[c] not in utils.AA_LETTERS:
                raise Exception
        super().__init__(s)


class RNASeq(Seq):
    def __init__(self, s: str):
        if 't' in s.lower():
            raise Exception
        no_u: str = s.lower().replace('u', 't').upper()
        super().__init__(no_u)
        self.seq = self.seq.replace('T', 'U')

    def translate(self):
        groups: list[str] = [(self.seq[i:i+3]) for i in range(0, len(self.seq), 3)]
        aas: str = ""
        for group in groups:
            aas = aas + f"{utils.AMINO[group]}"
        return aas
  
class DNASeq(Seq):
    def __init__(self, s: str):
        super().__init__(s)

    def transcribe(self) -> str:
        return self.seq.lower().replace('t', 'u').upper()


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":

    pass
    # Write your solution inside classes.
    # Code here is NOT evaluated.

# -----------------------------------------------------------------------------
