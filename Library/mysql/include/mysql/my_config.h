/* include/config.h.  Generated from config.h.in by configure.  */
/* include/config.h.in.  Generated from configure.in by autoheader.  */

/* Define if building universal (internal helper macro) */
#define AC_APPLE_UNIVERSAL_BUILD 1

/* Support big tables */
/* #undef BIG_TABLES */

/* Whether features provided by the user community should be included */
#define COMMUNITY_SERVER 1

/* Define to one of `_getb67', `GETB67', `getb67' for Cray-2 and Cray-YMP
   systems. This function is required for `alloca.c' support on those systems.
   */
/* #undef CRAY_STACKSEG_END */

/* Define to 1 if using `alloca.c'. */
/* #undef C_ALLOCA */

/* Don't use libdbug */
#define DBUG_OFF 1

/* Use libdbug */
/* #undef DBUG_ON */

/* all charsets are available */
#define DEFINE_ALL_CHARACTER_SETS 1

/* Disables the use of --init-file, --skip-grant-tables and --bootstrap
   options */
/* #undef DISABLE_GRANT_OPTIONS */

/* Version of .frm files */
#define DOT_FRM_VERSION 6

/* If Debug Sync Facility should be enabled */
/* #undef ENABLED_DEBUG_SYNC */

/* If LOAD DATA LOCAL INFILE should be enabled by default */
#define ENABLED_LOCAL_INFILE 1

/* If SHOW PROFILE should be enabled */
#define ENABLED_PROFILING 1

/* Enable error injection in MySQL Server */
/* #undef ERROR_INJECT_SUPPORT */

/* Do we have FIONREAD */
#define FIONREAD_IN_SYS_IOCTL 1

/* READLINE: your system defines TIOCGWINSZ in sys/ioctl.h. */
#define GWINSZ_IN_SYS_IOCTL 1

/* Define to 1 if you have the `abi::__cxa_demangle' function. */
#define HAVE_ABI_CXA_DEMANGLE 1

/* Define to 1 if you have the <aio.h> header file. */
#define HAVE_AIO_H 1

/* Define to 1 if you have the `alarm' function. */
#define HAVE_ALARM 1

/* Define to 1 if you have `alloca', as a function or macro. */
#define HAVE_ALLOCA 1

/* Define to 1 if you have <alloca.h> and it should be used (not on Ultrix).
   */
#define HAVE_ALLOCA_H 1

/* Define to 1 if you have the <arpa/inet.h> header file. */
#define HAVE_ARPA_INET_H 1

/* Define to 1 if you have the <asm/termbits.h> header file. */
/* #undef HAVE_ASM_TERMBITS_H */

/* Define to 1 if you have the `atomic_add_long_nv' function. */
/* #undef HAVE_ATOMIC_ADD_LONG_NV */

/* Define to 1 if you have the `atomic_cas_32' function. */
/* #undef HAVE_ATOMIC_CAS_32 */

/* Define to 1 if you have the `atomic_cas_64' function. */
/* #undef HAVE_ATOMIC_CAS_64 */

/* Define to 1 if you have the `atomic_cas_ulong' function. */
/* #undef HAVE_ATOMIC_CAS_ULONG */

/* Define to 1 if you have the `atomic_swap_uchar' function. */
/* #undef HAVE_ATOMIC_SWAP_UCHAR */

/* Define to 1 if you have the `backtrace' function. */
#define HAVE_BACKTRACE 1

/* Define to 1 if you have the `backtrace_symbols' function. */
#define HAVE_BACKTRACE_SYMBOLS 1

/* Define to 1 if you have the `backtrace_symbols_fd' function. */
#define HAVE_BACKTRACE_SYMBOLS_FD 1

/* Define to 1 if you have the `bfill' function. */
/* #undef HAVE_BFILL */

/* Define to 1 if you have the `bmove' function. */
/* #undef HAVE_BMOVE */

/* bool is not defined by all C++ compilators */
#define HAVE_BOOL 1

/* Define to 1 if isinf() uses 80-bit register for intermediate values */
/* #undef HAVE_BROKEN_ISINF */

/* Can netinet be included */
/* #undef HAVE_BROKEN_NETINET_INCLUDES */

/* BSD style signals */
/* #undef HAVE_BSD_SIGNALS */

/* Define to 1 if you have the `bsearch' function. */
#define HAVE_BSEARCH 1

/* Define to 1 if compiler defines __bss_start. */
/* #undef HAVE_BSS_START */

/* Define to 1 if you have the `bzero' function. */
#define HAVE_BZERO 1

/* Define to enable charset armscii8 */
/* #undef HAVE_CHARSET_armscii8 */

/* Define to enable ascii character set */
/* #undef HAVE_CHARSET_ascii */

/* Define to enable charset big5 */
#define HAVE_CHARSET_big5 1

/* Define to enable cp1250 */
#define HAVE_CHARSET_cp1250 1

/* Define to enable charset cp1251 */
/* #undef HAVE_CHARSET_cp1251 */

/* Define to enable charset cp1256 */
/* #undef HAVE_CHARSET_cp1256 */

/* Define to enable charset cp1257 */
/* #undef HAVE_CHARSET_cp1257 */

/* Define to enable charset cp850 */
/* #undef HAVE_CHARSET_cp850 */

/* Define to enable charset cp852 */
/* #undef HAVE_CHARSET_cp852 */

/* Define to enable charset cp866 */
/* #undef HAVE_CHARSET_cp866 */

/* Define to enable charset cp932 */
#define HAVE_CHARSET_cp932 1

/* Define to enable charset dec8 */
/* #undef HAVE_CHARSET_dec8 */

/* Define to enable charset eucjpms */
#define HAVE_CHARSET_eucjpms 1

/* Define to enable charset euckr */
#define HAVE_CHARSET_euckr 1

