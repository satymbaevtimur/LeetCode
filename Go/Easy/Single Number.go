func singleNumber(nums []int) int {
    number := 0

    for _, value := range nums {
        number ^= value
    }

    return number
}
