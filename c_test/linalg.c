#include <math.h>
#include <Python.h>

/*
MULTIPLY BY SCALAR
*/
void c_multiplyByScalar(double* p1, double scalar, double* result)
{
    result[0] = p1[0] * scalar;
    result[1] = p1[1] * scalar;
    result[2] = p1[2] * scalar;
}

static PyObject* multiplyByScalar(PyObject* self, PyObject* args)
{
    double p1[3];
    double scalar;
    double result[3];
    if(!PyArg_ParseTuple(args, "(ddd)d", &p1[0], &p1[1], &p1[2], &scalar))
        return NULL;
    c_multiplyByScalar(p1, scalar, result);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}

/*
DOT PRODUCT
*/
double c_dotProduct(double* p1, double* p2)
{
    static double result;
    result = (p1[0] * p2[0]) + (p1[1] * p2[1]) + (p1[2] * p2[2]);
    return result;
}

static PyObject* dotProduct(PyObject* self, PyObject* args)
{
    double p1[3];
    double p2[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &p1[0], &p1[1], &p1[2],
                                             &p2[0], &p2[1], &p2[2]))
        return NULL;
    double result = c_dotProduct(p1, p2);
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
void c_normalize(double* p1, double* result)
{
    double mag = c_magnitude(p1);
    result[0] = p1[0] / mag;
    result[1] = p1[1] / mag;
    result[2] = p1[2] / mag;
}

static PyObject* normalize(PyObject* self, PyObject* args)
{
    double p1[3];
    double result[3];
    if(!PyArg_ParseTuple(args, "(ddd)", &p1[0], &p1[1], &p1[2]))
        return NULL;
    c_normalize(p1, result);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
SUBTRACT POINT
*/
void c_subtractPoint(double* left, double* right, double* result)
{
    result[0] = left[0] - right[0];
    result[1] = left[1] - right[1];
    result[2] = left[2] - right[2];
}

static PyObject* subtractPoint(PyObject* self, PyObject* args)
{
    double left[3];
    double right[3];
    double result[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &left[0], &left[1], &left[2], 
                                         &right[0], &right[1], &right[2]))
        return NULL;
    c_subtractPoint(left, right, result);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
ADD POINT
*/
void c_addPoint(double* left, double* right, double* result)
{
    result[0] = left[0] + right[0];
    result[1] = left[1] + right[1];
    result[2] = left[2] + right[2];
}

static PyObject* addPoint(PyObject* self, PyObject* args)
{
    double left[3];
    double right[3];
    double result[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &left[0], &left[1], &left[2], 
                                         &right[0], &right[1], &right[2]))
        return NULL;
    c_addPoint(left, right, result);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
CROSS 
*/
void c_cross(double* left, double* right, double* result)
{
    double x1 = left[0];
    double y1 = left[1];
    double z1 = left[2];

    double x2 = right[0];
    double y2 = right[1];
    double z2 = right[2];

    result[0] = (y1 * z2) - (z1 * y2);
    result[1] = (z1 * x2) - (x1 * z2);
    result[2] = (x1 * y2) - (y1 * x2);
}

static PyObject* cross(PyObject* self, PyObject* args)
{
    double left[3];
    double right[3];
    double result[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)", &left[0], &left[1], &left[2], 
                                             &right[0], &right[1], &right[2]))
        return NULL;
    c_cross(left, right, result);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


/*
TRIANGLE-LINE INTERSECT
*/
double* c_triangleLineIntersect(double* tA, double* tB, double* tC, double* lineStart, double* lineEnd)
{
    double p1[3];
    c_subtractPoint(tB, tA, p1);
    double p2[3];
    c_subtractPoint(tC, tA, p2);
    double n1[3];
    c_cross(p1, p2, n1);
    double n[3];
    c_normalize(n1, n);
    printf("n : (%lf, %lf, %lf)\n", n[0], n[1], n[2]);

    double* P = lineStart;
    double* end = lineEnd;
    double* dirv = c_subtractPoint(P, end);
    dirv = c_normalize(dirv);

    double d = c_dotProduct(n, tA);

    double top = d - c_dotProduct(n, P);
    double bottom = c_dotProduct(n, dirv);
    if(bottom < 0.000001 && bottom > -0.00001)
        return 0;
    double t = top / bottom;

    double* dirv_t = c_multiplyByScalar(dirv, t);
    double* Q = c_addPoint(P, dirv_t);

    double* AB = c_subtractPoint(tB, tA);
    double* AQ = c_subtractPoint(Q, tA);
    double ABCross = c_dotProduct(c_cross(AB, AQ), n);
    if(ABCross < 0)
        return 0;

    double* BC = c_subtractPoint(tC, tB);
    double* BQ = c_subtractPoint(Q, tB);
    double BCCross = c_dotProduct(c_cross(BC, BQ), n);
    if(BCCross < 0)
        return 0;

    double* CA = c_subtractPoint(tA, tC);
    double* CQ = c_subtractPoint(Q, tC);
    double CACross = c_dotProduct(c_cross(CA, CQ), n);
    if(CACross < 0)
        return 0;
    return Q;
}

static PyObject* triangleLineIntersect(PyObject* self, PyObject* args)
{
    double tA[3];
    double tB[3];
    double tC[3];
    double start[3];
    double end[3];
    if(!PyArg_ParseTuple(args, "(ddd)(ddd)(ddd)(ddd)(ddd)", 
                               &tA[0], &tA[1], &tA[2], 
                               &tB[0], &tB[1], &tB[2], 
                               &tC[0], &tC[1], &tC[2], 
                               &start[0], &start[1], &start[2], 
                               &end[0], &end[1], &end[2]))
        return NULL;
    double* result = c_triangleLineIntersect(tA, tB, tC, start, end);
    if(result == 0)
        return Py_BuildValue("d", 0);
    return Py_BuildValue("(ddd)", result[0], result[1], result[2]);
}


static PyMethodDef myMethods[] = {
    { "cross", cross, METH_VARARGS, "Computes cross product"},
    { "subtractPoint", subtractPoint, METH_VARARGS, "Subtracts 2 points (left - right)"},
    { "addPoint", addPoint, METH_VARARGS, "Adds 2 points"},
    { "magnitude", magnitude, METH_VARARGS, "Computes magnitude"},
    { "normalize", normalize, METH_VARARGS, "Normalizes vector"},
    { "dotProduct", dotProduct, METH_VARARGS, "Computes dot product"},
    { "multiplyByScalar", multiplyByScalar, METH_VARARGS, "Multiplies point by a scalar"},
    //{ "triangleLineIntersect", triangleLineIntersect, METH_VARARGS, "Finds intersection of line and triangle"},
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