/* Define to enable charset gb2312 */
#define HAVE_CHARSET_gb2312 1

/* Define to enable charset gbk */
#define HAVE_CHARSET_gbk 1

/* Define to enable charset geostd8 */
/* #undef HAVE_CHARSET_geostd8 */

/* Define to enable charset greek */
/* #undef HAVE_CHARSET_greek */

/* Define to enable charset hebrew */
/* #undef HAVE_CHARSET_hebrew */

/* Define to enable charset hp8 */
/* #undef HAVE_CHARSET_hp8 */

/* Define to enable charset keybcs2 */
/* #undef HAVE_CHARSET_keybcs2 */

/* Define to enable charset koi8r */
/* #undef HAVE_CHARSET_koi8r */

/* Define to enable charset koi8u */
/* #undef HAVE_CHARSET_koi8u */

/* Define to enable charset latin1 */
#define HAVE_CHARSET_latin1 1

/* Define to enable charset latin2 */
#define HAVE_CHARSET_latin2 1

/* Define to enable charset latin5 */
/* #undef HAVE_CHARSET_latin5 */

/* Define to enable charset latin7 */
/* #undef HAVE_CHARSET_latin7 */

/* Define to enable charset macce */
/* #undef HAVE_CHARSET_macce */

/* Define to enable charset macroman */
/* #undef HAVE_CHARSET_macroman */

/* Define to enable charset sjis */
#define HAVE_CHARSET_sjis 1

/* Define to enable charset swe7 */
/* #undef HAVE_CHARSET_swe7 */

/* Define to enable charset tis620 */
#define HAVE_CHARSET_tis620 1

/* Define to enable charset ucs2 */
#define HAVE_CHARSET_ucs2 1

/* Define to enable charset ujis */
#define HAVE_CHARSET_ujis 1

/* Define to enable ut8 */
#define HAVE_CHARSET_utf8 1

/* Define to 1 if you have the `chsize' function. */
/* #undef HAVE_CHSIZE */

/* Define to 1 if you have the `clock_gettime' function. */
/* #undef HAVE_CLOCK_GETTIME */

/* Define to enable compression support */
#define HAVE_COMPRESS 1

/* crypt */
#define HAVE_CRYPT 1

/* Define to 1 if you have the <crypt.h> header file. */
/* #undef HAVE_CRYPT_H */

/* Define to 1 if you have the <curses.h> header file. */
#define HAVE_CURSES_H 1

/* Define to 1 if you have the `cuserid' function. */
/* #undef HAVE_CUSERID */

/* Define to 1 if you have the <cxxabi.h> header file. */
#define HAVE_CXXABI_H 1

/* Define to 1 if you have the declaration of `fdatasync', and to 0 if you
   don't. */
#define HAVE_DECL_FDATASYNC 0

/* Define to 1 if you have the declaration of `madvise', and to 0 if you
   don't. */
#define HAVE_DECL_MADVISE 1

/* Define to 1 if you have the declaration of `SHM_HUGETLB', and to 0 if you
   don't. */
/* #undef HAVE_DECL_SHM_HUGETLB */

/* Define to 1 if you have the declaration of `tgoto', and to 0 if you don't.
   */
#define HAVE_DECL_TGOTO 1

/* Whether we are using DEC threads */
/* #undef HAVE_DEC_THREADS */

/* Define to 1 if you have the <dirent.h> header file. */
#define HAVE_DIRENT_H 1

/* Define to 1 if you have the `dlerror' function. */
#define HAVE_DLERROR 1

/* Define to 1 if you have the <dlfcn.h> header file. */
#define HAVE_DLFCN_H 1

/* Define to 1 if you have the `dlopen' function. */
#define HAVE_DLOPEN 1

/* Define to 1 if you don't have `vprintf' but do have `_doprnt.' */
/* #undef HAVE_DOPRNT */

/* Access checks in embedded library */
/* #undef HAVE_EMBEDDED_PRIVILEGE_CONTROL */

/* Define to 1 if you have the <execinfo.h> header file. */
#define HAVE_EXECINFO_H 1

/* Defined by configure. Use explicit template instantiation. */
#define HAVE_EXPLICIT_TEMPLATE_INSTANTIATION 1

/* Define to 1 if you have the `fchmod' function. */
#define HAVE_FCHMOD 1

/* Define to 1 if you have the `fcntl' function. */
#define HAVE_FCNTL 1

/* Define to 1 if you have the <fcntl.h> header file. */
#define HAVE_FCNTL_H 1

/* Define to 1 if you have the `fconvert' function. */
/* #undef HAVE_FCONVERT */

/* Define to 1 if you have the `fdatasync' function. */
#define HAVE_FDATASYNC 1

/* Define to 1 if you have the <fenv.h> header file. */
#define HAVE_FENV_H 1

/* Define to 1 if you have the `fesetround' function. */
#define HAVE_FESETROUND 1

/* Define to 1 if you have the `fgetln' function. */
#define HAVE_FGETLN 1

/* Define to 1 if you have the `finite' function. */
#define HAVE_FINITE 1

/* Define to 1 if you have the <floatingpoint.h> header file. */
/* #undef HAVE_FLOATINGPOINT_H */

/* Define to 1 if you have the <float.h> header file. */
#define HAVE_FLOAT_H 1

/* Define to 1 if you have the `flockfile' function. */
#define HAVE_FLOCKFILE 1

/* Define to 1 if you have the `fpresetsticky' function. */
/* #undef HAVE_FPRESETSTICKY */

/* Define to 1 if you have the `fpsetmask' function. */
/* #undef HAVE_FPSETMASK */

/* Define to 1 if you have the <fpu_control.h> header file. */
/* #undef HAVE_FPU_CONTROL_H */

/* Define to 1 if the system has the type `fp_except'. */
/* #undef HAVE_FP_EXCEPT */

/* Define to 1 if you have the `fsync' function. */
#define HAVE_FSYNC 1

