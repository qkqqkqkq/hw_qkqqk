# Book 클래스: 도서 정보를 관리
class Book:
    def __init__(self, title, writer, ISBN, year):
        self.title = title
        self.writer = writer
        self.ISBN = ISBN
        self.year = year
        self.borrow = False  

    def __str__(self):
        status = "대출중" if self.borrow else "대출 가능"
        return f"[{self.title}] {self.writer} ({self.year}) | ISBN:{self.ISBN} | 상태:{status}"


class Member:
    def __init__(self, name, member_id, phone=None, email=None):
        self.name = name
        self.member_id = member_id
        self.phone = phone
        self.email = email
        self.borrowed_books = []  # 대출한 책 목록 

    # 책 대출
    def borrow_book(self, book: Book):
        if not book.borrow:
            book.borrow = True
            self.borrowed_books.append(book)
            return True
        return False

    # 책 반납
    def return_book(self, book: Book):
        if book in self.borrowed_books and book.borrow:
            book.borrow = False
            self.borrowed_books.remove(book)
            return True
        return False

    # 회원 정보 보기
    def show_info(self):
        return {
            "회원명": self.name,
            "회원ID": self.member_id,
            "연락처": self.phone,
            "이메일": self.email,
            "대출중인 책": [b.title for b in self.borrowed_books]
        }

    def __str__(self):
        borrowed_titles = (
            "\n    - " + "\n    - ".join([b.title for b in self.borrowed_books])
            if self.borrowed_books else " 없음"
        )
        return (f"회원명: {self.name}\n"
                f"ID: {self.member_id}\n"
                f"연락처: {self.phone}\n"
                f"이메일: {self.email}\n"
                f"대출 중:{borrowed_titles}")


class Library:
    def __init__(self):
        self.books = []
        self.members = {}

    # 도서 관리(책 추가)
    def add_book(self, book: Book):
        self.books.append(book)

    #(책 삭제)
    def remove_book(self, ISBN):
        self.books = [b for b in self.books if b.ISBN != ISBN]

    # 도서 검색
    def search_by_title(self, title):
        return [b for b in self.books if title in b.title]

    def search_by_writer(self, writer):
        return [b for b in self.books if writer in b.writer]

    def search_by_ISBN(self, ISBN):
        return [b for b in self.books if b.ISBN == ISBN]

    # 회원 관리
    def register_member(self, member: Member):
        self.members[member.member_id] = member

    def get_member(self, member_id):
        return self.members.get(member_id, None)

    # 대출/반납
    def borrow_book(self, member_id, ISBN):
        member = self.get_member(member_id)
        books = self.search_by_ISBN(ISBN)
        if member and books:
            return member.borrow_book(books[0])
        return False

    def return_book(self, member_id, ISBN):
        member = self.get_member(member_id)
        books = self.search_by_ISBN(ISBN)
        if member and books:
            return member.return_book(books[0])
        return False

    # 현황
    def show_all_books(self):
        print("\n=== 📚 보유 도서 목록 ===")
        if not self.books:
            print("등록된 책이 없습니다.")
        for b in self.books:
            print(b)

    def show_all_members(self):
        print("\n=== 👤 회원 목록 ===")
        if not self.members:
            print("등록된 회원이 없습니다.")
        for m in self.members.values():
            print(m)
            print("-" * 40)


#예시
if __name__ == "__main__":
    lib = Library()

    b1 = Book("호의에 대하여", "문형배", "111", 2024)
    b2 = Book("혼모노", "성해나", "222", 2022)
    lib.add_book(b1)
    lib.add_book(b2)

    m1 = Member("박성진", "M001", "010-1234-5678", "psj@email.com")
    lib.register_member(m1)

    lib.borrow_book("M001", "111")
    lib.show_all_books()
    lib.show_all_members()

    lib.return_book("M001", "111")
    lib.show_all_books()
    lib.show_all_members()
