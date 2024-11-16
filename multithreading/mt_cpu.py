# multi-threading with computational operations

import threading

class NS_APP:
    # NS_APP.print("Thread 1", text="Hello!")
    # NS_APP.print("Thread 2", numeric=108)
    def display(prompt_text, **kwargs):
        if list(kwargs.keys()) in ["text", "numeric"]:
            try:
                s = prompt_text + kwargs["str"]
            except KeyError as ke:
                s = prompt_text + repr(kwargs["num"])
            finally:
                print(s)
        else:
            print("ERROR: Check function display!")


def isPrime(candidate_num):
    if candidate_num in [1,2]:
        retval = True
    else:
        retval = True
        for divisor in range(3, candidate_num+1, 2):
            if candidate_num%divisor == 0:
                retval = False
                break
    
    return retval

def find_primes_in_range(start_num, end_num):
    lst_primes = []
    for x in range (start_num, end_num+1, 1):
        if isPrime(x):
            pass

# Main code
if __name__ == '__main__':
    pass