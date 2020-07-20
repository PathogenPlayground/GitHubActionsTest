@echo off
:: Initialize Visual Studio dev tools
call vs-tools

:: Initialize cmake (if necessary)
if not exist build-sccache\build.ninja (
    cmake -G "Ninja" -S external/llvm-project/llvm/ -B build-sccache ^
        -DCMAKE_C_COMPILER=cl ^
        -DCMAKE_CXX_COMPILER=cl ^
        -DCMAKE_C_COMPILER_LAUNCHER="%CD%/sccache.exe" ^
        -DCMAKE_CXX_COMPILER_LAUNCHER="%CD%/sccache.exe" ^
        -DCMAKE_BUILD_TYPE=Release ^
        -DLLVM_ENABLE_PROJECTS=clang ^
        -DLLVM_INCLUDE_TESTS=off ^
        -DLLVM_INCLUDE_BENCHMARKS=off
)

:: Invoke Ninja
ninja -C build-sccache libclang
