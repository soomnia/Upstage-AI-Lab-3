# 책 데이터를 CRUD하는 REST API
from fastapi import APIRouter

## 메모리 DB
BOOKS = [{
    'id': 1,
    'title': '변하지 않는 원칙',
    'author': '모건 하우절',
    'url': 'http://yes24.com/변하지않는원칙'
}]

## router
# app 객체가 아닌 router를 불러와 url을 맵핑해준다.

# prefix를 설정해 해당 url을 사용해야만 아래 router로 접근 가능
router = APIRouter(prefix="/api/v1/books", tags=["books"])

# Read
## [GET] /api/v1/books
@router.get('/')
def get_all_books():
    return BOOKS

## 상세 페이지
## [GET] /api/v1/books/{book_id}
## [GET] /api/v1/books/1
@router.get('/{book_id}')
def get_book(book_id: int):
    # next(): 파이썬 내장 함수
    ## 조건을 만족하는 book을 찾으면 반복문을 빠져나옴, 만약 없으면 None 반환
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    # for book in BOOKS:
    #     if book['id'] == book_id:
    #         book
    #         break

    # book이 있으면 반환
    if book:
        return book
    # 없으면 오류 메시지 반환
    return {'error': f"cannot found ID: {book_id}"}

# Create
## [POST] /api/v1/books
@router.post('/')
def create_book(book: dict):
    BOOKS.append(book)
    return book

# Update
## [PUT] /api/v1/books/{book_id}
## 특정 item을 수정
@router.put('/{book_id}')
# 수정할 book_id, 수정할 내용이 반영된 dict
def update_book(book_id: int, book_update: dict):

    # BOOKS에 book_id에 해당하는 데이터가 있는지 확인
    book = next((book for book in BOOKS if book['id'] == book_id), None)

    # items(): key, value 형태로 dict 데이터를 가져옴
    for key, value in book_update.items():
        if key in book:
            # book_update의 value로 수정
            book[key] = value

    return book
  
# Delete
## [DELETE] /api/v1/books/{book_id}
## 특정 item을 삭제
@router.delete('/{book_id}')
def delete_book(book_id: int):
    # del 대신 global하게 새로운 BOOKS 만들기
    global BOOKS

    BOOKS = [ item for item in BOOKS if item['id'] != book_id ]

    # for item in BOOKS:
    #     # 삭제하지 않을 item만 담아 새로운 BOOK 생성
    #     if item['id'] != book_id:
    #         item

    return {'message': f"Success to delete book ID: {book_id}"}