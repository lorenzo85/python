from FsmTest import FsmTest

inputs = open("inputs.txt").readlines()
inputs = map(str.strip, inputs)

for i in inputs:
    print("------------------{0}------------------".format(i))
    test = FsmTest();
    test.runAll(list(i))
    print(": accepted={0}\n".format(test.isAccepted()))