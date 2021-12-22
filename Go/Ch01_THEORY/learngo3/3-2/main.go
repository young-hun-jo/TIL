package main

import (
	"fmt"

	"github.com/younghun-jo/learngo3_prac/3-2/mydict"
)

func main() {
	dictionary := mydict.Dictionary{"First": "First word"}
	fmt.Println(dictionary)

	// 특정 단어 찾기
	second := "Second"
	value, err := dictionary.GetWord(second)
	if err == nil { // nil 이면 단어 있는 것!
		fmt.Println(value)
	} else {
		fmt.Println(err)
	}

	// 특정 단어 삽입
	err1 := dictionary.AddWord("Second", "Second Word")
	if err1 == nil {
		fmt.Println("Finish inserting new word")
	} else {
		fmt.Println(err1)
	}
	err2 := dictionary.AddWord("Second", "Second Word")
	if err2 == nil {
		fmt.Println("Finish inserting new word")
	} else {
		fmt.Println(err2)
	}

}
