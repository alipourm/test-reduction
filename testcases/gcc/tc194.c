/*
 * This is a RANDOMLY GENERATED PROGRAM.
 *
 * Generator: csmith 2.3.0
 * Git version: 30dccd7
 * Options:   --argc --arrays --no-bitfields --no-checksum --no-comma-operators --no-compound-assignment --consts --no-divs --embedded-assigns --no-pre-incr-operator --no-pre-decr-operator --no-post-incr-operator --post-decr-operator --no-unary-plus-operator --no-jumps --no-longlong --int8 --uint8 --float --no-math64 --inline-function --no-muls --no-safe-math --packed-struct --no-paranoid --pointers --structs --no-unions --volatiles --volatile-pointers --const-pointers -o /project/alipour/c-testcases/swarm/tc194.c
 * Seed:      3810766076
 */


#define NO_LONGLONG

#include <float.h>
#include <math.h>
#include "csmith.h"

volatile uint32_t csmith_sink_ = 0;

static long __undefined;

/* --- Struct/Union Declarations --- */
#pragma pack(push)
#pragma pack(1)
struct S0 {
   volatile int16_t  f0;
   int32_t  f1;
   int32_t  f2;
   float  f3;
   uint32_t  f4;
   volatile uint16_t  f5;
   volatile int8_t  f6;
};
#pragma pack(pop)

/* --- GLOBAL VARIABLES --- */
static uint32_t g_2[8][2][4] = {{{3U,0xEB987642,0xCC25BFC8,0xCC25BFC8},{0x6038591B,0x6038591B,3U,0xCC25BFC8}},{{0x374B1B05,0xEB987642,0x374B1B05,3U},{0x374B1B05,3U,3U,0x374B1B05}},{{0x6038591B,3U,0xCC25BFC8,3U},{3U,0xEB987642,0xCC25BFC8,0xCC25BFC8}},{{0x6038591B,0x6038591B,3U,0xCC25BFC8},{0x374B1B05,0xEB987642,0x374B1B05,3U}},{{0x374B1B05,3U,3U,0x374B1B05},{0x6038591B,3U,0xCC25BFC8,3U}},{{3U,0xEB987642,0xCC25BFC8,0xCC25BFC8},{0x6038591B,0x6038591B,0x374B1B05,0xEB987642}},{{0xCC25BFC8,0x6038591B,0xCC25BFC8,0x374B1B05},{0xCC25BFC8,0x374B1B05,0x374B1B05,0xCC25BFC8}},{{3U,0x374B1B05,0xEB987642,0x374B1B05},{0x374B1B05,0x6038591B,0xEB987642,0xEB987642}}};
static int32_t g_5 = 1;
static int32_t * volatile g_4 = &g_5;/* VOLATILE GLOBAL g_4 */
static struct S0 g_6 = {-1,1,0x3EC3E1B8,0x8.131DDAp+80,4294967293U,0U,1};/* VOLATILE GLOBAL g_6 */


/* --- FORWARD DECLARATIONS --- */
static struct S0  func_1(void);


/* --- FUNCTIONS --- */
/* ------------------------------------------ */
/* 
 * reads : g_2 g_4 g_6
 * writes: g_5
 */
static struct S0  func_1(void)
{ /* block id: 0 */
    int8_t l_3[6][4][7] = {{{1,0xB6,3,0x2A,0,1,0xB6},{0,0xF5,4,0xF5,0,0,(-1)},{0,0,0x95,(-1),0x76,6,0xAD},{(-4),1,4,0x35,3,8,3}},{{0,(-1),(-1),0,0xDB,0x95,3},{0,0x50,(-1),0,0x0E,0x50,1},{1,0,0xF5,(-1),1,1,3},{0,0xEF,0,8,(-4),0xCE,3}},{{0x76,0xAD,(-1),0x2A,0,3,0xAD},{0xA9,0xF5,(-1),0xCE,1,0xCE,(-1)},{1,1,3,0xF5,0x76,1,0xB6},{0xC8,8,4,0xF5,0xC8,0x50,(-4)}},{{0,0xAD,0,0,0x76,0x95,0xE5},{0x0E,1,4,0,1,8,4},{6,0,(-1),0,0,6,3},{0xC8,0,(-4),0,(-4),0,0xC8}},{{1,(-1),(-1),0,1,1,(-1)},{0xA9,0xEF,1,0xF5,0x0E,0xCE,4},{0,0,(-1),0xF5,0xDB,0x76,0xAD},{0,8,(-4),0xCE,3,0xFE,(-4)}},{{1,0xB6,(-1),0x2A,0x76,1,1},{0,8,4,8,0,0x50,(-1)},{6,0,0,(-1),0,6,0xE5},{(-4),0xEF,4,0,3,0xF5,3}}};
    int i, j, k;
    (*g_4) = (g_2[6][0][1] <= l_3[4][2][5]);
    return g_6;
}




/* ---------------------------------------- */
int main (int argc, char* argv[])
{
    int i, j, k;
    int print_hash_value = 0;
    if (argc == 2 && strcmp(argv[1], "1") == 0) print_hash_value = 1;
    platform_main_begin();
    func_1();
    for (i = 0; i < 8; i = i + 1)
    {
        for (j = 0; j < 2; j = j + 1)
        {
            for (k = 0; k < 4; k = k + 1)
            {
                csmith_sink_ = g_2[i][j][k];
            }
        }
    }
    csmith_sink_ = g_5;
    csmith_sink_ = g_6.f0;
    csmith_sink_ = g_6.f1;
    csmith_sink_ = g_6.f2;
    csmith_sink_ = g_6.f3;
    csmith_sink_ = g_6.f4;
    csmith_sink_ = g_6.f5;
    csmith_sink_ = g_6.f6;
    platform_main_end(0,0);
    return 0;
}

/************************ statistics *************************
XXX max struct depth: 1
breakdown:
   depth: 0, occurrence: 2
   depth: 1, occurrence: 1
XXX total union variables: 0

XXX max expression depth: 2
breakdown:
   depth: 1, occurrence: 2
   depth: 2, occurrence: 1

XXX total number of pointers: 1

XXX times a variable address is taken: 1
XXX times a pointer is dereferenced on RHS: 0
breakdown:
XXX times a pointer is dereferenced on LHS: 1
breakdown:
   depth: 1, occurrence: 1
XXX times a pointer is compared with null: 0
XXX times a pointer is compared with address of another variable: 0
XXX times a pointer is compared with another pointer: 0
XXX times a pointer is qualified to be dereferenced: 0

XXX max dereference level: 1
breakdown:
   level: 0, occurrence: 0
   level: 1, occurrence: 1
XXX number of pointers point to pointers: 0
XXX number of pointers point to scalars: 1
XXX number of pointers point to structs: 0
XXX percent of pointers has null in alias set: 0
XXX average alias set size: 1

XXX times a non-volatile is read: 3
XXX times a non-volatile is write: 1
XXX times a volatile is read: 0
XXX    times read thru a pointer: 0
XXX times a volatile is write: 1
XXX    times written thru a pointer: 0
XXX times a volatile is available for access: 0
XXX percentage of non-volatile access: 80

XXX forward jumps: 0
XXX backward jumps: 0

XXX stmts: 2
XXX max block depth: 0
breakdown:
   depth: 0, occurrence: 2

XXX percentage a fresh-made variable is used: 100
XXX percentage an existing variable is used: 0
********************* end of statistics **********************/

