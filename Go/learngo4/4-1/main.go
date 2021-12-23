// 다양한 URL에 request 요청 보내기
package main

import (
	"errors"
	"fmt"
	"net/http"
)

var errFailed = errors.New("REQUEST FAILED")

func main() {
	urls := []string{
		"https://www.airbnb.com/",
		"https://www.google.com/",
		"https://www.amazon.com/",
		"https://www.reddit.com/",
		"https://www.google.com/",
		"https://soundcloud.com/",
		"https://www.facebook.com/",
		"https://www.instagram.com/",
		"https://academy.nomadcoders.co/",
	}
	status := "OK"
	for _, url := range urls {
		err := Request(url)
		if err != nil {
			status = "FAILED"
		}
		fmt.Println(url, status)
	}
}

func Request(url string) error {
	resp, err := http.Get(url)
	if err != nil || resp.StatusCode >= 400 {
		return errFailed
	}
	return nil
}
