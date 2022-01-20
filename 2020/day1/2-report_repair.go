package main

import (
	"bytes"
	"io/ioutil"
	"log"
	"strconv"
)

func findTriple(content map[int]int, target int) {
	for val, _ := range content {
		twoSum := target - val
		for number, _ := range content {
			thirdNumber := twoSum - number
			if _, ok := content[thirdNumber]; ok {
				log.Println(val * number * thirdNumber)
				return
			}
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

	findTriple(m, 2020)
}
