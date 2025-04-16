def longest_consecutive_ones(n):
    # Convert the number to binary and remove the "0b" prefix
    binary_rep = bin(n)[2:]

    # Split the binary string by '0' and find the longest segment of '1's
    return max(len(seq) for seq in binary_rep.split('0'))

# Input from user
y = int(input("Enter a number: "))

# Output the result
print("Longest consecutive 1's in the binary representation:", longest_consecutive_ones(y))
