/*
 * This is a RANDOMLY GENERATED PROGRAM.
 *
 * Generator: csmith 2.3.0
 * Git version: 30dccd7
 * Options:   --argc --arrays --no-bitfields --checksum --no-comma-operators --no-compound-assignment --consts --no-divs --embedded-assigns --pre-incr-operator --no-pre-decr-operator --no-post-incr-operator --post-decr-operator --unary-plus-operator --jumps --longlong --no-int8 --no-uint8 --float --math64 --no-inline-function --no-muls --no-safe-math --no-packed-struct --paranoid --no-pointers --structs --no-unions --no-volatiles --volatile-pointers --no-const-pointers -o /project/alipour/c-testcases/swarm/tc828.c
 * Seed:      1281988729
 */

#include <float.h>
#include <math.h>
#include "csmith.h"


static long __undefined;

/* --- Struct/Union Declarations --- */
/* --- GLOBAL VARIABLES --- */
static int32_t g_3[6] = {(-10L),(-10L),(-10L),(-10L),(-10L),(-10L)};
static int32_t g_4 = 0L;
static int32_t g_7 = 0xF5872D9EL;


/* --- FORWARD DECLARATIONS --- */
static int16_t  func_1(void);


/* --- FUNCTIONS --- */
/* ------------------------------------------ */
/* 
 * reads : g_3 g_4 g_7
 * writes: g_3 g_4 g_7
 */
static int16_t  func_1(void)
{ /* block id: 0 */
    int32_t l_2[6] = {5L,5L,5L,5L,5L,5L};
    int i;
    for (g_3[5] = 1; (g_3[5] <= 5); g_3[5] += 1)
    { /* block id: 3 */
        int i;
        l_2[g_3[5]] = l_2[g_3[5]];
    }
    for (g_4 = 0; (g_4 <= 2); g_4 += 4)
    { /* block id: 8 */
        uint64_t l_10 = 0x59CDC345FE46C2E7LL;
        for (g_7 = 0; (g_7 == (-25)); g_7--)
        { /* block id: 11 */
            return l_10;
        }
        l_2[2] = g_3[5];
        g_3[5] = l_10;
    }
    l_2[1] = g_3[5];
    l_2[0] = l_2[4];
    return g_3[5];
}




/* ---------------------------------------- */
int main (int argc, char* argv[])
{
    int i;
    int print_hash_value = 0;
    if (argc == 2 && strcmp(argv[1], "1") == 0) print_hash_value = 1;
    platform_main_begin();
    crc32_gentab();
    func_1();
    for (i = 0; i < 6; i = i + 1)
    {
        transparent_crc(g_3[i], "g_3[i]", print_hash_value);
        if (print_hash_value) printf("index = [%d]\n", i);

    }
    transparent_crc(g_4, "g_4", print_hash_value);
    transparent_crc(g_7, "g_7", print_hash_value);
    platform_main_end(crc32_context ^ 0xFFFFFFFFUL, print_hash_value);
    return 0;
}

/************************ statistics *************************
XXX max struct depth: 0
breakdown:
   depth: 0, occurrence: 1
XXX total union variables: 0

XXX max expression depth: 2
breakdown:
   depth: 1, occurrence: 12
   depth: 2, occurrence: 3

XXX total number of pointers: 0

XXX times a non-volatile is read: 10
XXX times a non-volatile is write: 8
XXX times a volatile is read: 0
XXX    times read thru a pointer: 0
XXX times a volatile is write: 0
XXX    times written thru a pointer: 0
XXX times a volatile is available for access: 0
XXX percentage of non-volatile access: 100

XXX forward jumps: 0
XXX backward jumps: 0

XXX stmts: 10
XXX max block depth: 2
breakdown:
   depth: 0, occurrence: 5
   depth: 1, occurrence: 4
   depth: 2, occurrence: 1

XXX percentage a fresh-made variable is used: 9.09
XXX percentage an existing variable is used: 90.9
********************* end of statistics **********************/

