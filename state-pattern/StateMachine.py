
import sys

class StateMachine:

      def __init__(self, state):
          self.state = state
          self.state.run()

      def runAll(self, inputs):
          for i in inputs:
              sys.stdout.write(i)
              sys.stdout.write(" ")
              self.state = self.state.next(i)
              self.state.run()
              
      def isAccepted(self):
          return self.state.isAccepted()