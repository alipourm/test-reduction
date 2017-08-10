/*
 * This is a RANDOMLY GENERATED PROGRAM.
 *
 * Generator: csmith 2.3.0
 * Git version: 30dccd7
 * Options:   --argc --arrays --no-bitfields --no-checksum --comma-operators --no-compound-assignment --no-consts --divs --no-embedded-assigns --pre-incr-operator --pre-decr-operator --no-post-incr-operator --no-post-decr-operator --unary-plus-operator --no-jumps --longlong --int8 --uint8 --no-float --no-math64 --no-inline-function --no-muls --no-safe-math --packed-struct --no-paranoid --pointers --no-structs --no-unions --no-volatiles --no-volatile-pointers --const-pointers -o /project/alipour/c-testcases/swarm/tc288.c
 * Seed:      415904752
 */

#include "csmith.h"

volatile uint32_t csmith_sink_ = 0;

static long __undefined;

/* --- Struct/Union Declarations --- */
/* --- GLOBAL VARIABLES --- */
static int32_t g_5[7][5] = {{3L,0L,3L,1L,0L},{0x07222631L,0x565E08CCL,1L,0x07222631L,1L},{0x07222631L,0x07222631L,0x6FF23B1AL,0L,0xCF54C3C6L},{3L,0xCF54C3C6L,1L,1L,0xCF54C3C6L},{0xCF54C3C6L,0x565E08CCL,3L,0xCF54C3C6L,1L},{0L,0xCF54C3C6L,0x6FF23B1AL,0xCF54C3C6L,0L},{3L,0x07222631L,0x565E08CCL,1L,0x07222631L}};
static int32_t *g_7 = &g_5[3][3];


/* --- FORWARD DECLARATIONS --- */
static int16_t  func_1(void);


/* --- FUNCTIONS --- */
/* ------------------------------------------ */
/* 
 * reads : g_5
 * writes: g_5 g_7
 */
static int16_t  func_1(void)
{ /* block id: 0 */
    int8_t l_2 = 1L;
    int32_t *l_3 = (void*)0;
    int32_t *l_4 = &g_5[3][3];
    int32_t **l_6[10];
    int i;
    for (i = 0; i < 10; i = i + 1)
        l_6[i] = &l_3;
    (*l_4) = l_2;
    g_7 = &g_5[2][2];
    return g_5[3][3];
}




/* ---------------------------------------- */
int main (int argc, char* argv[])
{
    int i, j;
    int print_hash_value = 0;
    if (argc == 2 && strcmp(argv[1], "1") == 0) print_hash_value = 1;
    platform_main_begin();
    func_1();
    for (i = 0; i < 7; i = i + 1)
    {
        for (j = 0; j < 5; j = j + 1)
        {
            csmith_sink_ = g_5[i][j];
        }
    }
    platform_main_end(0,0);
    return 0;
}

/************************ statistics *************************
XXX max struct depth: 0
breakdown:
   depth: 0, occurrence: 2
XXX total union variables: 0

XXX max expression depth: 1
breakdown:
   depth: 1, occurrence: 5

XXX total number of pointers: 4

XXX times a variable address is taken: 4
XXX times a pointer is dereferenced on RHS: 0
breakdown:
XXX times a pointer is dereferenced on LHS: 1
breakdown:
   depth: 1, occurrence: 1
XXX times a pointer is compared with null: 0
XXX times a pointer is compared with address of another variable: 0
XXX times a pointer is compared with another pointer: 0
XXX times a pointer is qualified to be dereferenced: 13

XXX max dereference level: 1
breakdown:
   level: 0, occurrence: 0
   level: 1, occurrence: 1
XXX number of pointers point to pointers: 1
XXX number of pointers point to scalars: 3
XXX number of pointers point to structs: 0
XXX percent of pointers has null in alias set: 25
XXX average alias set size: 1

XXX times a non-volatile is read: 2
XXX times a non-volatile is write: 3
XXX times a volatile is read: 0
XXX    times read thru a pointer: 0
XXX times a volatile is write: 0
XXX    times written thru a pointer: 0
XXX times a volatile is available for access: 0
XXX percentage of non-volatile access: 100

XXX forward jumps: 0
XXX backward jumps: 0

XXX stmts: 3
XXX max block depth: 0
breakdown:
   depth: 0, occurrence: 3

XXX percentage a fresh-made variable is used: 40
XXX percentage an existing variable is used: 60
********************* end of statistics **********************/

