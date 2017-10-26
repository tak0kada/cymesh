cdef void vadd(double target[3], double a[3], double b[3])
cdef void vsub(double target[3], double a[3], double b[3])
cdef void vmultf(double target[3], double a[3], double f)
cdef void vdivf(double target[3], double a[3], double f) except *
cdef void cross(double target[3], double a[3], double b[3])
cdef void vset(double target[3], double a[3])
cdef void inormalized(double a[3])
cdef double dot(double a[3], double b[3])
cdef double vdist(double a[3], double b[3])
cdef double vangle(double a[3], double b[3])
