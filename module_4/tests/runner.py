import unittest

import module_4.tests as tests

loader = unittest.TestLoader()

arrayEqualSuite = unittest.TestSuite()
arrayEqualSuite.addTests(loader.loadTestsFromModule(tests.arrayEqual))

arraySortedSuite = unittest.TestSuite()
arraySortedSuite.addTests(loader.loadTestsFromModule(tests.arraySorted))

arraySumSuite = unittest.TestSuite()
arraySumSuite.addTests(loader.loadTestsFromModule(tests.arraySum))

longestStringSuite = unittest.TestSuite()
longestStringSuite.addTests(loader.loadTestsFromModule(tests.longestString))

toCamelCaseSuite = unittest.TestSuite()
toCamelCaseSuite.addTests(loader.loadTestsFromModule(tests.toCamelCase))

runner = unittest.TextTestRunner(verbosity=3, failfast=True)
runner.run(arrayEqualSuite)
runner.run(arraySortedSuite)
runner.run(arraySumSuite)
runner.run(longestStringSuite)
runner.run(toCamelCaseSuite)
