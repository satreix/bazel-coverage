#!/usr/bin/env bats

source lib.sh

@test "add 1 and 4 prints 5" {
    run add 1 4
    [ "$status" -eq 0 ]
    [ "$output" = "5" ]
}