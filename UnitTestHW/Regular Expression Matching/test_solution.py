import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()
    
testcases = [
    # s, p, expected_res
    ["", "", True],
    ["aa", "a", False],
    ["aa", "a*", True],
    ["ab", ".*", True],
    ["a", ".*.", False],
    ["aab", "c*a*b", True],
    ["aaa", "ab*a*c*a", True]
]


@pytest.mark.parametrize("s, p, expected_res", testcases)
def test_broken_solution(solution, s, p, expected_res):
    assert solution.isMatch(s, p) == expected_res
"""
@pytest.mark.xfail
def test_broken_solution(solution):
    assert solution.isMatch() == 

class Solution:
    # 應輸入s、p，輸出bool
    def isMatch(self, s: str, p: str) -> bool:
        # 不須懂
        def sol(s, p, bp):
            if s=="" and p=="":
                return True
            if p=="":
                return False
            if s=="":
                if len(p) > 1 and p[1] == "*":
                    return sol(s, p[2:], "*")
                return False
            .... you just to know to this  
"""
