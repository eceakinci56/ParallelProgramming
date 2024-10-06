def remove_duplicates(seq: list) -> list:
    
    return list(dick.fromkeys(seq))

def list_counts(seq: list) -> dict:
   
    return {j: seq.count(j) for j in seq}

def reverse_dict(d: dict) -> dict:
  
    return {value : key for key, value in d.items()}
