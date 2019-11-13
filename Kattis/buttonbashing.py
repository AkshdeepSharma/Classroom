from collections import deque


def microwave(desired_cooking_time, buttons_list):
    queue = deque()
    HOUR = 60 * 60
    best_button_presses, best_cooking_time = -1, HOUR + 1
    dp = [-1] * (HOUR + 1)
    queue.append((0, 0))
    while queue:
        curr_cooking_time, curr_button_presses = queue.popleft()
        if dp[curr_cooking_time] > 0 and dp[curr_cooking_time] <= curr_button_presses:
            continue
        dp[curr_cooking_time] = curr_button_presses
        if curr_cooking_time >= desired_cooking_time and curr_cooking_time < best_cooking_time:
            best_cooking_time, best_button_presses = curr_cooking_time, curr_button_presses
        for button in buttons_list:
            time = curr_cooking_time + button
            time = min(max(0, time), HOUR)
            queue.append((time, curr_button_presses + 1))
    return best_button_presses, best_cooking_time - desired_cooking_time


def main():
    cases = int(input())
    for _ in range(cases):
        number_of_buttons, desired_cooking_time = map(int, input().split())
        buttons_list = list(map(int, input().split()))
        actual_button_presses, actual_cooking_time = microwave(
            desired_cooking_time, buttons_list)
        print(actual_button_presses, actual_cooking_time)


if __name__ == '__main__':
    main()
