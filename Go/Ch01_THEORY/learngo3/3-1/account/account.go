package account

import (
	"errors"
	"fmt"
)

type Account struct {
	owner   string
	balance int
}

// struct에 함수 만들기
func NewAccount(owner string) *Account {
	account := Account{owner: owner}
	return &account // 새로운 것을 복사하지 않고 원래의 것에 적용하기 위함
}

// struct에 메소드 만들기 -> 입금시키는 시뮬레이션(값을 수정해야 하므로 receiver pointer 사용)
func (a *Account) Insert(amount int) {
	a.balance += amount
}

// struct에 메소드 만들기 -> 잔금 반환하는 시뮬레이션
func (a Account) GetBalance() int {
	return a.balance
}

// 에러 변수
var errNoBalance = errors.New("CAN'T BE WITHDRAWN. YOU ARE POOR")

// struct에 메소드 만들기 -> 인출하는 시뮬레이션(에러 핸들링 까지!)
func (a *Account) WithDraw(amount int) error {
	if a.balance < amount {
		return errNoBalance
	}
	a.balance -= amount
	return nil
}

// 계좌 주인 조회
func (a Account) GetOwner() string {
	return a.owner
}

// 계좌 주인 변경
func (a *Account) ChangeOwner(newOwner string) {
	a.owner = newOwner
}

// struct 출력할 때 나오는 문자열 메직 메소드 변경하기
func (a Account) String() string {
	return fmt.Sprint(a.owner, "'s account. \n Has:", a.balance)
}
