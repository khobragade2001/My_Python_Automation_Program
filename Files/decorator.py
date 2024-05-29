


def Decorator (fun):
    print("this is statement before main functions start==")
    fun()
    print("this is statement after main functions end ==")

def Main_fun():
    print("==== MAIN FUNCTION START ====")

## calling of functions =========================
var = Decorator(Main_fun)
print(var)

## using @decorator
@Decorator
def hello():
    print("==== MAIN FUN START USING @ DECORATOR ====")

