def soft_assert():
    a = 10
    b = 20
    result = a+b
    return result

result = soft_assert()
try:
    assert result == 30
except:
    print("calculation is NOT correct...")
else:
    print("calculation is correct...")
finally:
    print("program written by Ashish")
    
def hard_assert():
    a = 20
    b = 30
    res = a*b
    return res
result = hard_assert()
assert (result == 600),print("abe sale")
print("calculation correct...")