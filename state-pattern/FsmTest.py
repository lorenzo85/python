
from State import State
from StateMachine import StateMachine
import sys

class S1(State):
      def run(self):
          sys.stdout.write("S1 ")

      def next(self, input):
          if input == "a":
             return FsmTest.S2
          return FsmTest.S1

class S2(State):
      def run(self):
          sys.stdout.write("S2 ")

      def next(self, input):
          if input == "c":
             return FsmTest.S4
          if input == "b":
             return FsmTest.S1
          return FsmTest.S2

class S3(State):
      def run(self):
          sys.stdout.write("S3 ")

      def next(self, input):
          if input == "a":
             return FsmTest.S1
          if input == "b":
             return FsmTest.S4
          return FsmTest.S3

class S4(State):
      def run(self):
          sys.stdout.write("S4 ")

      def next(self, input):
          if input == "d":
             return FsmTest.S3
          return FsmTest.S4


class FsmTest(StateMachine):
      def __init__(self):
          StateMachine.__init__(self, S1(False))

FsmTest.S1 = S1(False)
FsmTest.S2 = S2(False)
FsmTest.S3 = S3(False)
FsmTest.S4 = S4(True)