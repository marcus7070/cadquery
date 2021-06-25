from vtk import vtkXMLPolyDataWriter
from ..shapes import Shape


def exportVTP(
    shape: Shape, fname: str, tolerance: float = 0.1, angularTolerance: float = 0.1
):

    writer = vtkXMLPolyDataWriter()
    writer.SetFileName(fname)
    print("about to call toVtkPolyData")
    writer.SetInputData(shape.toVtkPolyData(tolerance, angularTolerance))
    print("about to write")
    writer.Write()
    print("finished write")


def toString(
    shape: Shape, tolerance: float = 1e-3, angularTolerance: float = 0.1
) -> str:

    writer = vtkXMLPolyDataWriter()
    writer.SetWriteToOutputString(True)
    writer.SetInputData(shape.toVtkPolyData(tolerance, angularTolerance))
    writer.Write()

    return writer.GetOutputString()
