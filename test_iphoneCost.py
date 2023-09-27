from iphoneCost import Iphone15Discount


def test_discount_for_regular_customer():
    discount_calculator = Iphone15Discount()
    assert discount_calculator.calculate_discount(
        False, -500) == "Điểm không hợp lệ"
    assert discount_calculator.calculate_discount(False, 500) == 2000
    assert discount_calculator.calculate_discount(False, 1500) == 1900
    assert discount_calculator.calculate_discount(False, 6000) == 1800


def test_discount_for_student_customer():
    discount_calculator = Iphone15Discount()
    assert discount_calculator.calculate_discount(
        True, -500) == "Điểm không hợp lệ"
    assert discount_calculator.calculate_discount(True, 500) == 1900
    assert discount_calculator.calculate_discount(True, 1500) == 1800
    assert discount_calculator.calculate_discount(True, 6000) == 1700
