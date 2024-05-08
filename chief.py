def chiefHopper(arr):
    # Write your code here
    su = arr[0]
    for i in range(len(arr) - 1):
        su += arr[i + 1] - arr[i]

    return su