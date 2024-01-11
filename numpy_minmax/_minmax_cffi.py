import os
from cffi import FFI


ffibuilder = FFI()
ffibuilder.cdef("""
    typedef struct {
        float min_val;
        float max_val;
    } MinMaxResult;
""")
ffibuilder.cdef(
    "MinMaxResult minmax_1d(float *, size_t);"
)
ffibuilder.cdef(
    "MinMaxResult minmax_2d(float *, size_t, size_t);"
)

script_dir = os.path.dirname(os.path.realpath(__file__))
c_file_path = os.path.join(script_dir, "_minmax.c")

with open(c_file_path, "r") as file:
    c_code = file.read()

extra_compile_args = ["-mavx", "-O3", "-Wall"]
if os.name == "posix":
    extra_compile_args.append("-Wextra")

ffibuilder.set_source(
    "_numpy_minmax", c_code, extra_compile_args=extra_compile_args
)


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)
