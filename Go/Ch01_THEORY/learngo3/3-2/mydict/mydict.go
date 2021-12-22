package mydict

import "errors"

// map
type Dictionary map[string]string

var errNoFound = errors.New("THE WORD DOESN'T EXISTED")
var errAlreadyExisted = errors.New("ALREADY IS EXISTED")

// map에다가도 메소드 적용 -> 특정 단어가 사전 내에 존재하는지 체크하는 메소드
func (d Dictionary) GetWord(word string) (string, error) {
	value, exists := d[word]
	if exists { // true는 단어가 존재!
		return value, nil
	}
	return "", errNoFound
}

// map에다가도 메소드 적용 -> 단어를 삽입.(이미 단어가 있으면 삽입하지 않는 에러 핸들링)
func (d Dictionary) AddWord(word, def string) error {
	_, exists := d.GetWord(word)
	switch exists {
	case errNoFound:
		d[word] = def
	case nil:
		return errAlreadyExisted
	}
	return nil
}
