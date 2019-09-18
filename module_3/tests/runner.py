import unittest

import module_3.tests.Element as Element
import module_3.tests.Elements as Elements
import module_3.tests.Layout as Layout
import module_3.tests.HomePage as HomePage

loader = unittest.TestLoader()

elementSuite = unittest.TestSuite()
elementSuite.addTests(loader.loadTestsFromModule(Element))

elementsSuite = unittest.TestSuite()
elementsSuite.addTests(loader.loadTestsFromModule(Elements))

layoutSuite = unittest.TestSuite()
layoutSuite.addTests(loader.loadTestsFromModule(Layout))

homePageSuite = unittest.TestSuite()
homePageSuite.addTests(loader.loadTestsFromModule(HomePage))

runner = unittest.TextTestRunner(verbosity=3, failfast=True)
runner.run(elementSuite)
runner.run(elementsSuite)
runner.run(layoutSuite)
runner.run(homePageSuite)
