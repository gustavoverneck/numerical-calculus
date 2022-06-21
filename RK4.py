# ------ RK4-2 ------
from numpy import *
import matplotlib.pyplot as plt

# Initial Data

def getInitialConditions():
    global t0, x0, v0, tn, dt, function, t_list, x_list, v_list, eq
    eqtype = str(input("Insira as variaveis independentes da sua funcao: "))
    eq = str(input("Insira a equação (t, x, v): "))
    t0 = float(input("Insira t0: "))
    x0 = float(input("Insira x0: "))
    v0 = float(input("Insira v0: "))
    tn = float(input("Insira tf: "))
    dt = input("Insira a precisão [padrao 0.001]: ")
    if dt == "":
        dt = 0.001
    else:
        dt = float(dt)
    t_list = [];    x_list = [];   v_list = []


# RK4
def RK4(t, x, v):
    ti = t0
    xi = x0
    vi = v0

    # Functions
    def fv(t, x, v):
        return v

    def fa(t, x, v):
        global eq
        return eval(eq)

    # Coefficients

    def k1_v(t, x, v):
        return fv(t, x, v)

    def k1_a(t, x, v):
        return fa(t, x, v)

    def k2_v(t, x, v):
        return fv(t+dt, x + dt*k1_v(t,x,v)/2, v+dt*k1_a(t,x,v)/2)

    def k2_a(t, x, v):
        return fa(t+dt, x + dt*k1_v(t,x,v)/2, v+dt*k1_a(t,x,v)/2)

    def k3_v(t, x, v):
        return fv(t + dt,x + dt*k2_v(t,x,v)/2.0, v + dt*k2_a(t,x,v)/2.0)

    def k3_a(t, x, v):
        return fa(t + dt,x + dt*k2_v(t,x,v)/2.0, v + dt*k2_a(t,x,v)/2.0)

    def k4_v(t, x, v):
        return fv(t + dt, x + dt*k3_v(t,x,v), v + dt*k3_a(t,x,v))

    def k4_a(t, x, v):
        return fa(t + dt, x + dt*k3_v(t,x,v), v + dt*k3_a(t,x,v))

    while ti <= tn:
        t_list.append(ti)
        x_list.append(xi)

        xi  = xi + (dt/6.0)*(k1_v(ti,xi,vi) + 2*k2_v(ti,xi,vi) + 2*k3_v(ti,xi,vi) + k4_v(ti,xi,vi))
        v_list.append(vi)
        vi  = vi + (dt/6.0)*(k1_a(ti,xi,vi) + 2*k2_a(ti,xi,vi) + 2*k3_a(ti,xi,vi) + k4_a(ti,xi,vi))
        ti = ti + dt

    return t, x, v

def runCode():
    global t_list, x_list, v_list
    t_list, x_list, v_list = RK4(t_list, x_list, v_list)

def plotGraphs():
    global t_list, x_list, v_list
    # Gráficos	
    fig, axs = plt.subplots(3, 1)

    # 1 - x(t)
    axs[0].plot(t_list, x_list)
    axs[0].set_xlabel('tempo (s)')
    axs[0].set_ylabel('posição (m)')
    axs[0].grid(True)
    # 2 - v(t)
    axs[1].plot(t_list, v_list)
    axs[1].set_xlabel('tempo (s)')
    axs[1].set_ylabel('velocidade (m/s)')
    axs[1].grid(True)
    # 3 - v(x)
    axs[2].plot(x_list, v_list)
    axs[2].set_xlabel('posição (m)')
    axs[2].set_ylabel('velocidade (m/s)')
    axs[2].grid(True)

    fig.tight_layout()
    plt.show()

def main():
    getInitialConditions()
    runCode()
    plotGraphs()

if __name__ == '__main__':
    main()