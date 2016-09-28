from WasRun import *


class TestCaseTest(TestCase):

    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert self.test.wasRun

    def testSetup(self):
        self.test.run()
        assert self.test.wasSetUp