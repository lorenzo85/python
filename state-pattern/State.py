
class State:
      def __init__(self, final):
          self.final = final

      def run(self):
          assert 0, "Run not implemented"

      def next(self, action):
          assert 0, "Next not implemented"
          
      def isAccepted(self):
          return self.final