/* Define to 1 if you have the `ftruncate' function. */
#define HAVE_FTRUNCATE 1

/* Define to 1 if compiler provides atomic builtins. */
#define HAVE_GCC_ATOMIC_BUILTINS 1

/* Define to 1 if you have the `getcwd' function. */
#define HAVE_GETCWD 1

/* Define to 1 if you have the `gethostbyaddr_r' function. */
/* #undef HAVE_GETHOSTBYADDR_R */

/* Define to 1 if you have the `gethostbyname_r' function. */
/* #undef HAVE_GETHOSTBYNAME_R */

/* Solaris define gethostbyname_r with 5 arguments. glibc2 defines this with 6
   arguments */
/* #undef HAVE_GETHOSTBYNAME_R_GLIBC2_STYLE */

/* In OSF 4.0f the 3'd argument to gethostbyname_r is hostent_data * */
/* #undef HAVE_GETHOSTBYNAME_R_RETURN_INT */

/* Define to 1 if you have the `gethrtime' function. */
/* #undef HAVE_GETHRTIME */

/* Define to 1 if you have the `getline' function. */
/* #undef HAVE_GETLINE */

/* Define to 1 if you have the `getpagesize' function. */
#define HAVE_GETPAGESIZE 1

/* Define to 1 if you have the `getpass' function. */
#define HAVE_GETPASS 1

/* Define to 1 if you have the `getpassphrase' function. */
/* #undef HAVE_GETPASSPHRASE */

/* Define to 1 if you have the `getpwnam' function. */
#define HAVE_GETPWNAM 1

/* Define to 1 if you have the `getpwuid' function. */
#define HAVE_GETPWUID 1

/* getpwent() declaration present */
/* #undef HAVE_GETPW_DECLS */

/* Define to 1 if you have the `getrlimit' function. */
#define HAVE_GETRLIMIT 1

/* Define to 1 if you have the `getrusage' function. */
#define HAVE_GETRUSAGE 1

/* Define to 1 if you have the `getwd' function. */
#define HAVE_GETWD 1

/* Define to 1 if you have the `gmtime_r' function. */
#define HAVE_GMTIME_R 1

/* Define to 1 if you have the <grp.h> header file. */
#define HAVE_GRP_H 1

/* HIST_ENTRY is defined in the outer libeditreadline */
#define HAVE_HIST_ENTRY 1

/* pthread_t can be used by GCC atomic builtins */
#define HAVE_IB_ATOMIC_PTHREAD_T_GCC 1

/* pthread_t can be used by solaris atomics */
/* #undef HAVE_IB_ATOMIC_PTHREAD_T_SOLARIS */

/* GCC atomic builtins are available */
#define HAVE_IB_GCC_ATOMIC_BUILTINS 1

/* Does x86 PAUSE instruction exist */
#define HAVE_IB_PAUSE_INSTRUCTION 1

/* Define to 1 if Solaris libc atomic functions are available */
/* #undef HAVE_IB_SOLARIS_ATOMICS */

/* Define to 1 if you have the <ieeefp.h> header file. */
/* #undef HAVE_IEEEFP_H */

/* Define to 1 if you have the `index' function. */
#define HAVE_INDEX 1

/* Define to 1 if you have the `initgroups' function. */
#define HAVE_INITGROUPS 1

/* Define to 1 if the system has the type `int16'. */
/* #undef HAVE_INT16 */

/* Define to 1 if the system has the type `int32'. */
/* #undef HAVE_INT32 */

/* Define to 1 if the system has the type `int64'. */
/* #undef HAVE_INT64 */

/* Define to 1 if the system has the type `int8'. */
/* #undef HAVE_INT8 */

/* Define to 1 if you have the <inttypes.h> header file. */
#define HAVE_INTTYPES_H 1

/* Define to 1 if the system has the type `in_addr_t'. */
#define HAVE_IN_ADDR_T 1

/* isinf() macro or function */
#define HAVE_ISINF 1

/* Define to 1 if you have the `isnan' function. */
#define HAVE_ISNAN 1

/* Define to 1 if you have the `issetugid' function. */
#define HAVE_ISSETUGID 1

/* Define to 1 if you have the `iswctype' function. */
#define HAVE_ISWCTYPE 1

/* Define to 1 if you have the `iswlower' function. */
#define HAVE_ISWLOWER 1

/* Define to 1 if you have the `iswupper' function. */
#define HAVE_ISWUPPER 1

/* Define if mysql_cv_langinfo_codeset=yes */
#define HAVE_LANGINFO_CODESET /**/

/* Define to 1 if you have the <langinfo.h> header file. */
#define HAVE_LANGINFO_H 1

/* Define if you have large pages support */
/* #undef HAVE_LARGE_PAGES */

/* Define to 1 if you have the `c_r' library (-lc_r). */
/* #undef HAVE_LIBC_R */

/* Define to 1 if you have the `dl' library (-ldl). */
#define HAVE_LIBDL 1

/* Define to 1 if you have the `m' library (-lm). */
#define HAVE_LIBM 1

/* Define to 1 if you have the `nsl' library (-lnsl). */
/* #undef HAVE_LIBNSL */

/* Define to 1 if you have the `nsl_r' library (-lnsl_r). */
/* #undef HAVE_LIBNSL_R */

/* Define to 1 if you have the `pthread' library (-lpthread). */
#define HAVE_LIBPTHREAD 1

/* Define if have -lwrap */
/* #undef HAVE_LIBWRAP */

/* Define to 1 if you have the <limits.h> header file. */
#define HAVE_LIMITS_H 1

/* Whether we are using Xavier Leroy's LinuxThreads */
/* #undef HAVE_LINUXTHREADS */

/* Define to 1 if you have the <linux/config.h> header file. */
/* #undef HAVE_LINUX_CONFIG_H */

