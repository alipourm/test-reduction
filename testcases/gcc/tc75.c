/*
 * This is a RANDOMLY GENERATED PROGRAM.
 *
 * Generator: csmith 2.3.0
 * Git version: 30dccd7
 * Options:   --argc --arrays --bitfields --no-checksum --no-comma-operators --compound-assignment --no-consts --no-divs --embedded-assigns --pre-incr-operator --no-pre-decr-operator --no-post-incr-operator --post-decr-operator --unary-plus-operator --jumps --no-longlong --no-int8 --uint8 --no-float --no-math64 --inline-function --no-muls --safe-math --no-packed-struct --no-paranoid --pointers --structs --no-unions --volatiles --no-volatile-pointers --const-pointers -o /project/alipour/c-testcases/swarm/tc75.c
 * Seed:      1660929502
 */


#define NO_LONGLONG

#include "csmith.h"

volatile uint32_t csmith_sink_ = 0;

static long __undefined;

/* --- Struct/Union Declarations --- */
struct S3 {
   unsigned f0 : 16;
   unsigned f1 : 16;
   volatile uint32_t  f2;
   volatile signed f3 : 1;
   unsigned f4 : 29;
   volatile unsigned f5 : 22;
   volatile unsigned f6 : 27;
};

/* --- GLOBAL VARIABLES --- */
static struct S3 g_2 = {16,87,4294967295U,0,11320,683,8487};/* VOLATILE GLOBAL g_2 */
static struct S3 g_3 = {24,226,0U,0,13,1326,7472};/* VOLATILE GLOBAL g_3 */


/* --- FORWARD DECLARATIONS --- */
static int32_t  func_1(void);


/* --- FUNCTIONS --- */
/* ------------------------------------------ */
/* 
 * reads : g_2
 * writes: g_3
 */
static int32_t  func_1(void)
{ /* block id: 0 */
    g_3 = g_2;
    return g_2.f0;
}




/* ---------------------------------------- */
int main (int argc, char* argv[])
{
    int print_hash_value = 0;
    if (argc == 2 && strcmp(argv[1], "1") == 0) print_hash_value = 1;
    platform_main_begin();
    func_1();
    csmith_sink_ = g_2.f0;
    csmith_sink_ = g_2.f1;
    csmith_sink_ = g_2.f2;
    csmith_sink_ = g_2.f3;
    csmith_sink_ = g_2.f4;
    csmith_sink_ = g_2.f5;
    csmith_sink_ = g_2.f6;
    csmith_sink_ = g_3.f0;
    csmith_sink_ = g_3.f1;
    csmith_sink_ = g_3.f2;
    csmith_sink_ = g_3.f3;
    csmith_sink_ = g_3.f4;
    csmith_sink_ = g_3.f5;
    csmith_sink_ = g_3.f6;
    platform_main_end(0,0);
    return 0;
}

/************************ statistics *************************
XXX max struct depth: 1
breakdown:
   depth: 0, occurrence: 0
   depth: 1, occurrence: 2
XXX total union variables: 0

XXX non-zero bitfields defined in structs: 6
XXX zero bitfields defined in structs: 0
XXX const bitfields defined in structs: 0
XXX volatile bitfields defined in structs: 3
XXX structs with bitfields in the program: 2
breakdown:
   indirect level: 0, occurrence: 2
XXX full-bitfields structs in the program: 0
breakdown:
XXX times a bitfields struct's address is taken: 0
XXX times a bitfields struct on LHS: 1
XXX times a bitfields struct on RHS: 1
XXX times a single bitfield on LHS: 0
XXX times a single bitfield on RHS: 1

XXX max expression depth: 1
breakdown:
   depth: 1, occurrence: 3

XXX total number of pointers: 0

XXX times a non-volatile is read: 2
XXX times a non-volatile is write: 1
XXX times a volatile is read: 0
XXX    times read thru a pointer: 0
XXX times a volatile is write: 0
XXX    times written thru a pointer: 0
XXX times a volatile is available for access: 1
XXX percentage of non-volatile access: 100

XXX forward jumps: 0
XXX backward jumps: 0

XXX stmts: 2
XXX max block depth: 0
breakdown:
   depth: 0, occurrence: 2

XXX percentage a fresh-made variable is used: 66.7
XXX percentage an existing variable is used: 33.3
FYI: the random generator makes assumptions about the integer size. See platform.info for more details.
********************* end of statistics **********************/

