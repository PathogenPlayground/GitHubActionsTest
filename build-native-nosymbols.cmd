@echo off
:: Initialize Visual Studio dev tools
call vs-tools

:: Initialize cmake (if necessary)
if not exist build-nosymbols\build.ninja (
    cmake -G "Ninja" -S external/llvm-project/llvm/ -B build-nosymbols ^
        -DCMAKE_C_COMPILER=cl ^
        -DCMAKE_CXX_COMPILER=cl ^
        -DCMAKE_BUILD_TYPE=Release ^
        -DLLVM_ENABLE_PROJECTS=clang ^
        -DLLVM_INCLUDE_TESTS=off ^
        -DLLVM_INCLUDE_BENCHMARKS=off
)

:: Invoke Ninja
ninja -C build-nosymbols libclang
