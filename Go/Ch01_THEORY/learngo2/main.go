package main

import "fmt"

// if ~ else 구문 적용하기
func getScore(score int) string {
	grade := "A"
	if score > 90 {
		return grade
	} else {
		grade = "B"
		return grade
	}
}

// switch로 if ~ elif ~ else 구문 구현
func getScore2(score int) string {
	grade := "A"
	switch {
	case score > 80:
		grade = "B"
		return grade
	case score > 70:
		grade = "C"
		return grade
	case score > 60:
		grade = "D"
		return grade
	}
	grade = "E"
	return grade
}

// variable expression in if 구문, switch 구문
func veIf(age int) bool {
	if koreanAge := age + 2; koreanAge > 20 {
		return true
	}
	return false
}

func veSwitch(age int) bool {
	switch koreanAge := age + 2; koreanAge {
	case 20:
		return true
	case 30:
		return false
	}
	return true
}

func main() {
	grade := getScore(70)
	fmt.Println(grade)
	B := getScore2(82)
	C := getScore2(71)
	D := getScore2(64)
	E := getScore2(10)
	fmt.Println(B, C, D, E)

	// &(address)를 연결하여 *(Pointer) 활용하기
	a := 10
	b := &a
	fmt.Println(a, b)
	fmt.Println(a, *b)
	a = 50
	fmt.Println(a, *b)

	// array -> 길이, dtype을 지정해주어야 함
	names := [5]string{"Jo", "kim", "lee"}
	names[3] = "Zoo"
	names[4] = "Mok"
	fmt.Println(names, names[3])

	// slice -> 길이 제한이 없는 array
	slice_names := []string{"Jo", "kim", "lee"}
	slice_names = append(slice_names, "Zoo")
	slice_names = append(slice_names, "Mok")
	fmt.Println(slice_names, slice_names[2])

	// map -> 파이썬의 딕셔너리 같은 객체, key, value 각각에 동일한 dtype만 들어갈 수 있음(미리 지정해야 하기 때문에)
	map_names := map[string]string{"name": "younghun", "age": "27"}
	fmt.Println(map_names)
	for k, v := range map_names {
		fmt.Println(k, v)
	}

	// struct 사용
	favorite := []string{"python", "ML", "deep learning"}
	my_struct := my_struct{name: "younghun", age: 27, favorite: favorite}
	fmt.Println(my_struct)
}

// struct 정의 -> type struct_name struc { ... }
type my_struct struct {
	name     string
	age      int
	favorite []string
}
