import pytest


class Rectangle:
    def __init__(self, w, h):
        if not (isinstance(w, (int, float)) and isinstance(h, (int, float))):
            raise TypeError("value is not numeric")
        if w < 0 or h < 0:
            raise ValueError("dimensions cannot be negative")

        self.width = w
        self.height = h

    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return (self.width + self.height) * 2


def test_rect_type():
    with pytest.raises(TypeError):
        Rectangle("a", 4)
        
def test_rect_neg():
    with pytest.raises(ValueError):
        Rectangle(-3, 4)

@pytest.fixture
def rect():
    return Rectangle(3, 4)

def test_rect_area(rect):
    assert rect.get_area() == 12
    
def test_rect_perimeter(rect):
    assert rect.get_perimeter() == 14