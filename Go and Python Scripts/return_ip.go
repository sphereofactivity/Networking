package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type Response struct {
	Status string
	Query  string
}

func main() {
	statusCode, ip := getIp()
	fmt.Printf("Endpoint Connection: %s\n", statusCode)
	fmt.Printf("Public Facing IPv4 Address is: %s\n", ip)
}

func getIp() (string, string) {
	req, err := http.Get("http://ip-api.com/json/")
	if err != nil {
		return err.Error(), err.Error()
	}
	defer req.Body.Close()

	var response Response

	if err := json.NewDecoder(req.Body).Decode(&response); err != nil {
		return err.Error(), err.Error()
	}

	return response.Status, response.Query
}
