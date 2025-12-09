import pytest
from string_utils import StringUtils

class TestStringUtils:
    string_utils = StringUtils()

 # Тесты для метода capitalize
    def test_capitalize_positive(self):
        assert self.string_utils.capitalize("skypro") == "Skypro"
    
    def test_capitalize_empty(self):
        assert self.string_utils.capitalize("") == ""
    
    def test_capitalize_single_char(self):
        assert self.string_utils.capitalize("a") == "A"
    
    # Тесты для метода trim
    def test_trim_positive(self):
        assert self.string_utils.trim("   skypro") == "skypro"
    
    def test_trim_no_whitespace(self):
        assert self.string_utils.trim("skypro") == "skypro"
    
    def test_trim_empty(self):
        assert self.string_utils.trim("") == ""
    
    def test_trim_multiple_spaces(self):
        assert self.string_utils.trim("      name  ") == "name  "

    # Тесты для метода contains
    def test_contains_positive(self):
        assert self.string_utils.contains("SkyPro", "S") == True
    
    def test_contains_negative(self):
        assert self.string_utils.contains("SkyPro", "U") == False

    def test_contains_empty_string(self):
        assert self.string_utils.contains("", "S") == False
    
        # Тесты для метода delete_symbol
    def test_delete_symbol_positive(self):
        assert self.string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    
    def test_delete_symbol_not_found(self):
        assert self.string_utils.delete_symbol("SkyPro", "u") == "SkyPro"
    
    def test_delete_symbol_empty_string(self):
        assert self.string_utils.delete_symbol("", "S") == ""
    
    def test_delete_symbol_multiple_occurrences(self):
        assert self.string_utils.delete_symbol("SkyProSky", "k") == "SyProSy"
    
    def test_delete_symbol_whole_string(self):
        assert self.string_utils.delete_symbol("SkyPro", "SkyPro") == ""