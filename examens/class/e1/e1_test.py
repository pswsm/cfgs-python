import pytest
from e1 import Seq, DNASeq, RNASeq, Protein


# #############################################################################
# IMPORTANT: YOU CANNOT CHANGE THIS FILE.
# #############################################################################


# #############################################################################
# Seq Class
# #############################################################################

# -----------------------------------------------------------------------------
def test_seq_constructor():

    s: Seq = Seq('GATAGATA')
    assert s.seq  == 'GATAGATA'
    assert str(s) == 'GATAGATA'
    assert len(s) == 8

# -----------------------------------------------------------------------------
def test_seq_from_fasta():

    s: Seq = Seq.from_fasta('data_dna.fasta')
    assert s.seq  == 'GATAGATA'
    assert str(s) == 'GATAGATA'
    assert len(s) == 8



# #############################################################################
# DNASeq Class
# #############################################################################

# -----------------------------------------------------------------------------
def test_dna_seq_constructor():

    s: DNASeq = DNASeq('GATAGATA')
    assert s.seq == 'GATAGATA'

    assert isinstance(s, Seq)
    assert isinstance(s, DNASeq)

# -----------------------------------------------------------------------------
def test_dna_seq_constructor_exception():

    with pytest.raises(Exception):
        s: DNASeq = DNASeq('UGUU')

# -----------------------------------------------------------------------------
def test_dna_seq_from_fasta():

    s: DNASeq = DNASeq.from_fasta('data_dna.fasta')
    assert s.seq == 'GATAGATA'

    assert isinstance(s, Seq)
    assert isinstance(s, DNASeq)

# -----------------------------------------------------------------------------
def test_dna_seq_transcribe():

    s: DNASeq = DNASeq('ATCG')
    assert s.transcribe() == 'AUCG'



# #############################################################################
# RNASeq Class
# #############################################################################

# -----------------------------------------------------------------------------
def test_rna_seq_constructor():

    s: RNASeq = RNASeq('AUG')
    assert s.seq == 'AUG'

    assert     isinstance(s, Seq)
    assert not isinstance(s, DNASeq)
    assert     isinstance(s, RNASeq)

# -----------------------------------------------------------------------------
def test_rna_seq_constructor_exception():

    with pytest.raises(Exception):
        RNASeq('ATTA')

# -----------------------------------------------------------------------------
def test_rna_seq_from_fasta():

    s: RNASeq = RNASeq.from_fasta('data_rna.fasta')
    assert s.seq == 'AUUAAUUA'

    with pytest.raises(Exception):
        RNASeq.from_fasta('data_dna.fasta')

    assert     isinstance(s, Seq)
    assert not isinstance(s, DNASeq)
    assert     isinstance(s, RNASeq)

# -----------------------------------------------------------------------------
def test_rna_seq_translate():

    s: RNASeq = RNASeq('AUGGAUAAAUUCUAA')
    assert s.translate() == 'MDKF*'

    with pytest.raises(Exception):
        RNASeq('AU').translate()



# #############################################################################
# Protein Class
# #############################################################################

# -----------------------------------------------------------------------------
def test_protein_constructor():

    s: Protein = Protein('KIRAVINE')
    assert s.seq == 'KIRAVINE'

    assert     isinstance(s, Seq)
    assert not isinstance(s, DNASeq)
    assert not isinstance(s, RNASeq)
    assert     isinstance(s, Protein)

# -----------------------------------------------------------------------------
def test_protein_constructor_exception():

    with pytest.raises(Exception):
        s: Protein = Protein('ÇÑ')

# -----------------------------------------------------------------------------
def test_protein_from_fasta():

    s: Protein = Protein.from_fasta('data_protein.fasta')
    assert s.seq == 'ARNDCEQGHILKMFPSTWYV'

    with pytest.raises(Exception):
        Protein.from_fasta('data_rna.fasta')

    assert     isinstance(s, Seq)
    assert not isinstance(s, DNASeq)
    assert not isinstance(s, RNASeq)
    assert     isinstance(s, Protein)

# -----------------------------------------------------------------------------
