import numpy as np

class RungeKuttaSolver:
    def __init__(self, f, t_start, t_end, y0, h):
        self.f = f  # Система ОДУ
        self.t_start = t_start
        self.t_end = t_end
        self.y0 = np.array(y0)
        self.h = h

    def solve(self):
        t = self.t_start
        y = np.array(self.y0)
        trajectory = [(t, *y)]

        while t < self.t_end:
            k1 = self.f(t, y)
            k2 =self.f(t + self.h*0.5, y + self.h * 0.5 * k1)
            y += self.h * (1 * k2)
            t += self.h
            trajectory.append((t, *y))

        return trajectory