/* Define to 1 if you have the <locale.h> header file. */
#define HAVE_LOCALE_H 1

/* Define to 1 if you have the `localtime_r' function. */
#define HAVE_LOCALTIME_R 1

/* Define to 1 if you have the `locking' function. */
/* #undef HAVE_LOCKING */

/* Define to 1 if you have the `longjmp' function. */
#define HAVE_LONGJMP 1

/* Define to 1 if you have the `lrand48' function. */
#define HAVE_LRAND48 1

/* Define to 1 if you have the `lstat' function. */
#define HAVE_LSTAT 1

/* Define to 1 if you have the `madvise' function. */
#define HAVE_MADVISE 1

/* Define to 1 if you have the `mallinfo' function. */
/* #undef HAVE_MALLINFO */

/* Define to 1 if you have the <malloc.h> header file. */
/* #undef HAVE_MALLOC_H */

/* Define if you have mbrlen */
#define HAVE_MBRLEN /**/

/* Define if you have mbrtowc */
#define HAVE_MBRTOWC /**/

/* Define if you have mbscmp */
/* #undef HAVE_MBSCMP */

/* Define if you have mbsrtowcs */
#define HAVE_MBSRTOWCS /**/

/* Define if mysql_cv_have_mbstate_t=yes */
#define HAVE_MBSTATE_T /**/

/* Define to 1 if you have the `memcpy' function. */
#define HAVE_MEMCPY 1

/* Define to 1 if you have the `memmove' function. */
#define HAVE_MEMMOVE 1

/* Define to 1 if you have the <memory.h> header file. */
#define HAVE_MEMORY_H 1

/* Define to 1 if you have the `mkstemp' function. */
#define HAVE_MKSTEMP 1

/* Define to 1 if you have the `mlockall' function. */
#define HAVE_MLOCKALL 1

/* Define to 1 if you have the `mmap' function. */
#define HAVE_MMAP 1

/* Define to 1 if you have the `mmap64' function. */
/* #undef HAVE_MMAP64 */

/* Define to 1 if you have the <ndir.h> header file. */
/* #undef HAVE_NDIR_H */

/* Define to 1 if you have the <netinet/in.h> header file. */
#define HAVE_NETINET_IN_H 1

/* For some non posix threads */
/* #undef HAVE_NONPOSIX_PTHREAD_GETSPECIFIC */

/* For some non posix threads */
/* #undef HAVE_NONPOSIX_PTHREAD_MUTEX_INIT */

/* sigwait with one argument */
/* #undef HAVE_NONPOSIX_SIGWAIT */

/* NPTL threads implementation */
/* #undef HAVE_NPTL */

/* Define to 1 if the system has the type `off_t'. */
#define HAVE_OFF_T 1

/* OpenSSL */
/* #undef HAVE_OPENSSL */

/* Define to 1 if you have the <paths.h> header file. */
#define HAVE_PATHS_H 1

/* Define to 1 if you have the `perror' function. */
#define HAVE_PERROR 1

/* Define to 1 if you have the `poll' function. */
#define HAVE_POLL 1

/* Define to 1 if you have the <poll.h> header file. */
#define HAVE_POLL_H 1

/* Define to 1 if you have the `port_create' function. */
/* #undef HAVE_PORT_CREATE */

/* Define to 1 if you have the <port.h> header file. */
/* #undef HAVE_PORT_H */

/* Define to 1 if you have the `posix_fallocate' function. */
/* #undef HAVE_POSIX_FALLOCATE */

/* Signal handling is POSIX (sigset/sighold, etc) */
#define HAVE_POSIX_SIGNALS 1

/* Define to 1 if you have the `pread' function. */
#define HAVE_PREAD 1

/* Define to 1 if you have the `printstack' function. */
/* #undef HAVE_PRINTSTACK */

/* Define to 1 if you have the `pthread_attr_create' function. */
/* #undef HAVE_PTHREAD_ATTR_CREATE */

/* Define to 1 if you have the `pthread_attr_getstacksize' function. */
#define HAVE_PTHREAD_ATTR_GETSTACKSIZE 1

/* Define to 1 if you have the `pthread_attr_setprio' function. */
/* #undef HAVE_PTHREAD_ATTR_SETPRIO */

/* Define to 1 if you have the `pthread_attr_setschedparam' function. */
#define HAVE_PTHREAD_ATTR_SETSCHEDPARAM 1

/* pthread_attr_setscope */
#define HAVE_PTHREAD_ATTR_SETSCOPE 1

/* Define to 1 if you have the `pthread_attr_setstacksize' function. */
#define HAVE_PTHREAD_ATTR_SETSTACKSIZE 1

/* Define to 1 if you have the `pthread_condattr_create' function. */
/* #undef HAVE_PTHREAD_CONDATTR_CREATE */

/* Define to 1 if you have the `pthread_getsequence_np' function. */
/* #undef HAVE_PTHREAD_GETSEQUENCE_NP */

/* Define to 1 if you have the `pthread_init' function. */
/* #undef HAVE_PTHREAD_INIT */

/* Define to 1 if you have the `pthread_key_delete' function. */
#define HAVE_PTHREAD_KEY_DELETE 1

/* Define to 1 if you have the `pthread_rwlock_rdlock' function. */
#define HAVE_PTHREAD_RWLOCK_RDLOCK 1

/* Define to 1 if you have the `pthread_setprio' function. */
/* #undef HAVE_PTHREAD_SETPRIO */

/* Define to 1 if you have the `pthread_setprio_np' function. */
/* #undef HAVE_PTHREAD_SETPRIO_NP */

/* Define to 1 if you have the `pthread_setschedparam' function. */
#define HAVE_PTHREAD_SETSCHEDPARAM 1

/* Define to 1 if you have the `pthread_setschedprio' function. */
/* #undef HAVE_PTHREAD_SETSCHEDPRIO */

