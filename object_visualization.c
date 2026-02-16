#include <stdio.h>

void drawObject(int width, int height) {
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (i == 0 || i == height - 1 || j == 0 || j == width - 1) {
                printf("*"); // Draw the border
            } else {
                printf(" "); // Empty space
            }
        }
        printf("\n"); // New line after each row
    }
}

int main() {
    int width = 10;
    int height = 5;
    drawObject(width, height);
    return 0;
}