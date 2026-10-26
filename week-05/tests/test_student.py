"""可修改的小测试示例：另选输入，保留自己的预期与解释。

测试通过参数接收课程 fixture，--impl 才能切换候选实现。
不要直接 from operations import pop_last 绕过这个开关。
"""


def test_my_pop_example(pop_last):
    items = [7, 4]

    result = pop_last(items)

    assert result == 4
    assert items == [7]

def test_positive_squares(positive_squares):
    values = [0, 3, 3, -1]

    assert positive_squares(values) == [9, 9]
    assert values == [0, 3, 3, -1]
# 断言说明：
# 第一条断言比较函数的返回结果与预期列表 [9, 9] 是否相同。
# 预期结果来自输入列表中大于 0 的两个元素 3 和 3，它们的平方都是 9。
# 函数不会改变原列表 values，返回的是新列表 [9, 9]。
     
 