/* Define to 1 if you have the `pthread_sigmask' function. */
#define HAVE_PTHREAD_SIGMASK 1

/* pthread_yield function with one argument */
/* #undef HAVE_PTHREAD_YIELD_ONE_ARG */

/* pthread_yield that doesn't take any arguments */
/* #undef HAVE_PTHREAD_YIELD_ZERO_ARG */

/* Define to 1 if you have the `putenv' function. */
#define HAVE_PUTENV 1

/* Define to 1 if you have the <pwd.h> header file. */
#define HAVE_PWD_H 1

/* If we want to have query cache */
#define HAVE_QUERY_CACHE 1

/* POSIX readdir_r */
#define HAVE_READDIR_R 1

/* Define to 1 if you have the `readlink' function. */
#define HAVE_READLINK 1

/* Define to 1 if you have the `realpath' function. */
#define HAVE_REALPATH 1

/* Define to 1 if you have the `regcomp' function. */
#define HAVE_REGCOMP 1

/* Define to 1 if you have the `rename' function. */
#define HAVE_RENAME 1

/* If we want to have response_time_distribution */
#define HAVE_RESPONSE_TIME_DISTRIBUTION 1

/* Define to 1 if system calls automatically restart after interruption by a
   signal. */
#define HAVE_RESTARTABLE_SYSCALLS 1

/* Define to 1 if you have the `re_comp' function. */
/* #undef HAVE_RE_COMP */

/* Define to 1 if you have the `rint' function. */
#define HAVE_RINT 1

/* RTree keys */
#define HAVE_RTREE_KEYS 1

/* Define to 1 if you have the `rwlock_init' function. */
/* #undef HAVE_RWLOCK_INIT */

/* Define to 1 if you have the <sched.h> header file. */
#define HAVE_SCHED_H 1

/* Define to 1 if you have the `sched_yield' function. */
#define HAVE_SCHED_YIELD 1

/* Define to 1 if you have the `select' function. */
#define HAVE_SELECT 1

/* Define to 1 if you have the <select.h> header file. */
/* #undef HAVE_SELECT_H */

/* Define to 1 if you have the <semaphore.h> header file. */
#define HAVE_SEMAPHORE_H 1

/* Define to 1 if you have the `setenv' function. */
#define HAVE_SETENV 1

/* Define to 1 if you have the `setlocale' function. */
#define HAVE_SETLOCALE 1

/* Define to 1 if you have the `setupterm' function. */
/* #undef HAVE_SETUPTERM */

/* Define to 1 if you have the `shmat' function. */
#define HAVE_SHMAT 1

/* Define to 1 if you have the `shmctl' function. */
#define HAVE_SHMCTL 1

/* Define to 1 if you have the `shmdt' function. */
#define HAVE_SHMDT 1

/* Define to 1 if you have the `shmget' function. */
#define HAVE_SHMGET 1

/* Define to 1 if you have the `sigaction' function. */
#define HAVE_SIGACTION 1

/* Define to 1 if you have the `sigaddset' function. */
#define HAVE_SIGADDSET 1

/* Define to 1 if you have the `sigemptyset' function. */
#define HAVE_SIGEMPTYSET 1

/* Define to 1 if you have the `sighold' function. */
#define HAVE_SIGHOLD 1

/* Define to 1 if you have the `sigset' function. */
#define HAVE_SIGSET 1

/* Define to 1 if the system has the type `sigset_t'. */
/* #undef HAVE_SIGSET_T */

/* Define to 1 if you have the `sigthreadmask' function. */
/* #undef HAVE_SIGTHREADMASK */

/* POSIX sigwait */
#define HAVE_SIGWAIT 1

/* Define to 1 if the system has the type `size_t'. */
#define HAVE_SIZE_T 1

/* Define to 1 if you have the `sleep' function. */
#define HAVE_SLEEP 1

/* Define to 1 if you have the `snprintf' function. */
#define HAVE_SNPRINTF 1

/* Define to 1 if you have the `socket' function. */
#define HAVE_SOCKET 1

/* Solaris define gethostbyaddr_r with 7 arguments. glibc2 defines this with 8
   arguments */
/* #undef HAVE_SOLARIS_STYLE_GETHOST */

/* Spatial extentions */
#define HAVE_SPATIAL 1

/* Define to 1 if you have the <stdarg.h> header file. */
#define HAVE_STDARG_H 1

/* Define to 1 if you have the <stddef.h> header file. */
#define HAVE_STDDEF_H 1

/* Define to 1 if you have the <stdint.h> header file. */
#define HAVE_STDINT_H 1

/* Define to 1 if you have the <stdlib.h> header file. */
#define HAVE_STDLIB_H 1

/* Define to 1 if you have the `stpcpy' function. */
#define HAVE_STPCPY 1

/* Define to 1 if you have the `strcasecmp' function. */
#define HAVE_STRCASECMP 1

/* Define to 1 if you have the `strcoll' function. */
#define HAVE_STRCOLL 1

/* Define to 1 if you have the `strdup' function. */
#define HAVE_STRDUP 1

/* Define to 1 if you have the `strerror' function. */
#define HAVE_STRERROR 1

/* Define to 1 if you have the <strings.h> header file. */
#define HAVE_STRINGS_H 1

/* Define to 1 if you have the <string.h> header file. */
#define HAVE_STRING_H 1

/* Define to 1 if you have the `strlcat' function. */
#define HAVE_STRLCAT 1

/* Define to 1 if you have the `strlcpy' function. */
#define HAVE_STRLCPY 1

/* Define to 1 if you have the `strnlen' function. */
/* #undef HAVE_STRNLEN */

/* Define to 1 if you have the `strpbrk' function. */
#define HAVE_STRPBRK 1

/* Define to 1 if you have the `strsep' function. */
#define HAVE_STRSEP 1

