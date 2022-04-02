"""
run bublik.py from console!
"""

from math import sin, cos, sqrt, fabs, ceil
from classes_cp import Vec2, Vec3
import decimal
from decimal import Decimal as dec


import sys


def clamp(value: float, xmin: float, xmax: float):
    return max(min(value, xmax), xmin)


def sign(a: float):
    return (0.0 < a) - (a < 0.0)


def step(edge: float, x: float):
    return x > edge


def length(v):
    if type(v) == Vec2:
        return sqrt(v.x * v.x + v.y * v.y)
    elif type(v) == Vec3:
        return sqrt(v.x * v.x + v.y * v.y + v.z * v.z)


def norm(v: Vec3):
    return v / length(v)


def dot(a: Vec3, b: Vec3):
    return a.x * b.x + a.y * b.y + a.z * b.z


def v_abs (v: Vec3):
    return Vec3(abs(v.x), abs(v.y), abs(v.z))


def v_sign(v: Vec3):
    return Vec3(sign(v.x), sign(v.y), sign(v.z))


def v_step(edge: Vec3, v: Vec3):
    return Vec3(step(edge.x, v.x), step(edge.y, v.y), step(edge.z, v.z))


def reflect(rd: Vec3, n: Vec3):
    return rd - n * (2.0 * dot(n, rd))


def rotateX(a: Vec3, angle):
    # b = a
    b = Vec3(a.x, a.y, a.z)
    b.z = a.z * cos(angle) - a.y * sin(angle)
    b.y = a.z * sin(angle) + a.y * cos(angle)
    return b


def rotateY(a: Vec3, angle):
    # b = a
    b = Vec3(a.x, a.y, a.z)
    b.x = a.x * cos(angle) - a.z * sin(angle)
    b.z = a.x * sin(angle) + a.z * cos(angle)
    return b


def rotateZ(a: Vec3, angle):
    # b = a
    b = Vec3(a.x, a.y, a.z)
    b.x = a.x * cos(angle) - a.y * sin(angle)
    b.y = a.x * sin(angle) + a.y * cos(angle)
    return b


def sphere(ro: Vec3, rd: Vec3, r):
    b = dot(ro, rd)
    c = dot(ro, ro) - r ** 2
    h = b ** 2 - c
    if h < 0.0:
        return Vec2(-1)  #
    h = sqrt(h)
    return Vec2(-b - h, -b + h)


def box(ro: Vec3, rd: Vec3, box_size: Vec3, out_normal: Vec3):
    m = Vec3(1) / rd    #
    n = m * ro
    k = v_abs(m) * box_size
    t1 = -n - k
    t2 = -n + k
    tn = max(max(t1.x, t1.y), t1.z)
    tf = min(min(t2.x, t2.y), t2.z)
    if tn > tf or tf < 0.0:
        return Vec2(-1)    #
    yzx = Vec3(t1.y, t1.z, t1.x)
    zxy = Vec3(t1.z, t1.x, t1.y)
    out_normal = -v_sign(rd) * v_step(yzx, t1) * v_step(zxy, t1)
    return Vec2(tn, tf)


def plane(ro: Vec3, rd: Vec3, p: Vec3, w):
    return -(dot(ro, p) + w) / dot(rd, p)


def get_dist(p: Vec3, t):
    q = Vec2(length(Vec2(p.x, p.y)) - 1.0, p.z)
    return length(q) - 0.5


def bubl_dvum():
    width = 120
    height = 30
    aspect = width / height
    pixel_aspect = 11.0 / 24.0
    gradient = list(" .:!/r(l1Z4H9W8$@")
    gradient_size = len(gradient) - 2

    screen = list(range(width * height + 1))
    screen[width * height] = "\0"

    for t in range(10000):
        for i in range(width):
            for j in range(height):
                uv = Vec2(float(i), float(j)) / Vec2(width, height) * 2.0 - 1.0
                uv.x *= aspect * pixel_aspect
                uv.x += sin(t * 0.001)
                # x = float(i) / width * 2.0 - 1.0
                # y = float(j) / height * 2.0 - 1.0
                # x *= aspect * pixel_aspect
                # x += sin(t * 0.001)
                pixel = ' '
                # dist = float(sqrt(x * x + y * y))
                dist = float(sqrt(uv.x * uv.x + uv.y * uv.y))
                if dist:
                    color = int(1.0 / dist)
                color = clamp(color, 0, gradient_size)
                pixel = gradient[color]
                screen[i + j * width] = pixel

        print(*screen, sep="")



def main():
    decimal.getcontext().prec = 6
    decimal.getcontext().rounding = decimal.ROUND_HALF_UP

    width = 120
    height = 30
    aspect = dec(width / height)
    pixel_aspect = dec(11) / dec(24)
    gradient = list(" .:!/r(l1Z4H9W8$@")
    gradient_size = len(gradient) - 2

    screen = list(range(width * height))    # +1

    for t in range(1, 10000):
        light = norm(Vec3(-0.5, 0.5, -1))
        sphere_pos = Vec3(0, 3, 0)
        for i in range(width):
            for j in range(height):
                uv = Vec2(i, j) / Vec2(width, height) * 2 - 1
                print(uv)
                break
                uv.x = uv.x * aspect * pixel_aspect
                ro = Vec3(-6, 0, 0)
                rd = norm(Vec3(x=2, v=uv))
                ro = rotateY(ro, 0.25)
                rd = rotateY(rd, 0.25)
                ro = rotateZ(ro, t * 0.01)
                rd = rotateZ(rd, t * 0.01)
                diff = 1
                for k in range(5):
                    min_iter = 99999
                    intersection = sphere(ro - sphere_pos, rd, 1)
                    n = Vec3(0)
                    albedo = 1

                    if intersection.x > 0:
                        it_point = ro - sphere_pos + rd * intersection.x
                        min_iter = intersection.x
                        n = norm(it_point)

                    box_n = Vec3(0)   # !!!
                    intersection = box(ro, rd, Vec3(1), box_n)

                    if 0 < intersection.x < min_iter:
                        min_iter = intersection.x
                        n = box_n

                    intersection = Vec2((plane(ro, rd, Vec3(0, 0, -1), 1)))    #
                    if 0 < intersection.x < min_iter:
                        min_iter = intersection.x
                        n = Vec3(0, 0, -1)
                        albedo = 0.5

                    if min_iter < 99999:
                        diff = diff * (dot(n, light) * 0.5 + 0.5) * albedo
                        # diff = round(diff, 7)
                        # print(diff, end=" ")
                        ro = ro + rd * (min_iter - 0.01)
                        rd = reflect(rd, n)
                    else:
                        break

                color = diff * 20
                color = clamp(color, 0, gradient_size)
                color = round(color)  #
                pixel = gradient[color]
                screen[i + j * width] = pixel

        screen[width * height - 1] = "\0"
        # print(*screen, sep="")

        # for el in screen:
        #     sys.stdout.write(str(el))


main()


