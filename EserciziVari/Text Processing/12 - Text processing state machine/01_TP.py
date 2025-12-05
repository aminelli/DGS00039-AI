class StateMachine:

    # Initialize
    def start(self):
        self.state = self.startState

# Step through the input
    def step(self, inp):
        (s, o) = self.getNextValues(self.state, inp)
        self.state = s
        return o

# Loop through the input
    def feeder(self, inputs):
        self.start()
        return [self.step(inp) for inp in inputs]

# Determine the TRUE or FALSE state


class TextSeq(StateMachine):
    startState = 0

    def getNextValues(self, state, inp):
        if state == 0 and inp == 'A':
            return (1, True)
        elif state == 1 and inp == 'G':
            return (2, True)
        elif state == 2 and inp == 'C':
            return (0, True)
        else:
            return (3, False)


InSeq = TextSeq()

x = InSeq.feeder(['A', 'A', 'A'])
print(x)

y = InSeq.feeder(['A', 'G', 'C', 'A', 'C', 'A', 'G'])
print(y)
