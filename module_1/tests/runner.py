import unittest

import module_1.tests.euclidean as euclidean
import module_1.tests.classification as classification
import module_1.tests.fibonacci as fibonacci

loader = unittest.TestLoader()

eucSuite = unittest.TestSuite()
eucSuite.addTests(loader.loadTestsFromModule(euclidean))

gradeSuite = unittest.TestSuite()
gradeSuite.addTests(loader.loadTestsFromModule(classification))

fibSuite = unittest.TestSuite()
fibSuite.addTests(loader.loadTestsFromModule(fibonacci))

runner = unittest.TextTestRunner(verbosity=3, failfast=True)
runner.run(eucSuite)
runner.run(gradeSuite)
runner.run(fibSuite)
