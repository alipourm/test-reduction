/*
 * This is a RANDOMLY GENERATED PROGRAM.
 *
 * Generator: csmith 2.3.0
 * Git version: 30dccd7
 * Options:   --argc --no-arrays --no-bitfields --checksum --no-comma-operators --compound-assignment --no-consts --no-divs --embedded-assigns --pre-incr-operator --no-pre-decr-operator --no-post-incr-operator --post-decr-operator --unary-plus-operator --no-jumps --longlong --int8 --uint8 --float --math64 --no-inline-function --muls --no-safe-math --no-packed-struct --paranoid --no-pointers --structs --unions --volatiles --volatile-pointers --no-const-pointers -o /project/alipour/c-testcases/swarm/tc74.c
 * Seed:      1641338191
 */

#include <float.h>
#include <math.h>
#include "csmith.h"


static long __undefined;

/* --- Struct/Union Declarations --- */
struct S0 {
   volatile int32_t  f0;
   volatile uint8_t  f1;
   volatile uint16_t  f2;
};

/* --- GLOBAL VARIABLES --- */
static int32_t g_10 = 7L;
static struct S0 g_12 = {-1L,255UL,0x7C6AL};/* VOLATILE GLOBAL g_12 */


/* --- FORWARD DECLARATIONS --- */
static struct S0  func_1(void);
static float  func_3(uint8_t  p_4, int32_t  p_5, int64_t  p_6, int64_t  p_7, uint32_t  p_8);


/* --- FUNCTIONS --- */
/* ------------------------------------------ */
/* 
 * reads : g_10 g_12
 * writes: g_10
 */
static struct S0  func_1(void)
{ /* block id: 0 */
    int32_t l_2 = 0x9D786592L;
    int16_t l_9 = (-3L);
    l_2 = (l_2 < func_3(l_2, l_2, l_9, (g_10 ^= 0x5F996F377CC42477LL), (l_2 <= 1L)));
    return g_12;
}


/* ------------------------------------------ */
/* 
 * reads :
 * writes:
 */
static float  func_3(uint8_t  p_4, int32_t  p_5, int64_t  p_6, int64_t  p_7, uint32_t  p_8)
{ /* block id: 2 */
    uint16_t l_11 = 1UL;
    l_11 &= p_8;
    return p_7;
}




/* ---------------------------------------- */
int main (int argc, char* argv[])
{
    int print_hash_value = 0;
    if (argc == 2 && strcmp(argv[1], "1") == 0) print_hash_value = 1;
    platform_main_begin();
    crc32_gentab();
    func_1();
    transparent_crc(g_10, "g_10", print_hash_value);
    transparent_crc(g_12.f0, "g_12.f0", print_hash_value);
    transparent_crc(g_12.f1, "g_12.f1", print_hash_value);
    transparent_crc(g_12.f2, "g_12.f2", print_hash_value);
    platform_main_end(crc32_context ^ 0xFFFFFFFFUL, print_hash_value);
    return 0;
}

/************************ statistics *************************
XXX max struct depth: 1
breakdown:
   depth: 0, occurrence: 4
   depth: 1, occurrence: 1
XXX total union variables: 0

XXX max expression depth: 9
breakdown:
   depth: 1, occurrence: 5
   depth: 9, occurrence: 1

XXX total number of pointers: 0

XXX times a non-volatile is read: 8
XXX times a non-volatile is write: 3
XXX times a volatile is read: 0
XXX    times read thru a pointer: 0
XXX times a volatile is write: 0
XXX    times written thru a pointer: 0
XXX times a volatile is available for access: 0
XXX percentage of non-volatile access: 100

XXX forward jumps: 0
XXX backward jumps: 0

XXX stmts: 4
XXX max block depth: 0
breakdown:
   depth: 0, occurrence: 4

XXX percentage a fresh-made variable is used: 45.5
XXX percentage an existing variable is used: 54.5
********************* end of statistics **********************/

