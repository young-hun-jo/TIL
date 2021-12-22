package main

import (
	"fmt"

	"github.com/younghun-jo/learngo3_prac/account"
	"github.com/younghun-jo/learngo3_prac/banking"
)

func main() {
	banking := banking.Account{Owner: "younghun", Balance: 10000}
	banking.Owner = "mikyoung" // public(첫 글자 대문자)으로 만들었기 때문에 원소 값 변경 가능
	fmt.Println(banking)

	// struct의 private한 key의 value를 struct 기반으로 생성한 함수로 수정해보기
	account := account.NewAccount("younghun")
	account.Insert(1000)
	fmt.Println(account)

	balance := account.GetBalance()
	fmt.Println(balance)

	err := account.WithDraw(2000)
	if err != nil { // 돈이 없는 경우
		fmt.Println("YOU ARE POOR! Can't be withdrawn!")
	} else {
		fmt.Println(account.GetBalance())
	}

	// 계좌 주인 조회
	fmt.Println(account.GetOwner())

	// 계좌 주인 변경
	account.ChangeOwner("chulhyun")
	fmt.Println(account.GetOwner())

	// struct 출력 매직 메소드 변경 후 출력
	fmt.Println(account)
}
