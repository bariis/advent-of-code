package main

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"log"
	"strconv"
)

func findPair(content map[int]int, target int) {
	for val, _ := range content {
		complement := target - val
		if _, ok := content[complement]; ok {
			fmt.Print(val, " * ", complement, " = ", (val * complement))
			return
		}
	}
}

func main() {
	fileBytes, err := ioutil.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	m := make(map[int]int, 0)
	for _, line := range bytes.Split(fileBytes, []byte("\n")) {
		number, err := strconv.Atoi(string(line))
		if err != nil {
			log.Println(err)
		}
		m[number]++
	}

	findPair(m, 2020)
}
