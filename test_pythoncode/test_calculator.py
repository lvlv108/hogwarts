# -*- coding: utf-8 -*-
# @Time:2021/4/23 9:08 上午
# @Author:lvlv
# @File:test_calculator.py
import pytest
import yaml
from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        print("计算开始")
        # 将函数实例话放在setup_class中，使其成为类实例
        self.calc = Calculator()
    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('calc.yml'))['add'],ids = ['addcase1','addcase2','addcase3'])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect
    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('calc.yml'))['sub'],ids = ['subcase1','subcase2','subcase3'])
    def test_sub(self,a,b,expect):
        result = self.calc.sub(a,b)
        assert result == expect
    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('calc.yml'))['mul'],ids = ['mulcase1','mulcase2','mulcase3'])
    def test_mul(self,a,b,expect):
        result = self.calc.mul(a,b)
        assert result == expect
    @pytest.mark.parametrize('a,b,expect',yaml.safe_load(open('calc.yml'))['div'],ids = ['divcase1','divcase2','divcase3'])
    def test_div(self,a,b,expect):
        result = Calculator().div(a,b)
        assert result == expect