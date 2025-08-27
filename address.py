# 딕셔너리를 활용하여 간단한 주소록 프로그램 작성

# - 연락처 이름을 키로 하고, 전화번호, 이메일, 주소 등의 정보를 값으로 저장
# - 중첩 딕셔너리 구조를 사용하여 각 연락처마다 여러 정보를 저장
# - 연락처 추가, 삭제, 검색, 수정, 모든 연락처 보기 기능을 구현


contacts = {
    "박성진": {
        "number": "010-0907-0116",
        "email": "qkrtjdwls@example.com",
        "address": "부산시"
    },
    "강영현": {
        "number": "010-0907-1219",
        "email": "rkddudgus@example.com",
        "address": "서울특별시"
    }
}

#연락처 추가
def add_contact(name, number,email,address):
    if name in contacts:
        print(f"{name}은 이미 존재하는 연락처입니다.")
    else:
        contacts[name]={
            "number":number,
            "email":email,
            "address":address
        }
        print(f"{name}의 연락처가 추가되었습니다.")

#연락처 삭제
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name}의 연락처가 삭제되었습니다")
    else:
        print(f"{name}의 연락처는 존재하지 않습니다")

#연락처 검색
def search_contact(name):
    if name in contacts:
        print(f"{name}의 정보:")
        for key,value in contacts[name].items():
            print(f"{key}:{value}")
    else:
        print(f"{name}의 정보가 존재하지 않습니다 ")

#연락처 수정
def update_contact(name, number=None, email=None, address=None):
    if name in contacts:
        if number: contacts[name]["number"] = number
        if email: contacts[name]["email"] = email
        if address: contacts[name]["address"] = address
        print(f"{name}의 정보가 수정되었습니다.")
    else:
        print(f"{name}의 정보가 존재하지 않습니다.")

def show_all_contacts():
    if not contacts:
        print("저장된 연락처가 없습니다.")
    else:
        print("모든 연락처!")
        for name, info in contacts.items():
            print(f"- {name}: {info['number']}, {info['email']}, {info['address']}")


add_contact("김원필", "010-0907-0428", "rladnjsvlf@example.com", "인천광역시")
add_contact("윤도운", "010-0907-0825", "dbsehdns@example.com", "서울특별시")
add_contact("홍길동","010-1234-5678","1234@example.com","제주도")

show_all_contacts()

search_contact("박성진")

update_contact("윤도운",address="경상남도 창원")

delete_contact("홍길동")
show_all_contacts()