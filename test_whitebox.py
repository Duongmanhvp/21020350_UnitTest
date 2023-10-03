from iphoneCost import Iphone15Discount


def test_white_box():
    discount_calculator = Iphone15Discount()
    assert discount_calculator.calculate_discount(
        False, -500) == "Điểm không hợp lệ"
    assert discount_calculator.calculate_discount(True, 500) == 1900
    assert discount_calculator.calculate_discount(True, 3000) == 1800
    assert discount_calculator.calculate_discount(True, 6000) == 1700
    assert discount_calculator.calculate_discount(False, 500) == 2000
    assert discount_calculator.calculate_discount(False, 3000) == 1900
    assert discount_calculator.calculate_discount(False, 6000) == 1800
