class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def run(self):
        # result.testStarted()
        self.setUp()
        method = getattr(self, self.name)
        method()
        self.tearDown()