/* Define to 1 if you have the `strsignal' function. */
#define HAVE_STRSIGNAL 1

/* Define to 1 if you have the `strstr' function. */
#define HAVE_STRSTR 1

/* Define to 1 if you have the `strtok_r' function. */
#define HAVE_STRTOK_R 1

/* Define to 1 if you have the `strtol' function. */
#define HAVE_STRTOL 1

/* Define to 1 if you have the `strtoll' function. */
#define HAVE_STRTOLL 1

/* Define to 1 if you have the `strtoul' function. */
#define HAVE_STRTOUL 1

/* Define to 1 if you have the `strtoull' function. */
#define HAVE_STRTOULL 1

/* Define to 1 if `st_rdev' is a member of `struct stat'. */
#define HAVE_STRUCT_STAT_ST_RDEV 1

/* Define to 1 if your `struct stat' has `st_rdev'. Deprecated, use
   `HAVE_STRUCT_STAT_ST_RDEV' instead. */
#define HAVE_ST_RDEV 1

/* Define to 1 if you have the <synch.h> header file. */
/* #undef HAVE_SYNCH_H */

/* Define to 1 if you have the <sys/cdefs.h> header file. */
#define HAVE_SYS_CDEFS_H 1

/* Define to 1 if you have the <sys/dir.h> header file. */
#define HAVE_SYS_DIR_H 1

/* Define to 1 if you have the <sys/file.h> header file. */
#define HAVE_SYS_FILE_H 1

/* Define to 1 if you have the <sys/ioctl.h> header file. */
#define HAVE_SYS_IOCTL_H 1

/* Define to 1 if you have the <sys/ipc.h> header file. */
#define HAVE_SYS_IPC_H 1

/* Define to 1 if you have the <sys/malloc.h> header file. */
#define HAVE_SYS_MALLOC_H 1

/* Define to 1 if you have the <sys/mman.h> header file. */
#define HAVE_SYS_MMAN_H 1

/* Define to 1 if you have the <sys/ndir.h> header file. */
/* #undef HAVE_SYS_NDIR_H */

/* Define to 1 if you have the <sys/param.h> header file. */
#define HAVE_SYS_PARAM_H 1

/* Define to 1 if you have the <sys/prctl.h> header file. */
/* #undef HAVE_SYS_PRCTL_H */

/* Define to 1 if you have the <sys/ptem.h> header file. */
/* #undef HAVE_SYS_PTEM_H */

/* Define to 1 if you have the <sys/pte.h> header file. */
/* #undef HAVE_SYS_PTE_H */

/* Define to 1 if you have the <sys/resource.h> header file. */
#define HAVE_SYS_RESOURCE_H 1

/* Define to 1 if you have the <sys/select.h> header file. */
#define HAVE_SYS_SELECT_H 1

/* Define to 1 if you have the <sys/shm.h> header file. */
#define HAVE_SYS_SHM_H 1

/* Define to 1 if you have the <sys/socket.h> header file. */
#define HAVE_SYS_SOCKET_H 1

/* Define to 1 if you have the <sys/stat.h> header file. */
#define HAVE_SYS_STAT_H 1

/* Define to 1 if you have the <sys/stream.h> header file. */
/* #undef HAVE_SYS_STREAM_H */

/* Define to 1 if you have the <sys/timeb.h> header file. */
#define HAVE_SYS_TIMEB_H 1

/* Define to 1 if you have the <sys/types.h> header file. */
#define HAVE_SYS_TYPES_H 1

/* Define to 1 if you have the <sys/un.h> header file. */
#define HAVE_SYS_UN_H 1

/* Define to 1 if you have the <sys/utime.h> header file. */
/* #undef HAVE_SYS_UTIME_H */

/* Define to 1 if you have the <sys/vadvise.h> header file. */
#define HAVE_SYS_VADVISE_H 1

/* Define to 1 if you have the <sys/wait.h> header file. */
#define HAVE_SYS_WAIT_H 1

/* Define to 1 if you have the `tcgetattr' function. */
#define HAVE_TCGETATTR 1

/* Define to 1 if you have the `tell' function. */
/* #undef HAVE_TELL */

/* Define to 1 if you have the `tempnam' function. */
#define HAVE_TEMPNAM 1

/* Define to 1 if you have the <termbits.h> header file. */
/* #undef HAVE_TERMBITS_H */

/* Define to 1 if you have the <termcap.h> header file. */
#define HAVE_TERMCAP_H 1

/* Define to 1 if you have the <termios.h> header file. */
#define HAVE_TERMIOS_H 1

/* Define to 1 if you have the <termio.h> header file. */
/* #undef HAVE_TERMIO_H */

/* Define to 1 if you have the <term.h> header file. */
#define HAVE_TERM_H 1

/* Define to 1 if you have the `thr_setconcurrency' function. */
/* #undef HAVE_THR_SETCONCURRENCY */

/* Timespec has a ts_sec instead of tv_sev */
/* #undef HAVE_TIMESPEC_TS_SEC */

/* Define to 1 if you have the `towlower' function. */
#define HAVE_TOWLOWER 1

/* Define to 1 if you have the `towupper' function. */
#define HAVE_TOWUPPER 1

/* Have the tzname variable */
#define HAVE_TZNAME 1

/* national Unicode collations */
#define HAVE_UCA_COLLATIONS 1

/* Define to 1 if the system has the type `uchar'. */
/* #undef HAVE_UCHAR */

/* Define to 1 if the system has the type `uint'. */
#define HAVE_UINT 1

/* Define to 1 if the system has the type `uint16'. */
/* #undef HAVE_UINT16 */

/* Define to 1 if the system has the type `uint32'. */
/* #undef HAVE_UINT32 */

/* Define to 1 if the system has the type `uint64'. */
/* #undef HAVE_UINT64 */

/* Define to 1 if the system has the type `uint8'. */
/* #undef HAVE_UINT8 */

