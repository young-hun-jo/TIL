package main

import (
	"fmt"
	"strings"

	"github.com/younghun-jo/learngo2/something"
)

func multiply(a int, b int) int {
	return a * b
}

func lenAndUpper(word string) (int, string) {
	length := len(word)
	uppercase := strings.ToUpper(word)
	return length, uppercase
}

func repeatNumber(numbers ...int) {
	fmt.Println(numbers)
}

func lenAndLower(word string) (length int, lowercase string) {
	defer fmt.Println("lenAndLower Function is done")
	length = len(word)
	lowercase = strings.ToLower(word)
	return
}

func superAdd(numbers ...int) int {
	total := 0
	for _, num := range numbers {
		total += num
	}
	return total
}

func main() {
	// 단순한 출력문
	fmt.Println("Hello world!")
	// 함수 첫 글자의 대문자로 시작하는 것만 export가 가능함
	something.Uppercase() // something.lowercase() 는 export 안됨!
	// 상수(const) 정의 -> 수정 불가
	const sun string = "Sun is rising"
	fmt.Println(sun)
	// 변수(Variable) 정의 -> 수정 가능
	var name string = "YoungHun"
	name = "Jo YoungHun"
	fmt.Println(name)

	// 곱셈함수 만들기
	multiple_res := multiply(100, 2)
	fmt.Println(multiple_res)

	// 문자열 길이, 대문자형으로 변환하는 multiple return
	length, uppercase := lenAndUpper("Carlos")
	fmt.Println(length, uppercase)

	// 함수에 여러개 인자 넣기
	repeatNumber(1, 2, 3, 4, 5, 6)

	// naked return
	length, lowercase := lenAndLower("Ronaldo")
	fmt.Println(length, lowercase)

	// for loop 구현해서 인자로 넣어준 합 구하기
	sum_res := superAdd(10, 11, 12, 13, 14)
	fmt.Println(sum_res)
}
