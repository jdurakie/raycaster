#include <math.h>
#include <Python.h>

/*
DOT PRODUCT
*/
double c_dotProduct(double* p1, double* p2)
{
    static double result[3];
    result = (p1[0] * p2[0]) + (p1[1] * p2[1]) + (p1[2] * p2[2]);
    return result
}

static PyObject* dotProduct(PyObject* self, PyObject* args)
{
    double p1[3];
    double p2[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &p1[0], &p1[1], &p1[2],
                                             &p2[0], &p2[1], &p2[2]))
        return NULL;
    double result = c_magnitude(p1);
    return Py_BuildValue("d", result);
}


/*
MAGNITUDE
*/
double c_magnitude(double* p1)
{
    double x = p1[0];
    double y = p1[1];
    double z = p1[2];
    return pow((x*x) + (y*y) + (z*z), 0.5);
}

static PyObject* magnitude(PyObject* self, PyObject* args)
{
    double p1[3];
    if(!PyArg_ParseTuple(args, "(ddd)", &p1[0], &p1[1], &p1[2]))
        return NULL;
    double result = c_magnitude(p1);
    return Py_BuildValue("d", result);
}


/*
NORMALIZE
*/
double* c_normalize(double* p1)
{
    double mag = c_magnitude(p1);
    static double result[3];
    result[0] = p1[0] / mag;
    result[1] = p1[1] / mag;
    result[2] = p1[2] / mag;
    return result;
}

static PyObject* normalize(PyObject* self, PyObject* args)
{
    double p1[3];
    if(!PyArg_ParseTuple(args, "(ddd)", &p1[0], &p1[1], &p1[2]))
        return NULL;
    double* result = c_normalize(p1);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
SUBTRACT POINT
*/
double * c_subtractPoint(double* left, double* right)
{
    static double result[3];
    result[0] = left[0] - right[0];
    result[1] = left[1] - right[1];
    result[2] = left[2] - right[2];
    return result;
}

static PyObject* subtractPoint(PyObject* self, PyObject* args)
{
    double left[3];
    double right[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &left[0], &left[1], &left[2], 
                                         &right[0], &right[1], &right[2]))
        return NULL;
    double* result = c_subtractPoint(left, right);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
CROSS 
*/
double * c_cross(double x1, double y1, double z1, double x2, double y2, double z2)
{
    static double result[3];
    result[0] = (y1 * z2) - (z1 * y2);
    result[1] = (z1 * x2) - (x1 * z2);
    result[2] = (x1 * y2) - (y1 * x2);
    return result;
}

static PyObject* cross(PyObject* self, PyObject* args)
{
    double x1, y1, z1, x2, y2, z2;
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &x1, &y1, &z1, &x2, &y2, &z2))
        return NULL;
    double* result = c_cross(x1, y1, z1, x2, y2, z2);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}



// Our Module's Function Definition struct
// We require this `NULL` to signal the end of our method
// definition 
static PyMethodDef myMethods[] = {
    { "cross", cross, METH_VARARGS, "Computes cross product"},
    { "subtractPoint", subtractPoint, METH_VARARGS, "Subtracts 2 points (left - right)"},
    { "magnitude", magnitude, METH_VARARGS, "Computes magnitude"},
    { "normalize", normalize, METH_VARARGS, "Normalizes vector"},
    { NULL, NULL, 0, NULL }
};

// Our Module Definition struct
static struct PyModuleDef linalg = {
    PyModuleDef_HEAD_INIT,
    "linalg",
    "Math helper module",
    -1,
    myMethods
};

// Initializes our module using our above struct
PyMODINIT_FUNC PyInit_linalg(void)
{
    return PyModule_Create(&linalg);
}