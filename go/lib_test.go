package lib

import "testing"

func TestAdd(t *testing.T)  {
    const want = 5
    got := Add(1, 4)
    if got != want {
        t.Fatalf("got %d, want %d", got, want)
    }
}
