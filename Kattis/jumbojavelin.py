def main():
  N = int(input())
  runningSum = 0
  for _ in range(N):
    runningSum += int(input())
  print(runningSum - N + 1)

if __name__ == "__main__":
  main()
