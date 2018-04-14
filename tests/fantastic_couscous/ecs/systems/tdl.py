# Fakes out the TDL class so we can import/use it.
tdl_calls = []
def flush():
    tdl_calls.append("flush")