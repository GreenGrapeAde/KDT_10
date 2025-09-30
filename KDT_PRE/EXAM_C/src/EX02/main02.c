/* ------------------------------------------------------
*                        데이터 타입 - 정수형
*                 메모리 낭비를 막기 위해서 다양한 종류 존재
* 타입별 저장이 가능한 범위가 정해져 있음
* 해당 범위를 넘은 경우 => overflow/underflow
------------------------------------------------------ */
#include <stdio.h>

int main(void) {
    // short 범위 : -32768 ~ 32767
    short sMinNum = -32768;    // unerflow
    short sMaxNum = 32767;     // overflow
    float fNum = 1.8f;         // ★★★ f를 붙여주지 않으면 1.800000으로 출력됨, 원래는 에러남

    printf("자료형의 크기를 알아보는 코드\n");
    printf("sMinNum : %d, sMaxNum : %d, fNum : %f\n", sMinNum, sMaxNum, fNum);


    return 0;
}