/* Define to 1 if the system has the type `ulong'. */
/* #undef HAVE_ULONG */

/* Define to 1 if you have the <unistd.h> header file. */
#define HAVE_UNISTD_H 1

/* Have UnixWare 7 (or similar) almost-POSIX threading library */
/* #undef HAVE_UNIXWARE7_THREADS */

/* sighold() is present and usable */
/* #undef HAVE_USG_SIGHOLD */

/* certain Japanese customer */
/* #undef HAVE_UTF8_GENERAL_CS */

/* Define to 1 if you have the <utime.h> header file. */
#define HAVE_UTIME_H 1

/* Define to 1 if `utime(file, NULL)' sets file's timestamp to the present. */
#define HAVE_UTIME_NULL 1

/* Define to 1 if the system has the type `u_int32_t'. */
#define HAVE_U_INT32_T 1

/* Define for Valgrind support */
/* #undef HAVE_VALGRIND */

/* Define to 1 if you have the <valgrind/memcheck.h> header file. */
/* #undef HAVE_VALGRIND_MEMCHECK_H */

/* Define to 1 if you have the <valgrind/valgrind.h> header file. */
/* #undef HAVE_VALGRIND_VALGRIND_H */

/* Define to 1 if you have the <varargs.h> header file. */
/* #undef HAVE_VARARGS_H */

/* Define to 1 if you have the `vidattr' function. */
/* #undef HAVE_VIDATTR */

/* Define to enable buffered read. This works only if syscalls read/recv
   return as soon as there is some data in the kernel buffer, no matter how
   big the given buffer is. */
#define HAVE_VIO_READ_BUFF 1

/* Found vis.h and the strvis() function */
#define HAVE_VIS_H 1

/* Define to 1 if you have the `vprintf' function. */
#define HAVE_VPRINTF 1

/* Define to 1 if you have the <wchar.h> header file. */
#define HAVE_WCHAR_H 1

/* systems should define this type here */
#define HAVE_WCHAR_T 1

/* Define if you have wcrtomb */
#define HAVE_WCRTOMB /**/

/* Define if you have wcscoll */
#define HAVE_WCSCOLL /**/

/* Define if you have wcsdup */
/* #undef HAVE_WCSDUP */

/* Define if you have wctype */
#define HAVE_WCTYPE /**/

/* Define to 1 if you have the <wctype.h> header file. */
#define HAVE_WCTYPE_H 1

/* systems should define this type here */
#define HAVE_WCTYPE_T 1

/* Define if you have wcwidth */
#define HAVE_WCWIDTH /**/

/* Define to 1 if compiler supports weak symbol attribute. */
#define HAVE_WEAK_SYMBOL 1

/* systems should define this type here */
#define HAVE_WINT_T 1

/* Define to 1 if you have the <xfs/xfs.h> header file. */
/* #undef HAVE_XFS_XFS_H */

/* Defined by configure. Using yaSSL for SSL. */
/* #undef HAVE_YASSL */

/* Define if /proc/meminfo shows the huge page size (Linux only) */
/* #undef HUGETLB_USE_PROC_MEMINFO */

/* Define if you have -lwrap */
/* #undef LIBWRAP */

/* Define to the sub-directory in which libtool stores uninstalled libraries.
   */
#define LT_OBJDIR ".libs/"

/* Machine type name, eg sparc */
#define MACHINE_TYPE "x86_64"

/* Maximum number of indexes per table */
#define MAX_INDEXES 64

/* Define the default charset name */
#define MYSQL_DEFAULT_CHARSET_NAME "latin1"

/* Define the default charset name */
#define MYSQL_DEFAULT_COLLATION_NAME "latin1_general_ci"

/* Assume single-CPU mode, no concurrency */
/* #undef MY_ATOMIC_MODE_DUMMY */

/* Use pthread rwlocks for atomic ops */
/* #undef MY_ATOMIC_MODE_RWLOCKS */

/* Define to 1 if you want to use fast mutexes */
/* #undef MY_PTHREAD_FASTMUTEX */

/* Including Ndb Cluster DB sci transporter */
/* #undef NDB_SCI_TRANSPORTER */

/* Including Ndb Cluster DB shared memory transporter */
#define NDB_SHM_TRANSPORTER 1

/* NDB build version */
#define NDB_VERSION_BUILD 54

/* NDB major version */
#define NDB_VERSION_MAJOR 5

/* NDB minor version */
#define NDB_VERSION_MINOR 1

/* NDB status version */
#define NDB_VERSION_STATUS ""

/* Name of package */
#define PACKAGE "mysql"

/* Define to the address where bug reports for this package should be sent. */
#define PACKAGE_BUGREPORT ""

/* Define to the full name of this package. */
#define PACKAGE_NAME "MySQL Server"

/* Define to the full name and version of this package. */
#define PACKAGE_STRING "MySQL Server 5.1.54"

/* Define to the one symbol short name of this package. */
#define PACKAGE_TARNAME "mysql"

/* Define to the home page for this package. */
#define PACKAGE_URL ""

/* Define to the version of this package. */
#define PACKAGE_VERSION "5.1.54"

/* mysql client protocol version */
#define PROTOCOL_VERSION 10

/* qsort returns void */
#define QSORT_TYPE_IS_VOID 1

/* The return type of qsort (int or void). */
#define RETQSORTTYPE void

/* Define as the return type of signal handlers (`int' or `void'). */
#define RETSIGTYPE void

/* The size of `char', as computed by sizeof. */
#define SIZEOF_CHAR 1

/* The size of `char*', as computed by sizeof. */
#define SIZEOF_CHARP 8

/* The size of `int', as computed by sizeof. */
#define SIZEOF_INT 4

/* The size of `long', as computed by sizeof. */
#define SIZEOF_LONG 8

/* The size of `long long', as computed by sizeof. */
#define SIZEOF_LONG_LONG 8

