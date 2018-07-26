a = 5  # bits = 101
b = 4  # bits = 100


def print_dec_and_bits(value):
    print('Dec: {:d} | Bits: {:3b}'.format(value, value))


print_dec_and_bits(a)
print_dec_and_bits(b)

c = a & b  # => 100
d = a | b  # => 101


#---- Example ----

view = 1  # 001
edit = 2  # 010
create = 4  # 100


class User:
    def __init__(self, rights):
        self.rights = rights

    def can_view(self):
        return view & self.rights

    def can_edit(self):
        return edit & self.rights

    def can_create(self):
        return create & self.rights


viewer = User(view)
editor = User(view | edit)  # Also has the view for viewing
creator = User(view | edit | create)  # Also allowed to view and edit

# Ask if viewer has right to do something
if creator.can_view():
    print('Yes')
else:
    print('No')

# Different bitwise operators
# <<, >> = shifting bits
# 3 << 1 means taking decimal 3, shifting the bits of 3 (11) to the left 1 place, which returns 6 (110)
# a << b == a * (2 ** b)
# a >> b == a // (2 ** b) <- integer division, so round down
# XOR is ^ . Returns true if the 2 bits are disagreeing (i.e. 101 ^ 111 returns 010)
# ~a returns complement (i.e. flips all bits) ~00000011 returns 11111100
# To go from positive to negative number (2's complement), flip every bit after the least significant bit
# For example, 00010100 = 20. -20 = 11101100 !

