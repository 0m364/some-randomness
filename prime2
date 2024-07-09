#!/bin/bash

# Function to check if a number is prime
is_prime() {
    local num=$1
    if (( num < 2 )); then
        echo 0
        return
    fi
    for (( i=2; i*i<=num; i++ )); do
        if (( num % i == 0 )); then
            echo 0
            return
        fi
    done
    echo 1
}

# Function to generate the next prime number
next_prime() {
    local num=$1
    while true; do
        (( num++ ))
        if [[ $(is_prime $num) -eq 1 ]]; then
            echo $num
            return
        fi
    done
}

# Terminal size
cols=$(tput cols)
rows=$(tput lines)

# Initialize primes
primes=()
current_prime=1
for (( i=0; i<cols; i++ )); do
    current_prime=$(next_prime $current_prime)
    primes+=($current_prime)
done

# Main loop
while true; do
    clear
    for (( r=0; r<rows; r++ )); do
        line=""
        for (( c=0; c<cols; c++ )); do
            line+=" ${primes[c]} "
        done
        echo -e "$line"
    done

    # Update primes for the next iteration
    for (( i=0; i<cols; i++ )); do
        primes[$i]=$(next_prime ${primes[$i]})
    done

    sleep 0.1
done