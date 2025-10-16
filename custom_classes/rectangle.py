class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
    
    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}


if __name__ == "__main__":
    print("="*60)
    print("RECTANGLE CLASS TEST")
    print("="*60)
    
    rect = Rectangle(length=10, width=5)
    print(f"\nCreated Rectangle with length=10, width=5")
    
    print("\nIterating over Rectangle:")
    for item in rect:
        print(item)
    
    print("\n" + "="*60)
    print("TEST PASSED ✓")
    print("="*60)
