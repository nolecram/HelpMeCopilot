#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <pthread.h>

void *CEPSXT1(void *);

void test_CEPSXT1() {
    int arg1 = 1;
    int arg2 = 2;
    void *status1, *status2;
    pthread_t thread1, thread2;

    // Create two threads and call CEPSXT1 function in each thread
    pthread_create(&thread1, NULL, CEPSXT1, &arg1);
    pthread_create(&thread2, NULL, CEPSXT1, &arg2);

    // Wait for threads to complete
    pthread_join(thread1, &status1);
    pthread_join(thread2, &status2);

    // Check return status of each thread
    assert(*(int *)status1 == 1);
    assert(*(int *)status2 == 1);
}

int main() {
    test_CEPSXT1();
    printf("All tests passed.\n");
    return 0;
}