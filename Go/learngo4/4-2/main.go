// 간단한 고루틴 만들기!

package main

import (
	"fmt"
	"time"
)

func main() {
	c := make(chan string)
	people := [5]string{"nico", "flynn", "Bob", "Tom", "Eliot"}
	for _, person := range people {
		go IsSexy(person, c)
	}
	for i := 0; i < len(people); i++ {
		fmt.Println(<-c)
	}
}

func IsSexy(person string, c chan string) {
	result := person + " is Sexy!"
	c <- result
	time.Sleep(time.Second * 10)
}
