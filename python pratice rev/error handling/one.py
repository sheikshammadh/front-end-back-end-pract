# from insufficientbal import InsuffientBalErr

# amount=int(input("Enter Amount:"))
# acc_Bal = 15000

# if acc_Bal < amount:
#     #print("Low Balance")
#     raise InsuffientBalErr("Low Balance")
# else:
#     print("Withdrawl and Enjoy")

from insufficientbal import InsuffientBalErr as balerror

# acc_bal=500
# try:
#     amount=int(input("Enter Amount:"))
#     if acc_bal<amount:
#         raise balerror("low balance, please check")
#     else:
#         print("withdraw and enjoy")
# except balerror as err:
#     print("balance error")
# finally:
#     print("check default error")
# print("gm")

try:
    print(10/0)

except ZeroDivisionError as error:
    print(error)
