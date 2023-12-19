from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL import *

# Initialize
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

# Draw cube
def draw_cube():
    glutWireCube(1)

# Display function
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    draw_cube()
    glutSwapBuffers()

# Main function
def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Simple 3D Graphics Engine")

    glEnable(GL_DEPTH_TEST)
    init()

    glutDisplayFunc(display)
    glutIdleFunc(display)

    glutMainLoop()

if __name__ == "__main__":
    main()
