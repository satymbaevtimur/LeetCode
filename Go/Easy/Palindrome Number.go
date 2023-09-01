import "strconv"

func isPalindrome(x int) bool {
    numberString := strconv.Itoa(x)

    length := len(numberString)

    for index := 0; index <= length / 2; index++ {
        if numberString[index] != numberString[length - index - 1] {
            return false
        }
    }

    return true
}
