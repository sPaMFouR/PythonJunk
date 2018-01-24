"""
General Numerical Solver for the 1D Time-Dependent Schrodinger's equation.

adapted from code at http://matplotlib.sourceforge.net/examples/animation/double_pendulum_animated.py

Double pendulum formula translated from the C code at
http://www.physics.usyd.edu.au/~wheat/dpend_html/solve_dpend.c

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
from numpy import sin, cos
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.animation as animation

class DoublePendulum:
    """Double Pendulum Class
    init_state is [theta1, theta1_dot, theta2, theta2_dot] in degrees,
    where theta1, omega1 is the angular position and velocity of the first
    pendulum arm, and theta2, omega2 is that of the second pendulum arm
    """
    def __init__(self,
                 init_state=[120, 0, -20, 0],
                 l1=1.0,  # Length of pendulum 1 in metres
                 l2=1.0,  # Length of pendulum 2 in metres
                 m1=1.0,  # Mass of pendulum 1 in kgs
                 m2=1.0,  # Mass of pendulum 2 in kgs
                 g=9.8,  # Acceleration due to gravity, in m/s^2
                 origin=(0, 0)):
        self.init_state = np.asarray(init_state, dtype='float')
        self.params = (l1, l2, m1, m2, g)
        self.origin = origin
        self.time_elapsed = 0
        self.state = self.init_state * np.pi / 180.
        self.x = np.asarray([])
        self.y = np.asarray([])

    def position(self):
        """Compute the current x,y positions of the pendulum arms"""
        (l1, l2, m1, m2, g) = self.params

        self.x = np.cumsum([self.origin[0], l1 * sin(self.state[0]), l2 * sin(self.state[2])])
        self.y = np.cumsum([self.origin[1], -l1 * cos(self.state[0]), -l2 * cos(self.state[2])])

        return (self.x, self.y)

    def energy(self):
        """compute the energy of the current state"""
        (l1, l2, m1, m2, g) = self.params

        # Potential Energy Of The System
        potential_energy = g * (m1 * self.y[1] + m2 * self.y[2])

        # Kinetic Energy Of The System
        kinetic_energy = 0.5 * (
            m1 * (l1 * self.state[1]) ** 2 +
            m2 * ((l1 * self.state[1]) ** 2 + (l2 * self.state[3]) ** 2 +
            2 * l1 * l2 * self.state[1] * self.state[3] * np.cos(self.state[0] - self.state[2])))

        return potential_energy + kinetic_energy

    def dstate_dt(self, state, t):
        """Compute the derivative of the given state"""
        (m1, m2, l1, l2, g) = self.params

        dydx = np.zeros_like(state)
        dydx[0] = state[1]
        dydx[2] = state[3]

        cos_delta = cos(state[2] - state[0])
        sin_delta = sin(state[2] - state[0])

        den1 = (m1 + m2) * l1 - m2 * l1 * (cos_delta) ** 2
        dydx[1] = (m2 * l1 * state[1] * state[1] * sin_delta * cos_delta
                   + m2 * g * sin(state[2]) * cos_delta
                   + m2 * l2 * state[3] * state[3] * sin_delta
                   - (m1 + m2) * G * sin(state[0])) / den1

        den2 = (l2 / l1) * den1
        dydx[3] = (-m2 * l2 * state[3] * state[3] * sin_delta * cos_delta
                   + (m1 + m2) * g * sin(state[0]) * cos_delta
                   - (m1 + m2) * l1 * state[1] * state[1] * sin_delta
                   - (m1 + m2) * g * sin(state[2])) / den2

        return dydx

    def step(self, dt):
        """execute one time step of length dt and update state"""
        self.state = integrate.odeint(self.dstate_dt, self.state, [0, dt])[1]
        self.time_elapsed += dt

#------------------------------------------------------------
# set up initial state and global variables
pendulum = DoublePendulum([180., 50, -20., 0.0])
pendulum1 = DoublePendulum([120., 30, -15., 1.0])
dt = 1./30 # 30 fps

#------------------------------------------------------------
# set up figure and animation
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(-2, 2), ylim=(-2, 2))
ax.grid()

line, = ax.plot([], [], 'o-', lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
energy_text = ax.text(0.02, 0.90, '', transform=ax.transAxes)

def init():
    """initialize animation"""
    line.set_data([], [])
    time_text.set_text('')
    energy_text.set_text('')
    return line, time_text, energy_text


def animate(i):
    """perform animation step"""
    global pendulum, dt
    pendulum.step(dt)

    line.set_data(*pendulum.position())
    time_text.set_text('time = %.1f' % pendulum.time_elapsed)
    energy_text.set_text('energy = %.3f J' % pendulum.energy())
    return line, time_text, energy_text

# choose the interval based on dt and the time to animate one step
from time import time
t0 = time()
animate(0)
t1 = time()
interval = 1000 * dt - (t1 - t0)

ani = animation.FuncAnimation(fig, animate, frames=300,
                              interval=interval, blit=True, init_func=init)

# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#ani.save('double_pendulum.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