/* The size of `off_t', as computed by sizeof. */
#define SIZEOF_OFF_T 8

/* The size of `pthread_t', as computed by sizeof. */
#define SIZEOF_PTHREAD_T 8

/* The size of `short', as computed by sizeof. */
#define SIZEOF_SHORT 2

/* The size of `void*', as computed by sizeof. */
#define SIZEOF_VOIDP 8

/* The base type of the last arg to accept */
#define SOCKET_SIZE_TYPE socklen_t

/* Last argument to get/setsockopt */
/* #undef SOCKOPT_OPTLEN_TYPE */

/* If using the C implementation of alloca, define if you know the
   direction of stack growth for your system; otherwise it will be
   automatically deduced at runtime.
	STACK_DIRECTION > 0 => grows toward higher addresses
	STACK_DIRECTION < 0 => grows toward lower addresses
	STACK_DIRECTION = 0 => direction of growth unknown */
#define STACK_DIRECTION -1

/* Define to 1 if the `S_IS*' macros in <sys/stat.h> do not work properly. */
/* #undef STAT_MACROS_BROKEN */

/* Define to 1 if you have the ANSI C header files. */
#define STDC_HEADERS 1

/* d_ino member present in struct dirent */
#define STRUCT_DIRENT_HAS_D_INO 1

/* d_namlen member present in struct dirent */
#define STRUCT_DIRENT_HAS_D_NAMLEN 1

/* The struct rlimit type to use with setrlimit */
#define STRUCT_RLIMIT struct rlimit

/* Name of system, eg sun-solaris */
#define SYSTEM_TYPE "apple-darwin10.7.0"

/* Whether we build for Linux */
/* #undef TARGET_OS_LINUX */

/* Define if you want to have threaded code. This may be undef on client code
   */
#define THREAD 1

/* Should the client be thread safe */
#define THREAD_SAFE_CLIENT 1

/* Define to 1 if time_t is unsigned */
/* #undef TIME_T_UNSIGNED */

/* Define to 1 if you can safely include both <sys/time.h> and <time.h>. */
#define TIME_WITH_SYS_TIME 1

/* declaration of TIOCSTAT in sys/ioctl.h */
#define TIOCSTAT_IN_SYS_IOCTL 1

/* Define to 1 if your <sys/time.h> declares `struct tm'. */
/* #undef TM_IN_SYS_TIME */

/* used libedit interface (can we dereference result of
   rl_completion_entry_function) */
#define USE_LIBEDIT_INTERFACE 1

/* Use multi-byte character routines */
#define USE_MB 1

/* */
#define USE_MB_IDENT 1

/* Needs to use mysys_new helpers */
/* #undef USE_MYSYS_NEW */

/* used new readline interface (are rl_completion_func_t and
   rl_compentry_func_t defined) */
/* #undef USE_NEW_READLINE_INTERFACE */

/* Version number of package */
#define VERSION "5.1.54"

/* sighandler type is void (*signal ()) (); */
#define VOID_SIGHANDLER 1

/* Include Archive Storage Engine into mysqld */
#define WITH_ARCHIVE_STORAGE_ENGINE 1

/* Include Basic Write-only Read-never tables into mysqld */
#define WITH_BLACKHOLE_STORAGE_ENGINE 1

/* Include Stores tables in text CSV format into mysqld */
#define WITH_CSV_STORAGE_ENGINE 1

/* Include Example for Storage Engines for developers into mysqld */
/* #undef WITH_EXAMPLE_STORAGE_ENGINE */

/* Include Connects to tables on remote MySQL servers into mysqld */
#define WITH_FEDERATED_STORAGE_ENGINE 1

/* Include Volatile memory based tables into mysqld */
#define WITH_HEAP_STORAGE_ENGINE 1

/* Include Transactional Tables using InnoDB into mysqld */
/* #undef WITH_INNOBASE_STORAGE_ENGINE */

/* Include Transactional Tables using InnoDB into mysqld */
#define WITH_INNODB_PLUGIN_STORAGE_ENGINE 1

/* Include Merge multiple MySQL tables into one into mysqld */
#define WITH_MYISAMMRG_STORAGE_ENGINE 1

/* Include Traditional non-transactional MySQL tables into mysqld */
#define WITH_MYISAM_STORAGE_ENGINE 1

/* Include High Availability Clustered tables into mysqld */
#define WITH_NDBCLUSTER_STORAGE_ENGINE 1

/* Including Ndb Cluster Binlog */
#define WITH_NDB_BINLOG 1

/* Include MySQL Partitioning Support into mysqld */
#define WITH_PARTITION_STORAGE_ENGINE 1

/* Define WORDS_BIGENDIAN to 1 if your processor stores words with the most
   significant byte first (like Motorola and SPARC, unlike Intel). */
#if defined AC_APPLE_UNIVERSAL_BUILD
# if defined __BIG_ENDIAN__
#  define WORDS_BIGENDIAN 1
# endif
#else
# ifndef WORDS_BIGENDIAN
/* #  undef WORDS_BIGENDIAN */
# endif
#endif

/* Number of bits in a file offset, on hosts where this is settable. */
/* #undef _FILE_OFFSET_BITS */

/* makes fseeko etc. visible, on some hosts. */
/* #undef _LARGEFILE_SOURCE */

/* Large files support on AIX-style hosts. */
/* #undef _LARGE_FILES */

/* Define to empty if `const' does not conform to ANSI C. */
/* #undef const */

/* Define to `__inline__' or `__inline' if that's what the C compiler
   calls it, or to nothing if 'inline' is not supported under any name.  */
#ifndef __cplusplus
/* #undef inline */
#endif

/* Define to `long int' if <sys/types.h> does not define. */
/* #undef off_t */

/* Define to `unsigned int' if <sys/types.h> does not define. */
/* #undef size_t */
