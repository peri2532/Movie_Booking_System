class BookingApp:
    def __init__(self):
        self.movies = ['Dune 2', 'Oppenheimer', 'Inside Out 2']
        self.seats = {'Dune 2': 10, 'Oppenheimer': 8, 'Inside Out 2': 12}
    
    def show_movies(self):
        return self.movies
    
    def check_seat(self, movie):
        return self.seats.get(movie, 0) > 0
    
    def book_seat(self, movie):
        if self.check_seat(movie):
            self.seats[movie] -= 1
            return True
        return False

class PaymentSystem:
    def pay(self, amount):
        # 결제 처리 (모의)
        return f"결제 승인 완료: {amount}원"

class TicketSystem:
    def generate_ticket(self, movie):
        # 티켓 생성 및 QR코드 반환 (모의)
        return f"QR-{movie.replace(' ', '')}-12345"

def main():
    user_movie_choice = 'Dune 2'

    booking_app = BookingApp()
    payment_system = PaymentSystem()
    ticket_system = TicketSystem()

    print("[User] 영화 목록 요청")
    movies = booking_app.show_movies()
    print(f"[BookingApp] 제공된 목록: {movies}")

    print(f"[User] 영화 및 좌석 선택: {user_movie_choice}")
    if booking_app.book_seat(user_movie_choice):
        print(f"[BookingApp] 좌석 선택 완료 - {user_movie_choice}")
    else:
        print(f"[BookingApp] 좌석 부족 - {user_movie_choice}")
        return

    print("[User] 결제 요청")
    pay_result = payment_system.pay(12000)
    print(f"[PaymentSystem] {pay_result}")

    ticket = ticket_system.generate_ticket(user_movie_choice)
    print(f"[TicketSystem] 티켓 생성 완료: {ticket}")

    print(f"[BookingApp] 예매 완료: {{'movie': '{user_movie_choice}', 'qr_code': '{ticket}'}}")

if __name__ == "__main__":
    main()
