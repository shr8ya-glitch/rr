nlarge=int(input("Enter the larger number:"))
nsmall=int(input("Enter the smaller number:"))
while (nsmall):
    nums=nsmall
    nsmall=nlarge%nsmall
    nlarge=nums
print("HCF is :",nlarge)