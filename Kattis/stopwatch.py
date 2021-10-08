def stopWatch(arr):
  ans = 0
  if len(arr) % 2 == 1:
    return "still running"
  for i in range(1, len(arr), 2):
    ans += arr[i] - arr[i - 1]
  return ans


def main():
  N = int(input())
  arr = [int(input()) for _ in range(N)]
  print(stopWatch(arr))

if __name__ == "__main__":
  main()
