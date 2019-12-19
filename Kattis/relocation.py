def main():
    company_locations = {}
    N, Q = map(int, input().split())
    companies = list(map(int, input().split()))
    for i in range(N):
        company_locations[i + 1] = companies[i]
    for _ in range(Q):
        query_type, A, B = map(int, input().split())
        if query_type == 1:
            company_locations[A] = B
        else:
            print(abs(company_locations[A] - company_locations[B]))


if __name__ == '__main__':
    main()
