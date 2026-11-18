# Logic-1: cigar_party

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    return 40 <= cigars <= 60
  
