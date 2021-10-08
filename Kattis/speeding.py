def speeding(arr):
  fastestSpeed = -1
  for i in range(1, len(arr)):
    currentSpeed = (arr[i][1] - arr[i - 1][1]) / (arr[i][0] - arr[i - 1][0])
    fastestSpeed = max(fastestSpeed, currentSpeed)
  return int(fastestSpeed)


def main():
  N = int(input())
  arr = [list(map(int, input().split())) for _ in range(N)]
  print(speeding(arr))

if __name__ == "__main__":
  main()
