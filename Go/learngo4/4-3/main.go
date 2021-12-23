package main

import (
	"errors"
	"fmt"
	"net/http"
)

type RequestResult struct {
	url    string
	status string
}

var errRequestFailed = errors.New("REQUEST FAILED")

func main() {
	finalResult := make(map[string]string)
	c := make(chan RequestResult)
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
	for _, url := range urls {
		go RoutineRequest(url, c)
	}

	for i := 0; i < len(urls); i++ {
		result := <-c
		finalResult[result.url] = result.status
	}
	for url, status := range finalResult {
		fmt.Println(url, status)
	}
}

func Request(url string) error {
	resp, err := http.Get(url)
	if err != nil || resp.StatusCode >= 400 {
		return errRequestFailed
	}
	return nil
}

func RoutineRequest(url string, c chan<- RequestResult) {
	err := Request(url)
	status := "OK"
	if err != nil {
		status = "FAILED"
	}
	result := RequestResult{url: url, status: status}
	c <- result
}
