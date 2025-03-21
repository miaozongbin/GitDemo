#include <stdio.h>

// 递归函数计算斐波那契数列
int fibonacci_recursive(int n) {
    if (n <= 1) {
        return n;
    } else {
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
    }
}

int main() {
    int n, i;
    printf("输入要计算的斐波那契数列的项数: ");
    scanf("%d", &n);

    printf("斐波那契数列: ");
    for (i = 0; i < n; i++) {
        printf("%d ", fibonacci_recursive(i));
    }
    printf("\n");

    return 0;
}