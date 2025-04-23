class Amount:
    def __init__(self, amount):
        self.amount = amount

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, request):
        if self.next_handler:
            self.next_handler.handle(request)

class FiftyDollarHandler(Handler):
    def handle(self, request):
        if request.amount >= 50:
            num_fifties = request.amount // 50
            print(f"Dispensing {num_fifties} x $50")
            request.amount -= num_fifties * 50
            if request.amount > 0:
                self.next_handler.handle(request)

class TwentyDollarHandler(Handler):
    def handle(self, request):
        if request.amount >= 20:
            num_twenties = request.amount // 20
            print(f"Dispensing {num_twenties} x $20")
            request.amount -= num_twenties * 20
            if request.amount > 0:
                self.next_handler.handle(request)

class TenDollarHandler(Handler):
    def handle(self, request):
        if request.amount >= 10:
            num_tens = request.amount // 10
            print(f"Dispensing {num_tens} x $10")
            request.amount -= num_tens * 10
            if request.amount > 0:
                self.next_handler.handle(request)

class ErrorHandler(Handler):
    def handle(self, request):
        if request.amount > 0:
            print(f"Error: Cannot dispense the remaining amount of ${request.amount}")

def create_atm_chain():
    error_handler = ErrorHandler()
    ten_handler = TenDollarHandler(error_handler)
    twenty_handler = TwentyDollarHandler(ten_handler)
    fifty_handler = FiftyDollarHandler(twenty_handler)
    return fifty_handler

# Example usage
if __name__ == "__main__":
    atm_chain = create_atm_chain()
    request = Amount(187)
    atm_chain.handle(request)
