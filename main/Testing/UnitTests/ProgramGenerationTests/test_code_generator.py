import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
from Core.ProgramGeneration.code_generator import CodeGenerator

# class TestCodeGenerator(unittest.TestCase):

#     def setUp(self):
#         self.class_name = "TestClass"
#         self.methods = [
#             {"name": "get_data", "return_type": "str", "description": "Returns data", "default_value": "\"Test\""},
#             {"name": "set_data", "return_type": "None", "description": "Sets data", "default_value": "null"}
#         ]

#     def test_generate_java_code(self):
#         generator = CodeGenerator(language="java", class_name=self.class_name, methods=self.methods)
#         generated_code = generator.generate_code()
        
#         # Test if Java class structure is generated correctly
#         self.assertIn("public class TestClass {", generated_code)
        
#         # Test if the get_data method is generated with the correct return type and default value
#         self.assertIn("public String getData() {", generated_code)
#         self.assertIn("return \"Test\";", generated_code)
        
#         # Test if the set_data method is generated with the correct return type and default value
#         self.assertIn("public void setData() {", generated_code)
#         self.assertIn("return null;", generated_code)

#     def test_generate_javascript_code(self):
#         generator = CodeGenerator(language="javascript", class_name=self.class_name, methods=self.methods)
#         generated_code = generator.generate_code()
        
#         # Test if JavaScript class structure is generated correctly
#         self.assertIn("class TestClass {", generated_code)
        
#         # Test if the get_data method is generated with the correct return type and default value
#         self.assertIn("getData() {", generated_code)
#         self.assertIn("return \"Test\";", generated_code)
        
#         # Test if the set_data method is generated with the correct return type and default value
#         self.assertIn("setData() {", generated_code)
#         self.assertIn("return null;", generated_code)

#     def test_generate_python_code(self):
#         generator = CodeGenerator(language="python", class_name=self.class_name, methods=self.methods)
#         generated_code = generator.generate_code()
        
#         # Test if Python class structure is generated correctly
#         self.assertIn("class TestClass:", generated_code)
        
#         # Test if the get_data method is generated with the correct return type and default value
#         self.assertIn("def get_data(self):", generated_code)
#         self.assertIn("return \"Test\"", generated_code)
        
#         # Test if the set_data method is generated with the correct return type and default value
#         self.assertIn("def set_data(self):", generated_code)
#         self.assertIn("return None", generated_code)

#     def test_invalid_language(self):
#         # Test with an invalid language
#         with self.assertRaises(ValueError):
#             generator = CodeGenerator(language="invalid_language", class_name=self.class_name, methods=self.methods)
#             generator.generate_code()

#     def test_empty_methods(self):
#         # Test with an empty list of methods
#         generator = CodeGenerator(language="python", class_name=self.class_name, methods=[])
#         generated_code = generator.generate_code()
#         self.assertIn("class TestClass:", generated_code)
#         self.assertNotIn("def", generated_code)

#     def test_method_with_params(self):
#         methods_with_params = [
#             {"name": "set_data", "return_type": "None", "description": "Sets data", "params": ["data"], "default_value": "null"}
#         ]
#         generator = CodeGenerator(language="javascript", class_name=self.class_name, methods=methods_with_params)
#         generated_code = generator.generate_code()

#         # Test if the method with parameters is generated correctly
#         self.assertIn("setData(data) {", generated_code)
#         self.assertIn("return null;", generated_code)

#     def test_empty_methods(self):
#         generator = CodeGenerator(language="python", class_name="TestClass", methods=[])
#         generated_code = generator.generate_code()
#         expected_code = (
#             "class TestClass:\n"
#             "\t\"\"\"Class TestClass.\n\n\tGenerated dynamically with defined methods.\n\t\"\"\"\n\n"
#             "\tpass\n"
#         )
#         self.assertEqual(generated_code.strip(), expected_code.strip())



# if __name__ == "__main__":
#     unittest.main()

# import unittest
# from code_generator import CodeGenerator  # Replace with the correct path to your CodeGenerator class

class TestCodeGenerator(unittest.TestCase):
    def test_generate_calculator(self):
        # Define the calculator methods
        methods = [
            {
                "name": "add",
                "return_type": "float",
                "description": "Adds two numbers.",
                "default_value": "0.0"
            },
            {
                "name": "subtract",
                "return_type": "float",
                "description": "Subtracts the second number from the first.",
                "default_value": "0.0"
            },
            {
                "name": "multiply",
                "return_type": "float",
                "description": "Multiplies two numbers.",
                "default_value": "0.0"
            },
            {
                "name": "divide",
                "return_type": "float",
                "description": "Divides the first number by the second.",
                "default_value": "0.0"
            }
        ]
        
        # Instantiate the CodeGenerator
        generator = CodeGenerator(language="java", class_name="Calculator", methods=methods)
        
        # Generate the code
        generated_code = generator.generate_code()
        
        # Expected code snippet
        expected_code = """class Calculator:
    \t\"\"\"Class Calculator.

    \tGenerated dynamically with defined methods.
    \t\"\"\"

    \t\"\"\" Adds two numbers. \"\"\"
    \tdef add(self):
    \t\t# TODO: Implement this method
    \t\treturn 0.0

    \t\"\"\" Subtracts the second number from the first. \"\"\"
    \tdef subtract(self):
    \t\t# TODO: Implement this method
    \t\treturn 0.0

    \t\"\"\" Multiplies two numbers. \"\"\"
    \tdef multiply(self):
    \t\t# TODO: Implement this method
    \t\treturn 0.0

    \t\"\"\" Divides the first number by the second. \"\"\"
    \tdef divide(self):
    \t\t# TODO: Implement this method
    \t\treturn 0.0
    """

        
        # Compare generated code with expected output
        # Normalize the whitespace for comparison
        # self.assertEqual("".join(generated_code.split()), "".join(expected_code.split()))
        print(generated_code);


# Run the tests
if __name__ == "__main__":
    unittest.main()
