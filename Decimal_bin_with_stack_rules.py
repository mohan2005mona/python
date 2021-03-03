class Stack:
    def __init__(self):
        self.elements=[]
        self.binary=[]
        self.dict={}
    def push(self,digit):
        self.elements.append(digit)
    def pop(self):
        del self.elements[-1]
    def peek(self):
        return self.elements[-1]
    def is_empty(self):
        return self.elements == []

class Binary(Stack):
    def check_Binary(self,var):
        # This variable is used to append to dictionery, as var would be zero at the end of opeartion
        v=var
        # this section is for binary representation
        while var > 0:
            digit = var % 2
            self.push(digit)
            var = int(var / 2)
        concat=''
        # This section is used for converting List variables to form the binary number
        if not self.is_empty():
            for i in range(len(self.elements)):
                concat = concat + str(self.peek())
                self.pop()
            self.binary.append(concat)
            self.dict[v]=concat
def main():
    series = [
        21, #10101
        15, #1111
        11, #1011
        111
    ]
    Bin_Conversion = Binary()
    for var in series:
        Bin_Conversion.check_Binary(var)
    print("Final Binary in dictionary :",Bin_Conversion.dict)
    print("\n Binary value in List",Bin_Conversion.binary)

if __name__ == '__main__':
    main()
