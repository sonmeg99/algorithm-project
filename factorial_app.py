import time

def factorial_iter(n: int) -> int:
    """반복문으로 팩토리얼 계산"""
    if n < 0:
        raise ValueError("n은 0 이상 정수여야 합니다.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n: int) -> int:
    """재귀로 팩토리얼 계산"""
    if n < 0:
        raise ValueError("n은 0 이상 정수여야 합니다.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


def run_with_time(func, n: int):
    """실행 함수와 시간을 함께 반환"""
    start = time.perf_counter()
    result = func(n)
    end = time.perf_counter()
    return result, end - start


def is_int(s: str) -> bool:
    """문자열이 정수인지 확인"""
    try:
        int(s)
        return True
    except ValueError:
        return False


def menu():
    while True:
        print("\n===== 팩토리얼 프로그램 =====")
        print("1. 반복문 방식 실행")
        print("2. 재귀 방식 실행")
        print("3. 두 방식 비교")
        print("4. 테스트 케이스 실행")
        print("5. 종료")
        choice = input("메뉴 선택 >> ")

        if choice in ["1", "2", "3"]:
            n_str = input("정수 n 입력 >> ")
            if not is_int(n_str):
                print("정수를 입력하세요.")
                continue
            n = int(n_str)

            try:
                if choice == "1":
                    result, t = run_with_time(factorial_iter, n)
                    print(f"반복문 결과: {result} (시간: {t:.6f}초)")
                elif choice == "2":
                    result, t = run_with_time(factorial_rec, n)
                    print(f"재귀 결과: {result} (시간: {t:.6f}초)")
                elif choice == "3":
                    r1, t1 = run_with_time(factorial_iter, n)
                    r2, t2 = run_with_time(factorial_rec, n)
                    print(f"반복문 결과: {r1} (시간: {t1:.6f}초)")
                    print(f"재귀 결과: {r2} (시간: {t2:.6f}초)")
            except ValueError as e:
                print("오류:", e)

        elif choice == "4":
            test_cases = [0, 1, 5, 10]
            print("\n=== 테스트 케이스 실행 ===")
            for n in test_cases:
                print(f"\nn = {n}")
                try:
                    r1, t1 = run_with_time(factorial_iter, n)
                    r2, t2 = run_with_time(factorial_rec, n)
                    print(f"반복문 결과: {r1} (시간: {t1:.6f}초)")
                    print(f"재귀 결과: {r2} (시간: {t2:.6f}초)")
                except Exception as e:
                    print("오류:", e)

        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1~5 중 입력하세요.")


if __name__ == "__main__":
    menu()
