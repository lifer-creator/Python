#include <stdio.h>

// 计算两个整数的和
int add(int a, int b) {
    return a + b;
}

int main(void) {
    int x = 10;
    int y = 20;
    int sum = add(x, y);

    printf("x = %d, y = %d\n", x, y);
    printf("sum = %d\n", sum);

    return 0;
}