def main():
    speed = 80
    capacity, fuel_leak, milesToStation = map(float, input().split())
    mileage = [float(input().split()[1]) for _ in range(6)]
    for i in range(5, -1, -1):
        time = milesToStation / speed
        if capacity / 2 - (milesToStation / mileage[i]) - (fuel_leak * time) > 0:
            print("YES", speed)
            return
        speed -= 5
    print("NO")


if __name__ == "__main__":
    main()
