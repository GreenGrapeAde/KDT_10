/* ------------------------------------------------------
*                        데이터 타입
* 정수의 다양한 표현법/진법
* 2진수 => 0b0101
* 8진수 => 065
* 16진수 => 0x23A
------------------------------------------------------ */
#include <stdio.h>

int main(void) {
    // 숫자의 다양한 진법표기
    int binValue = 0b1001;
    int otaValue = 067;
    int hexValue = 0x1F;
    int decValue = 982;

    // 출력 : %d -- 문자의 코드 값, %c -- 문자
    printf("binValue => %d, %o, %x\n", binValue, binValue, binValue);
    printf("otaValue => %o, %d\n", otaValue, otaValue);
    printf("hexValue => %x, %d\n", hexValue, hexValue);
    printf("decValue => %d, %o, %x\n", decValue, decValue, decValue);

    return 0;
}