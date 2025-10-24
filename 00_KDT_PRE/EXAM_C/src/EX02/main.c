#include <stdio.h>

/*
변수 선언 및 초기화
*/

int main(void) {
    // 변수 선언 : 데이터 저장할 메모리 공간에 라벨 달기
    //            형식 : 데이터타입 변수명;
    //            초기화 하지 않으면 이전에 사용된 데이터들 즉, 쓰레기값이 존재!
    int age;
    int year;
    int month = 9;          // 선언 + 초기화
    int day = 18;           // 선언 + 초기화

    printf("[Before] age : %d, year : %d\n", age, year);  // 임의의 값이 출력된다.
    // 변수 초기화 : 변수 선언 후 처음 데이터 저장하는 것
    //             형식 : 변수명 = 데이터;
    age = 10;
    year = 2025;

    // 출력
    printf("[After] age : %d, year : %d\n", age, year);

    return 0;
}