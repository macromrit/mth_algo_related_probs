def is_valid_state(state):
    #check if it's a valid solution
    return True

def get_candidates(state):
    return list()

def search(state, solutions):
    if is_valid_state(state):
      solutions.append(state.copy)
      #if a single solution's fine ->
      # return
    else: pass
  
    for candidate in get_candidates(state):
        state.add(candidate)
        search(state, solutions)
        state.remove(candidate)
 
def solve():
    solutions = list()
    state = set()
    search(state, solutions)
    return solutions
   
  
   
