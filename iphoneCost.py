class Iphone15Discount:
    def calculate_discount(self, is_student, membership_points):
        base_price = 2000
        if membership_points < 0:
            return "Điểm không hợp lệ"
        if is_student:
            if membership_points <= 1000:
                return base_price - 100
            elif membership_points <= 5000:
                return base_price - 200
            else:
                return base_price - 300
        else:
            if membership_points <= 1000:
                return base_price
            elif membership_points <= 5000:
                return base_price - 100
            else:
                return base_price - 200
